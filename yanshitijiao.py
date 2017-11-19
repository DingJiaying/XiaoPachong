#利用有道词典来翻译文本
import urllib.request
#延迟提交
import urllib.parse
import json
import time

while True:
    content = input("请输入需要翻译的内容(输入“q!”退出程序)：")
    if content == 'q! ':
        break
    

    url = " http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom="

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

    data = {
        'i':content,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'1510904693767',
        'sign':'dd35e68bf022507bfd62436033461755',
        'doctype':'json',  #用字符串的格式把python存储起来
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_CLICKBUTTION',
        'typoResult':'false'}

    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')

    target = json.loads(html)
    print("翻译的结果是:%s" % (target['translateResult'][0][0]['tgt']))

    time.sleep(5) #每次休息5秒
