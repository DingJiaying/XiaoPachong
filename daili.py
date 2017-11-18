#代理ip
import urllib.request


url = "http://www.whatismyip.com.tw"

proxy_support = urllib.request.ProxyHandler({'http':'61.135.217.7:80'})

opener = urllib.request.build_opener(proxy_support)
opener.addheader = [{'User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
