from bs4 import BeautifulSoup

import requests #http 요청 처리 library

headers={
    "User-Agent": "Dongyang Mirae"
}
#뉴스
webpage=requests.get("https://www.news1.kr/articles/5047308", headers=headers)
print(webpage)
soup=BeautifulSoup(webpage.content,"html.parser")
print(soup) #dic_area

news=soup.select_one("#articles_detail").get_text().strip()
print(news)