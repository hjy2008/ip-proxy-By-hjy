# ip代理池制作

## 一.依赖库

### requests

### parsel



## 二.过程

### 1.ip代理网页

在网上随便找一个[代理ip](https://free.kuaidaili.com/free/inha/1/)，如图

![快代理ip](img/1.jpg)

### 2.网站分析

通过不断切换页面，观察网址（又叫 url/uri）的变化

![](img/2.jpg)

![](img/3.jpg)

可以看出变化的部分是 "{}" 部分 `https://free.kuaidaili.com/free/inha/{}/`

以此，可以迭代出全部页面。

代码块：

```python
# range(a, b)：从a开始，在b前停止
for i in range(1, 4707):
    # str 进行格式转换
    url = f'https://free.kuaidaili.com/free/inha/{str(i)}/'
    # 加入UA防止反爬
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    response = requests.get(url, headers = headers).text
```

