#coding=utf8
import sys
import requests
import mmh3
import urlparse
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getURL(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('link')
    try:
        for l in links:
            if '.ico' in l.get('href'):
                return l.get('href')
    except Exception:
        return False


def urlParser(url):
    url_parse_tuple = urlparse.urlparse(url)
    filename = ''
    path = ''
    if '.' in url_parse_tuple[2].split('/')[-1]:
        print url_parse_tuple[2]
        filename = url_parse_tuple[2].split('/')[-1]
        path = url_parse_tuple[2].split('/')
    return url_parse_tuple[0], url_parse_tuple[1], path, filename


if len(sys.argv) < 2:
    print 'Usage:\n\tpython %s url' % sys.argv[0]
    sys.exit(0)

url = sys.argv[1]
scheme, netloc, path, filename = urlParser(url)

fav_url = getURL(requests.get(url, verify=False).content)

if not fav_url:
    fav_url = '/favicon.ico'
    final_url = urlparse.urlunsplit((scheme, netloc, path + fav_url, '', ''))
else:
    if fav_url.startswith('/'):
        final_url = urlparse.urlunsplit((scheme, netloc, fav_url, '', ''))
    else:
        final_url = urlparse.urlunsplit((scheme, netloc, path + fav_url, '', ''))

print '[+] URL ==> %s' % (final_url)
favicon = requests.get(final_url, verify=False).content
hash = mmh3.hash(favicon.encode('base64'))
print '[+] %s ==> %s' % (final_url, hash)
