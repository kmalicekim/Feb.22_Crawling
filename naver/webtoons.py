# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'
resp = requests.get(url)   # 해당 url을 get 방식으로 요청 (post방식으로 request하려면 requests.post(url))
# print(resp)   # https://comic.naver.com/webtoon/weekdayList?week=wed
# print(resp.text)  # 문자열로 나옴

soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

webtoons = soup.find('ul', {'class': 'img_list'})
# print(webtoons)
dl_list = webtoons.select('dl')

lst = list()
for dl in dl_list:
    title = dl.find('a')['title']   # 해당 태그 a 의 속성값 title
    star = dl.find('strong').text

    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star

    lst.append(tmp)

# print(lst) ---> 한 리스트 안에 여러 딕셔너리가 담겨있는 형태

res = dict()
res['webtoon'] = lst
# print(res)  ---> json 형태의 문자열로 되어 있음
res_json = json.dumps(res, ensure_ascii=False)   # default : ascii 코드로 나옴
print(res_json)

with open('webtoons.json', 'w', encoding='utf-8') as f:
    f.write(res_json)