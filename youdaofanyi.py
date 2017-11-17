#利用有道词典来翻译文本
import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = " http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom="

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

response = urllib.request.urlopen(url,data)

html = response.read().decode('utf-8')

target = json.loads(html)
print("翻译的结果是:%s" % (target['translateResult'][0][0]['tgt']))
