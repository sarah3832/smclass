import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"class":"hot_issue"}).find("dl",{"class":"ml0"}).text)
data = soup.find("div",{"class":"hot_issue"}).find("dl",{"class":"ml0"}).text
screens = soup.find("dd",{"class":"mov_area"})

print("제목 : ",soup.find("div",{"class":"hot_issue"}).find("dl",{"class":"ml0"}).text)