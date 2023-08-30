from django.shortcuts import render

# Create your views here.
import PyPDF2

# PDF 파일 열기
with open('test/test.pdf', 'rb') as pdf_file:
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


