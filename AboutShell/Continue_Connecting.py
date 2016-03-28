import requests
import getopt
import sys

global url,filename,number
url = ''
filename = ''
number = 0

def main():
	global url,filename,number
	if not sys.argv[1:]:
		print '[!] You must input url and filename!'
		sys.exit()
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'u:f:n:', ['url=', 'filename=', 'number='])
	except getopt.GetoptError as e:
		print str(e)
		sys.exit()

	for o,a in opts:
		if o in ('-u', 'url='):
			url = a
		if o in ('-f', 'filename='):
			filename = a
		if o in ('-n', 'number='):
			number = int(a)

	Continue_Fuck(url, filename, number)
	
def Continue_Fuck(url, filename, number):
	if url[-1] == '/':
		URL = url + filename
	else:
		URL = url + '/' + filename

	for n in xrange(number):
		try:
			response = requests.get(URL)
			if response:
				print '[+] Connected!',
		except Exception, e:
			continue
		finally:
			sys.stdout.write('Time round is %d\r' % (n+1))
			sys.stdout.flush()
		

if __name__ == '__main__':
	main()
