# coding:utf-8
import requests
import cloudscraper
from bs4 import BeautifulSoup


# 模拟浏览器请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
}


def get_html_doc(page):
    url = f'https://www.nature.com/nature/research-articles?searchType=journalSearch&sort=PubDate&page={page}'
    print(url)
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url=url)
    # print(response.encoding)
    # with open('./test.html', 'w', encoding=response.encoding) as fp:
    #     fp.write(response.text)
    return response.text.encode(response.encoding)


if __name__ == '__main__':
    prefix = 'https://www.nature.com'
    suffix = '_reference.pdf'
    total_nums = 10
    i = 1
    url_abstract = ''
    while i < total_nums:
        html_doc = get_html_doc(i)
        soup = BeautifulSoup(html_doc, 'html.parser')
        for link in soup.find_all(name='a', attrs={'class': 'c-card__link u-link-inherit'}):
            url_abstract += (prefix + link.get('href') + suffix + '\n')
        i += 1
    print(url_abstract)
    with open('./url/url-pdf.txt', 'w', encoding='utf-8') as fp:
        fp.write(url_abstract)

