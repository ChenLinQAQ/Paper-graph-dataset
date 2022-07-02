# coding: utf-8
import io
import requests


def download_pdf(save_path, pdf_name, pdf_url):
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }
    response = requests.get(pdf_url, headers=send_headers)
    bytes_io = io.BytesIO(response.content)
    print(save_path + str(pdf_name) + ".pdf")
    with open(save_path + str(pdf_name) + ".pdf", mode='wb') as f:
        f.write(bytes_io.getvalue())
        print(f'{pdf_name}.PDF,下载成功')


if __name__ == '__main__':
    with open('./url/url-pdf.txt', encoding='utf-8') as fp:
        urls = fp.read()
    urls = urls.split('\n')
    print(len(urls) - 1)
    urls = urls[0: len(urls) - 178]
    print(urls)
    count = 1
    for url in urls:
        print(url)
        save_path = './pdf_set/'
        pdf_name = count
        pdf_url = url
        download_pdf(save_path, pdf_name, pdf_url)
        count += 1
