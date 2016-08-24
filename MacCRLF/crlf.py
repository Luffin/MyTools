#!/usr/bin/env python
# coding=utf8

import sys

if len(sys.argv) < 2:
    print 'Usage:\n\tpython %s filename output' % (sys.argv[0])
    sys.exit(0)

with open(sys.argv[1], 'rb') as input, open(sys.argv[2], 'wb') as output:
    content = input.read().replace('\x0a', '\x0d\x0a')
    output.write(content)

input.close()
output.close()
