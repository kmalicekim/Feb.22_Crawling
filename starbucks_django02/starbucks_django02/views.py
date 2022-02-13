from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

def getSiDo(request):
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url)
    sido_list = resp.json()['list']

    sido_code = list(map(lambda x:x['sido_cd'], sido_list))
    sido_nm = list(map(lambda x:x['sido_nm'], sido_list))
    sido_dict = dict(zip(sido_code, sido_nm))

    return JsonResponse(sido_dict)

def getGuGun(request):
    sido_code = request.GET['sido_code']
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={'sido_cd':sido_code})

    gugun_list = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x:x['gugun_cd'], gugun_list)),
                          list(map(lambda x:x['gugun_nm'], gugun_list))))

    return JsonResponse(gugun_dict)

def getStore(request):
    code = request.GET['code']
    sido_code = code if code == '17' else ''   # 17번일 때는 코드로 넘어가고, 그 외에는 빈 칸으로 넘어감
    gugun_code = '' if code == '17' else code  # 17번일 때는 빈칸으로, 그 외에는 코드로 넘어감

    url = "https://www.starbucks.co.kr/store/getStore.do"     # sources 의 588번째 줄
    resp = requests.post(url, data={'ins_lat': '37.56682',    # 해당 data는 필수적으로 들어가야 되는 것들만 추려낸 것
                                    'ins_lng': '126.97865',
                                    'p_sido_cd': sido_code,
                                    'p_gugun_cd': gugun_code,
                                    'in_biz_cd': '',
                                    'set_date':''})
    store_list = resp.json()['list']
    # s_name, tel, doro_address, lat, lot
    result_list = list()
    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        result_list.append(store_dict)

    result_dict = dict()
    result_dict['store_list'] = result_list
    # print(result_dict)

    return JsonResponse(result_dict)
