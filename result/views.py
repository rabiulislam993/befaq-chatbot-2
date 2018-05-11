import re
import json
import time
import random
import requests
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import EXAM_YEARS, MARHALA, Result, Proxy

from result.bijoy_to_unicode import convertBijoyToUnicode


executor = ThreadPoolExecutor(10)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_result_from_befaq_server(exam_year, marhala, roll):
    all_proxies = Proxy.objects.all()

    result_url = "http://wifaqresult.com/result/{year}/{marhala}/{roll}". \
        format(year=exam_year, marhala=marhala, roll=roll)
    # r = requests.get(result_url, headers=headers)
    # random_proxy = ''

    random_proxy = random.choice(all_proxies)
    proxy_dict = {"http": random_proxy.ip}

    while True:
        try:
            r = requests.get(result_url, headers=headers)
            if r.status_code == 429:
                time.sleep(60)
                r = requests.get(result_url, headers=headers)

            r.encoding = 'utf-8'
            result = bs(r.text, "html.parser")
            try:
                result_in_js = result.find_all('script')[-1]
                pattern = re.compile(
                    "var result = (?P<result>{[\n\s\w\W':,`]*});\s*var additional = (?P<addition>{[\n\s\w\W':,`]*});")
                result_regex = re.search(pattern, result_in_js.text)
                result_info = eval(result_regex.group('result'))
                addition_info = eval(result_regex.group('addition'))
            except Exception as e:
                print("exception in result extracting")
                print(e)
                return None

            result_list = []
            result_list.append("রোলঃ  {}".format(convertBijoyToUnicode(str(addition_info['roll']))))
            result_list.append("নিবন্ধন নংঃ  {}".format(convertBijoyToUnicode(str(addition_info['alid']))))
            result_list.append("নামঃ  {}".format(convertBijoyToUnicode(str(addition_info['name']))))
            result_list.append("পিতার নামঃ  {}".format(convertBijoyToUnicode(str(addition_info['father']))))
            result_list.append("মাদ্রাসাঃ {}".format(convertBijoyToUnicode(str(addition_info['madrasa']))))
            result_list.append("মারকাযঃ  {}".format(convertBijoyToUnicode(str(addition_info['markaj']))))
            result_list.append("জন্ম তারিখঃ {}".format(convertBijoyToUnicode(str(addition_info['birth']))))
            result_list.append("সনঃ {}".format(convertBijoyToUnicode(str(addition_info['year']))))
            result_list.append("মারহালাঃ {}".format(convertBijoyToUnicode(str(addition_info['marhala']))))

            for k, v in result_info.items():
                result_list.append("{} : {}".format(convertBijoyToUnicode(k), convertBijoyToUnicode(v)))

            result_list.append(
                "মোট প্রাপ্ত নম্বরঃ  {}".format(convertBijoyToUnicode(str(addition_info['total-mark']))))
            result_list.append("প্রাপ্ত বিভাগঃ  {}".format(convertBijoyToUnicode(str(addition_info['grade']))))
            result_list.append("মেধা স্থানঃ {}".format(convertBijoyToUnicode(str(addition_info['position']))))

            result_string_for_save_in_db = '\n'.join(result_list)

            # replace a broken bangla!
            broken_word = 'জায়ি্যদ'
            correct_word = 'জায়্যিদ'
            result_string = result_string_for_save_in_db.replace(broken_word, correct_word)

            print("roll {} grabbed, using proxy: {}".format(roll, random_proxy))
            random_proxy.accepted = random_proxy.accepted + 1
            random_proxy.save()
            return result_string

        except Exception as e:
            print("exception in get_result_from_befaq_server")
            print(e)


def load_data(start, stop, exam_year, marhala):
    error_count = 0
    for roll in range(start, stop):
        print('roll {} result grabbing'.format(roll))

        try:
            if error_count > 100:
                break

            if Result.objects.filter(student_roll=roll, student_marhala=marhala, exam_year=exam_year).exists():
                continue

            result_string = get_result_from_befaq_server(exam_year, marhala, roll)
            if not result_string:
                continue

            new_result = Result(student_roll=roll, student_marhala=marhala, exam_year=exam_year)
            new_result.result = result_string
            new_result.save()
            print('result for roll {} added to database'.format(roll))

        except Exception as e:
            error_count += 1
            print("exception in load_data")
            print(e)

    if error_count > 100:
        print('data loading aborted due to more then 100 error')


@login_required
def grab_proxies(request):
    try:
        for i in range(100):
            res = requests.get("http://pubproxy.com/api/proxy", headers=headers)
            print(res.text)
            res = json.loads(res.text)
            proto = res['data'][0]['type']
            ip_port = res['data'][0]['ipPort']

            if proto not in ["http", "https"]:
                continue

            http_proxy = "{}://{}".format(proto, ip_port)
            p, c = Proxy.objects.get_or_create(ip=http_proxy)
            print("proxy {}, created: {}".format(p.ip, c))

    except Exception as e:
        print(e)

    return HttpResponse("Grabbed")


@login_required
def grab_results(request):
    if request.method == 'POST':
        print(request.POST)

        exam_year = request.POST.get('exam_year')
        marhala = request.POST.get('marhala')

        start = int(request.POST.get('start'))
        stop = int(request.POST.get('stop'))

        if exam_year and marhala:
            executor.submit(load_data, start, stop, exam_year, marhala)
        else:
            print('exam_year or marhala not provided')

    context = {
        'marhala': dict(MARHALA),
        'exam_years': dict(EXAM_YEARS),
    }

    return render(request, 'result/grab_results.html', context)


def get_result(request, exam_year, marhala, roll):
    result = Result.objects.filter(exam_year=exam_year, student_marhala=marhala, student_roll=roll)
    if result.exists():
        response = {
            "status" : True,
            "message" : "grabbed from database",
            "data" : result.first().as_json()
        }
        return HttpResponse(json.dumps(response, ensure_ascii=False), content_type="application/json")
    else:
        try:
            result_string = get_result_from_befaq_server(exam_year, marhala, roll)
            if result_string:
                new_result = Result(exam_year=exam_year, student_marhala=marhala, student_roll=roll)
                new_result.result = result_string
                new_result.save()

                response = {
                    "status": True,
                    "message": "grabbed from befaq server",
                    "data": new_result.as_json()
                }
                return HttpResponse(json.dumps(response, ensure_ascii=False), content_type="application/json")

        except Exception as e:
            print("exception in get result")
            print(e)

        response = {
            "status" : False,
            "message" : "no result found"
        }
        return JsonResponse(response, status=404)


def index(request):
    return HttpResponse("Its Working! ")
