import requests
import xml.etree.ElementTree as ET
from openpyxl import Workbook
 
# 전국 대학교 수
TOTAL_COUNT = 440
 
# 커리어넷 대학정보 URL
URL = 'https://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=f36cd36f04a2ea97e8115aebb3884ec8&svcType=api&svcCode=SCHOOL&contentType=xml&gubun=univ_list&perPage=440'
 
# API 요청
response = requests.get(URL) 
status = response.status_code 
text = response.text
root = ET.fromstring(response.text)
 
print(text)
 
"""
<dataSearch>
<content>
<campusName>본교</campusName>
<collegeinfourl/>
<schoolType>전문대학</schoolType>
<link>http://www.ict.ac.kr</link>
<schoolGubun>전문대학</schoolGubun>
<adres/>
<schoolName>ICT폴리텍대학</schoolName>
<region>경기도</region>
<totalCount>440</totalCount>
<estType>사립</estType>
<seq>684.0</seq>
</content>
<content>
<campusName>본교</campusName>
<collegeinfourl/>
<schoolType>일반대학</schoolType>
<link>http://kfu.kdb.co.kr</link>
<schoolGubun>대학(4년제)</schoolGubun>
<adres>서울특별시 영등포구 은행로 14 (여의도동, 산업은행본점)</adres>
<schoolName>KDB금융대학교</schoolName>
<region>서울특별시</region>
<totalCount>440</totalCount>
<estType>사립</estType>
<seq>964.0</seq>
</content>
...
...
"""
 
# root[i][0].text -> <campusName>       # 캠퍼스구분
# root[i][1].text -> <collegeinfourl>   # 대학정보URL
# root[i][2].text -> <schoolType>       # 학교종류
# root[i][3].text -> <link>             # 학교홈페이지링크
# root[i][4].text -> <schoolGubun>      # 학교구분
# root[i][5].text -> <adres>            # 주소
# root[i][6].text -> <schoolName>       # 학교명
# root[i][7].text -> <region>           # 지역
# root[i][9].text -> <estType>          # 설립
 
 
# OpenPyXL 이용해서 전국 대학정보 엑셀에 담기 위한 초기 작업
ABC = ["A1"]
columns = ["school"]
 
# 엑셀파일 쓰기
write_wb = Workbook()
 
# Sheet1에 입력
write_ws = write_wb.active
 
# Head Column 만들기
for (alphabet, col) in zip(ABC, columns): 
  write_ws[alphabet] = col
 
#행 단위로 추가
for i in range(TOTAL_COUNT):
  write_ws.append([
                   root[i][6].text, # <schoolName>       # 학교명
                 ]) 
 
# 파일 저장하기
write_wb.save("school_info.csv")
