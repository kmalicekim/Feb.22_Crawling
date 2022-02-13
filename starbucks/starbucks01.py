# -*- coding:utf-8 -*-

import requests
import json


def getSiDo():
    # __ajaxCall("/store/getSidoList.do", {}, true, "json", "post", (1246번째 줄 참고)
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url)
    # print(resp)    # <Response [200]> --> 응답코드가 200이면 제대로 응답을 받았다는 뜻
    # print(resp.text) # json 형태 문자열임 {"list":[{"seq":0,"sido_cd":"01","sido_nm":"서울","gugun_cd":null, ...}
    # print(resp.json()) # --> json 객체로 만들어줌 (응답받는 데이터를 제이슨 형태로 바꿔줌)  {'list': [{'seq': 0, 'sido_cd': '01', 'sido_nm': '서울', ...} None,..}


    # 내가 한 것
    # A = resp.json()
    # B = A["list"]
    # for c in B:
    #     print(c['sido_cd'], c['sido_nm'])

    sido_list = resp.json()['list']
    sido_code = list(map(lambda x:x['sido_cd'], sido_list))
    sido_nm = list(map(lambda x:x['sido_nm'], sido_list))
    sido_dict = dict(zip(sido_code, sido_nm))
    return sido_dict

def getGuGun(sido_code):
    # __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post",  (1302번째 줄 -1262참고)
    # {gugun_code: gugun_nm, ...} 형태
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url, data={'sido_cd':sido_code})
    # print(resp.json())
    gugun_list = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x:x['gugun_cd'], gugun_list)),
                          list(map(lambda x:x['gugun_nm'], gugun_list))))
    # print(gugun_dict)
    return gugun_dict


def getStore(sido_code='', gugun_code=''):
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

    # print(result_list) # [{'s_name': '역삼이마트', 'tel': '1522-3232', 'doro_address': '서울특별시 강남구 역삼로 310 (역삼동)',..]
    # {'store_list': [{}, {}, {}]
    result_dict = dict()
    result_dict['store_list'] = result_list
    # print(result_dict)

    # json 저장
    result_json = json.dumps(result_dict, ensure_ascii=False)
    with open('starbucks01.json', 'w', encoding='utf-8') as f:    #global 변수 사용하여 json 파일명을 시도구군에 맞춰 저장되게 해보기
        f.write(result_json)

    return result_json


if __name__=='__main__':
    print(getSiDo())
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        getStore(sido_code='17', gugun_code='')
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요 : ')
        print(getStore(gugun_code=gugun))

