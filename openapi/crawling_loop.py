from bs4 import BeautifulSoup
import requests

url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# titles = soup.find_all('span', class_='title')
# print(titles)

# # 내가 한 방법
# title_list = []
# for title in titles:
#     X = title.text.strip()
#     #print(X)
#     title_list.append(X)
# print(title_list)
#
# numbers = soup.find('nav', class_='pagination')
# numbers_2 = numbers.find_all('a')[2:-2]
# lst = []
# for number in numbers_2:
#     lst.append(number.text)
# print(lst)
#
# merged_list = list(zip(lst, title_list))
# print(merged_list)    ===> 이건 한 페이지당 모든 제목을 가져온 게 아닌, 10개의 숫자를 매칭한 것 (착각했음)

# 답
# for title in titles:
#     print(title.text.strip())


paging = soup.find('nav', class_="pagination")
"""
nums = list()
for page in paging:
    if page.text.isdigit():
        nums.append(page.text)

print(nums)
"""
nums = list(filter(None, map(lambda x:x.text if x.text.isdigit() else None, paging)))
# print(nums)

sub_url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage="
for i in nums:
    soup = BeautifulSoup(requests.get(sub_url+i).text, 'html.parser')
    titles = soup.select('span[class=title]')
    for title in titles:
        print(title.text.strip())




