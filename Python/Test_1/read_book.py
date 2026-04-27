#!/usr/bin/env python
# coding=utf-8
import re

import requests
from lxml import etree
import sys


def novels_page():
    global novels_name, file_name
    """小说章页数"""
    start_url = 'https://www.laiyexs.com/modules/article/search.php'
    data = {
        'searchkey': novels_name.encode('gbk'),
        'submit': novels_name.encode('gbk')
    }
    response = requests.post(start_url, headers=headers, data=data)
    response = response.text.encode("latin1").decode("GBK")
    html = etree.HTML(response)
    title = html.xpath('//div[@class="pic scal bookShadow oh"]//a/@title')
    href = html.xpath('//div[@class="pic scal bookShadow oh"]//a/@href')
    if title:
        novels_name = input('关于“{}”搜索完成请在{}里面选择哪一本|输入对应的名字：'.format(novels_name, title))
        file_name = '{}.txt'.format(novels_name)
        data = {
            'searchkey': novels_name.encode('gbk'),
            'submit': novels_name.encode('gbk')
        }
        response = requests.post(start_url, headers=headers, data=data)
        response = response.text.encode("latin1").decode("GBK")
        html = etree.HTML(response)
        title = html.xpath('//div[@class="pic scal bookShadow oh"]//a/@title')
        href = html.xpath('//div[@class="pic scal bookShadow oh"]//a/@href')
    if not title:
        title = html.xpath('//div[@class="xxcont"]//a/@title')
        href = html.xpath('//div[@class="xxcont"]//a/@href')
    if not title:
        print('您输入的小说名字暂时不在本网站内')
        sys.exit()
    novels_url = 'https://www.laiyexs.com'
    for h in range(len(title)):
        if novels_name == title[h]:
            novels_url = novels_url + re.sub('html', 'mulu', href[h], count=1)
    response = requests.get(novels_url, headers=headers)
    response = response.text.encode("latin1").decode("GBK")
    html = etree.HTML(response)
    pages = html.xpath('//span[@class="page-num"]/text()')[0]
    pages = int(re.compile(r'/ (\d+)').search(pages).group(1))
    num = re.compile('mulu/(\d+)\.html').search(novels_url).group(1)
    return novels_url, pages, num


def novels_details(novels_url, num, i):
    """小说详情名称，路由"""
    details_pages_url = novels_url.replace(num + '.html', num + '_{}.html'.format(i))
    response = requests.get(details_pages_url, headers=headers)
    response = response.text.encode("latin1").decode("GBK")
    html = etree.HTML(response)
    details_title = html.xpath('//div[@id="section-list"]//a/@title')
    details_url = html.xpath('//div[@id="section-list"]//a/@href')
    return details_title, details_url


def novels_details_page(d_url):
    """小说详情页数"""
    splicing_url = 'https://www.laiyexs.com' + d_url
    response = requests.get(splicing_url, headers=headers)
    response = response.text.encode("latin1").decode("GBK")
    html = etree.HTML(response)
    page_title = html.xpath('//div[@class="article-title mt10"]/h1/text()')[0]
    page = int(re.search('/(\d)', page_title).group(1))
    return splicing_url, html, page


def novels_file_w(d_title, splicing_url, html, page):
    """小说数据保存"""
    for p in range(1, page + 1):
        if p == 1:
            text = html.xpath('//div[@id="dx"]//p/text()')
            with open(file_name, 'a', encoding='utf-8') as f:
                print('-----------正在爬取{}-----------'.format(d_title))
                f.write(d_title + '\n')
                for t in text:
                    content = t
                    f.write(content + '\n')
        else:
            num = re.compile('/(\d+?)(\.html)').search(splicing_url)
            details_page_url = splicing_url.replace(num.group(1) + num.group(2), num.group(1) + '_{}.html'.format(p))
            print(details_page_url)
            response = requests.get(details_page_url, headers=headers)
            response = response.text.encode("latin1").decode("GBK")
            html = etree.HTML(response)
            text = html.xpath('//div[@id="dx"]//p/text()')
            with open(file_name, 'a', encoding='utf-8') as f:
                for t in text:
                    if '手机阅读请到' in t:
                        continue
                    content = t
                    f.write(content + '\n')


def novels_start():
    """入口"""
    novels_url, pages, num = novels_page()
    for i in range(1, pages + 1):
        details_title, details_url = novels_details(novels_url, num, i)
        for d in range(len(details_url)):
            d_url = details_url[d]
            d_title = details_title[d]
            splicing_url, html, page = novels_details_page(d_url)
            novels_file_w(d_title, splicing_url, html, page)
    print('爬取完成')


if __name__ == '__main__':
    """https://www.laiyexs.com/"""
    input_name = input('输入想要爬取的小说名字：')
    novels_name = input_name
    file_name = '{}.txt'.format(input_name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    }
    novels_start()
