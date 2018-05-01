import requests
from bs4 import BeautifulSoup as bs
from pyjsparser import PyJsParser

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import EXAM_YEARS, MARHALA

js_parser = PyJsParser()


@login_required
def grab_results(request):
    # result_url = http://wifaqresult.com/result/<year>/<marhala_id>/<roll>
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    if request.method == 'POST':
        print(request.POST)
        exam_year = request.POST.get('exam_year')
        marhala = request.POST.get('marhala')

        start = int(request.POST.get('start')) if request.POST.get('start') else 1
        stop = int(request.POST.get('stop')) if request.POST.get('stop') else 100000

        if exam_year and marhala:
            error_count = 0
            for roll in range(1, 2):
                if error_count > 5: break
                try:
                    result_url = "http://wifaqresult.com/result/{year}/{marhala}/{roll}".\
                                    format(year=exam_year, marhala=marhala, roll=roll)

                    # r = requests.get("http://wifaqresult.com/result/2046/1/1")
                    r = requests.get(result_url, headers=headers)
                    r.encoding = 'utf-8'

                    result = bs(r.text)
                    result_in_js = result.find_all('script')[-1]


                    start_first = 359
                    end_first = 737

                    start_second = 738
                    end_second = 1361

                    js_result_first = result_in_js.text[start_first: end_first]
                    js_result_second = result_in_js.text[start_second: end_second]


                    result_dict = {}
                    first_parsed_data = js_parser.parse(js_result_first)
                    prop = first_parsed_data['body'][0]['declarations'][0]['init']['properties']
                    for i in prop:
                        result_dict[i['key']['value']] = i['value']['value']

                    info_dict = {}
                    second_parsed_data = js_parser.parse(js_result_second)
                    prop = second_parsed_data['body'][0]['declarations'][0]['init']['properties']
                    for i in prop:
                        info_dict[i['key']['value']] = i['value']['value']


                    print(result_dict)
                    print('..........................')
                    print(info_dict)

                    # result = beautify(r)
                    
                    print('roll {} added to database'.format(roll))

                except Exception as e:
                    error_count +=1
                    print(e)
                    continue
            if error_count > 4:
                print( "data loading aborted due to 5 errors !")
            else:
                print("Data loaded succesfully")
        else:
            print('exam_year or marhala not provided')

    context = {
        'marhala': dict(MARHALA),
        'exam_years': dict(EXAM_YEARS),
    }

    return render(request, 'result/grab_results.html', context)


def get_result(request):
    return JsonResponse({'hello': 'there'})