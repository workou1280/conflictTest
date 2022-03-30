import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.kw.ac.kr/ko/life/notice.jsp",headers = {'user-agent': 'my-app/0.0.1'})
print(type(res))
soup = BeautifulSoup(res.content, 'html.parser',from_encoding='utf-8')
soup = soup.find_all('div', {"class":"board-text"})
f = open('bulletin.txt','w')
for link in soup:
    f.write(str(link))
f.close