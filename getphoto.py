import requests
import os

url = 'http://n.sinaimg.cn/news/w1000h500/20171219/ig4o-fypvuqc8908420.jpg'
root = r'D:/pics/'
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.text)
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
