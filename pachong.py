import requests


def getUrl(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'connect error!'

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getUrl(url))