import re
from pprint import pprint
from time import sleep

import parsel
import requests


def getIp():
    for i in range(1, 4707):
        url = f'https://free.kuaidaili.com/free/inha/{str(i)}/'
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        response = requests.get(url, headers = headers).text
        selector = parsel.Selector(response)
        ip = selector.xpath('//*[@id="list"]/table/tbody/tr/td[@data-title="IP"]/text()').getall()
        port = selector.xpath('//*[@id="list"]/table/tbody/tr/td[@data-title="PORT"]/text()').getall()
        print(ip, port)
        check(ip, port)
        sleep(0.5)


def check(ip, port):
    can = []
    for i in range(0, len(ip)):
        proxies = {
            'https': f'http://{ip[i]}:{port[i]}/',
            'http': f'http://{ip[i]}:{port[i]}/'
        }
        print(proxies)

        try:
            # print(requests.get('http://dev.kdlapi.com/testproxy', proxies = proxies, timeout = 20).text)
            # response = requests.get('http://dev.kdlapi.com/testproxy', proxies = proxies, timeout = 30) \
             #   .text.replace(' ', '').split(':')[-1]
            response = re.findall(r'<span class="c-red">(.*?)</span>', requests.get('http://mip.chinaz.com', proxies = proxies, timeout = 30).text)
            if 'seccess' in response:
                can.append(proxies)
                print('Success!')
            elif len(response) == 2:
                can.append(proxies)
                print(response)
        except requests.exceptions.ProxyError:
            print('pass')
        except requests.exceptions.ReadTimeout:
            print('Error')
        except requests.exceptions.ConnectTimeout:
            print('Error')
    pprint(can)
    with open('./ip.txt', 'a') as f:
        f.write(can)


getIp()
