import re
import sys

if len(sys.argv) < 2:
    print 'Usage:\n\t%s filename outputname'
    sys.exit(0)

outputname = 'result.txt'
inputname = sys.argv[1]

if len(sys.argv) > 2:
    outputname = sys.argv[2]
else:
    outputname = inputname

with open(inputname, 'r') as f:
    content = f.read()

m = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content)
res = {}.fromkeys(m).keys()

with open(outputname, 'w') as f:
    for ip in res:
        f.write(ip + '\n')
