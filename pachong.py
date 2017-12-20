import requests


def getUrl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'connect error!'

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getUrl(url))