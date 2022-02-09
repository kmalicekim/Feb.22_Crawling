from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.naver#')
# print(resp)  # <http.client.HTTPResponse object at 0x7fc01c13b250>
soup = BeautifulSoup(resp, 'html.parser')
# BeautifulSoup: Python library for pulling data out of HTML and XML files
# html.parser 를 이용하여 html의 parse tree를 만들어줌
# print(type(soup)) # <class 'bs4.BeautifulSoup'> ---> 현재 soup은 beautifulsoup이라는 객체 형태임

movies = soup.find_all('dl', class_='lst_dsc')  # css를 이용하여 가져오기 (현재 가져오고 싶은 건 제목과 별점)
# print(movies)
# print(movies[0])
for movie in movies:
    # 제목
    title = movie.find('a').get_text()    # a태그 안에 있는 텍스트 가져올 때 : .string 이나 .text 써도 됨 (.get_text() 함수도)

    # 별점
    star = movie.find('span', class_='num').text
    print(f'{title} [{star}]')

