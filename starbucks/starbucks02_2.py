# starbucks02.py 의 방법 2

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


def getStore(sido_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    res = requests.post(url, data={
                                    "ins_lat":"37.6113443",
                                    "ins_lng":"127.1580072",
                                    "p_sido_cd":sido_code,
                                    "p_gugun_cd":"",
                                    "in_biz_cd":"",
                                    "set_date":"",
                                    "iend":"1000"
                                    })
    store_list = res.json()['list']
    # s_name, tel, doro_address, lat, lot
    # {'list' : [{}, {}]}
    lst=[]
    for store in store_list:
        d = {}
        d['s_name'] = store['s_name']
        d['tel'] = store['tel']
        d['doro_address'] = store['doro_address']
        d['lat'] = store['lat']
        d['lot'] = store['lot']
        lst.append(d)
    return lst

if __name__ == '__main__':
    lst = []
    for sc in getSiDo():
        lst.extend(getStore(sc))
    print(len(lst))
    print(570 + 377 + 59 + 71 + 59 + 128 + 29 + 66 + 28 + 66 + 48 + 25 + 29 + 36 + 26 + 22 + 11)