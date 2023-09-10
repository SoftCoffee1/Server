from django.shortcuts import render

# Create your views here.
import PyPDF2




import requests
from bs4 import BeautifulSoup

# 웹 페이지의 URL 지정
# url = 'https://ssl.pstatic.net/imgstock/upload/research/company/1665450381294.pdf'  # PDF 파일이 있는 웹 페이지의 URL로 변경

# 해당 URL에서 웹 페이지 내용 가져오기
# response = requests.get(url)

# HTML 파서로 웹 페이지 내용을 파싱
# soup = BeautifulSoup(response.text, 'html.parser')

# PDF 다운로드 링크 찾기
# pdf_links = soup.find_all('a', href=True, text='Download PDF')

# PDF 다운로드
# for link in pdf_links:
# pdf_url = pdf_links['href']
pdf_response = requests.get("https://ssl.pstatic.net/imgstock/upload/research/company/1665450381294.pdf")
with open('./downloaded.pdf', 'wb') as pdf_file:
    pdf_file.write(pdf_response.content)


# PDF 파일 열기
with open('downloaded.pdf', 'rb') as pdf_file:
    # PdfReader를 사용하여 PDF 파일 읽기
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # 페이지 수 확인
    num_pages = len(pdf_reader.pages)
    print(f'총 페이지 수: {num_pages}')

    # 페이지 별로 텍스트 출력
    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()
        print(f'페이지 {page_number + 1}:\n{page_text}')