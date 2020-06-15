import requests
import mmh3
import sys

if len(sys.argv) < 2:
    print 'Usage:\n\tpython %s url' % sys.argv[0]
    sys.exit(0)

url = sys.argv[1].rstrip('/')
favicon = requests.get(url + '/favicon.ico').content
hash = mmh3.hash(favicon.encode('base64'))
print '[+] %s/favicon.ico ==> %s' % (url, hash)
