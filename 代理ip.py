import re

import parsel
import requests

list_ = set(())


def getIp():
    global list_
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
        print(list_)
        with open('./ip.txt', 'w') as f:
            for j in list_:
                print(j)
                f.writelines(j)


def check(ip, port):
    for i in range(0, len(ip)):
        proxies = {
            'https': f'http://{ip[i]}:{port[i]}/',
            'http': f'http://{ip[i]}:{port[i]}/'
        }
        # print(proxies)

        try:
            response = re.findall(r'<span class="c-red">(.*?)</span>',
                                  requests.get('http://mip.chinaz.com', proxies = proxies, timeout = 1.5).text)
            if 'seccess' in response:

                with open('ip.txt', 'r') as r:
                    for line in r.readlines():
                        list_.add(line)
                list_.add(str(proxies) + '\n')
                # print(list_)
                for abc in list_:
                    # print(abc)
                    pass
                print('Success!')
            elif len(response) == 2:
                with open('ip.txt', 'r') as r:
                    for line in r.readlines():
                        list_.add(line)
                list_.add(str(proxies) + '\n')
                # print(list_)
                for abc in list_:
                    # print(abc)
                    pass
                print(response)
        except:
            pass


getIp()
