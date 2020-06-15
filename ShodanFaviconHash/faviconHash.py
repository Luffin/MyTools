#coding=utf8
import sys
import requests
import mmh3
from bs4 import BeautifulSoup


def getURL(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('link')
    try:
        for l in links:
            if 'favicon.ico' in l.get('href'):
                return l.get('href')
    except Exception:
        return False


if len(sys.argv) < 2:
    print 'Usage:\n\tpython %s url' % sys.argv[0]
    sys.exit(0)

url = sys.argv[1]
fav_url = getURL(requests.get(url, verify=False).content)
if not fav_url:
    fav_url = '/favicon.ico'
favicon = requests.get(url + fav_url, verify=False).content
hash = mmh3.hash(favicon.encode('base64'))
print '[+] %s/favicon.ico ==> %s' % (url, hash)
