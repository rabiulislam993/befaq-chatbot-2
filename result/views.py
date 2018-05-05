import re
import json
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


def load_data(start, stop, exam_year, marhala):
    all_proxies = Proxy.objects.all()
    # reandom_proxy = random.choice(all_proxies)
    proxy_dict = None
    print(proxy_dict)

    error_count = 0

    for roll in range(start, stop):
        print('roll {} result grabbing'.format(roll))

        try:
            if error_count > 100:
                break

            if Result.objects.filter(student_roll=roll, student_marhala=marhala, exam_year=exam_year).exists():
                continue

            result_url = "http://wifaqresult.com/result/{year}/{marhala}/{roll}". \
                format(year=exam_year, marhala=marhala, roll=roll)

            r = requests.get(result_url, headers=headers, proxies=proxy_dict)
            print('status code {}'.format(r.status_code))
            while r.status_code != 200:
                print('returned status code: {}'.format(r.status_code))
                if r.status_code == 429:
                    reandom_proxy = random.choice(all_proxies)
                    proxy_dict = {"http": reandom_proxy.ip}
                else:
                    proxy_dict = None

                r = requests.get(result_url, headers=headers, proxies=proxy_dict)
                print('new status code {}'.format(r.status_code))

            r.encoding = 'utf-8'

            result = bs(r.text, "html.parser")

            with open('test.txt', 'w') as f:
                f.writelines(str(r.text))
                f.close()

            result_in_js = result.find_all('script')[-1]

            pattern = re.compile(
                "var result = (?P<result>{[\n\s\w\W':,`]*});\s*var additional = (?P<addition>{[\n\s\w\W':,`]*});")
            result_regex = re.search(pattern, result_in_js.text)
            result_info = eval(result_regex.group('result'))
            addition_info = eval(result_regex.group('addition'))

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
            print(result_string_for_save_in_db)

            # replace a broken bangla!
            broken_word = 'জায়ি্যদ'
            correct_word = 'জায়্যিদ'
            result_string_for_save_in_db = result_string_for_save_in_db.replace(broken_word, correct_word)

            print('===================================================')

            print('inserting result to database...')

            new_result = Result(student_roll=roll, student_marhala=marhala, exam_year=exam_year)
            new_result.result = result_string_for_save_in_db
            new_result.save()
            print(new_result)

            print('roll {} added to database'.format(roll))

        except Exception as e:
            error_count += 1
            print(e)
            global proxy_dict
            reandom_proxy = random.choice(all_proxies)
            proxy_dict = {"http": reandom_proxy.ip}
            # raise

    if error_count > 100:
        print('data loading aborted due to more then 100 error')


@login_required
def grab_proxies(request):
    try:
        for i in range(100):
            res = requests.get("http://pubproxy.com/api/proxy", headers=headers)
            res = json.loads(res.text)
            proto = res['data'][0]['type']
            if proto != 'http' or proto != 'https':
                continue
            ip_port = res['data'][0]['ipPort']

            http_proxy = "{}://{}".format(proto, ip_port)
            p, c = Proxy.objects.get_or_create(ip=http_proxy)
            print("proxy {}, created: {}".format(p.ip, c))

    except Exception as e:
        print(e)

    return HttpResponse("Grabed")


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
            # load_data(start, stop, exam_year=exam_year, marhala=marhala)
        else:
            print('exam_year or marhala not provided')

    context = {
        'marhala': dict(MARHALA),
        'exam_years': dict(EXAM_YEARS),
    }

    return render(request, 'result/grab_results.html', context)


def get_result(request):
    return JsonResponse({'hello': 'there'})