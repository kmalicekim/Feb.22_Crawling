from django.shortcuts import render
from django.http import JsonResponse
from . import starbucks02


def index(request):
    return render(request, 'index.html')

def starbucks(request):
    list_all = list()

    sido_all = starbucks02.getSiDo()
    for sido in sido_all:
        if sido == '17':
            result = starbucks02.getStore(sido_code=sido)
            # print(result)
            list_all.extend(result)
        else:
            gugun_all = starbucks02.getGuGun(sido)
            for gugun in gugun_all:
                result = starbucks02.getStore(gugun_code=gugun)
                # print(result)
                list_all.extend(result)

    # print(list_all)
    # print(len(list_all))   # 1622

    result_dict = dict()
    result_dict["list"] = list_all

    return JsonResponse(result_dict)   # 딕셔너리를 jsonresponse 하면 장고에서 자동으로 json 형태로 바꾸어 줌
