import requests

for i in range(1, 4707):
    url = f'https://free.kuaidaili.com/free/inha/{str(i)}/'
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    response = requests.get(url, headers = headers).text

