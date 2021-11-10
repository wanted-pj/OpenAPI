import requests
import xml.etree.ElementTree as ET
from openpyxl import Workbook
 
# 전국 학과 수
TOTAL_COUNT = 304
 
# 커리어넷 대학정보 URL
# 커리어넷 API를 신청해서 URL 생성하기
URL = 'https://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=f36cd36f04a2ea97e8115aebb3884ec8&svcType=api&svcCode=MAJOR&contentType=xml&gubun=univ_list&univSe=univ&perPage=304'
 
# API 요청하기
response = requests.get(URL) 
status = response.status_code 
text = response.text        # XML 형태
root = ET.fromstring(response.text)
 
print(text)
 
"""
<dataSearch>
<content>
<lClass>교육계열</lClass>
<facilName>가정교육과,실과교육과(심화전공)</facilName>
<majorSeq>10006</majorSeq>
<mClass>가정교육과</mClass>
<totalCount>304</totalCount>
</content>
<content>
<lClass>의약계열</lClass>
<facilName>간호과학과,간호과학부,간호과학전공,간호대학,간호복지학부,간호전공,간호학과,간호학과(4년제),간호학과(야간),간호학과(특별과정),간호학부,간호학부 간호학과,간호학부(간호학전공),간호학전공,글로벌건강간호학전공</facilName>
<majorSeq>10</majorSeq>
<mClass>간호학과</mClass>
<totalCount>304</totalCount>
</content>
...
...
"""
 
# root[i][0].text -> <lClass>       #계열
# root[i][1].text -> <facilName>   # 학과상세이름
# root[i][2].text -> <majorSeq>       
# root[i][3].text -> <mClass>             # 학과이름
# root[i][4].text -> <totalCount>      # 총학과수

 
 
# OpenPyXL 이용해서 전국 대학정보 엑셀에 담기 위한 초기 작업
ABC = ["A1"]
columns = ["major"]
 
# 엑셀파일 쓰기
write_wb = Workbook()
 
# Sheet1에 입력
write_ws = write_wb.active
 
# Head Column 만들기
for (alphabet, col) in zip(ABC, columns): 
  write_ws[alphabet] = col
 
#행 단위로 추가
for i in range(TOTAL_COUNT):
  write_ws.append([root[i][3].text # 학과이름<mClass>
                 ]) 
 
# 파일 저장하기
write_wb.save("major_Info.csv")
