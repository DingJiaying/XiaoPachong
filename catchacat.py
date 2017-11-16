#捕捉网站上一只猫的图片
import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/625/200")
cat_img = response.read()
with open('cat_625_200.jpg','wb') as f:
    f.write(cat_img)
