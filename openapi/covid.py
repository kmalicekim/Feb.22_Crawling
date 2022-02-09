from xml.etree import ElementTree
import requests
import re

service_key='VXBYQ69L5Fwe5N6ROU%2BQDFRw2QT7VAQq2iW9WUSFjTxT5tCatN27CjwGwFKDLtqMhSaBV2BfjIAhytbw2lcWmg%3D%3D'
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'

# print(url)

resp = requests.get(url)
tree = ElementTree.fromstring(resp.text)   # ElementTree를 사용하여 xml 문자열을 xml ParseTree로 만들겠다
print(tree)   # <Element 'response' at 0x7fdd2d4f70e0> ---> ParseTree가 되었으니 객체가 되었음 (응답된 객체)

for item in tree[1][0]:   # tree[1] = body (tree[0] 은 header) / tree[1][0] = <items>
    if item.find('gubun').text == '합계':
        stdDay = re.sub(r'(\D)+','', item.find('stdDay').text)   # 2022020900  --- 정규표현식 사용
        stdDay = stdDay[2:4] + "/" + stdDay[4:6] + "/" + stdDay[6:8]
        incDec = item.find('incDec').text
        localOccCnt = item.find('localOccCnt').text
        overFlowCnt = item.find('overFlowCnt').text
        print(f'[{stdDay}]\n일일합계:{incDec}\n국내발생:{localOccCnt}\n해외발생:{overFlowCnt}')





