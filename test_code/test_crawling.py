#https://finance.naver.com/research/company_list.naver?keyword=&brokerCode=&writeFromDate=&writeToDate=&searchType=itemCode&itemName=%C4%AB%C4%AB%BF%C0&itemCode=035720&x=40&y=33

import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/research/company_list.naver?keyword=&brokerCode=&writeFromDate=&writeToDate=&searchType=itemCode&itemName=%C4%AB%C4%AB%BF%C0&itemCode=035720&x=40&y=33'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    file_tds = soup.find_all('td', class_='file')
    # <a> 태그 선택
    for file_td in file_tds:
        a_tag = file_td.find('a')

        # href 속성 값(링크) 얻기
        pdf_url = a_tag['href']

        print(pdf_url)
        # print(soup)

else : 
    print(response.status_code)