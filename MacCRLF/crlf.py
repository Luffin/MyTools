#!/usr/bin/env python
# coding=utf8

import sys

if len(sys.argv) < 2:
    print 'Usage:\n\tpython %s filename {output}' % (sys.argv[0])
    sys.exit(0)

in_name = sys.argv[1]
if len(sys.argv) < 3:
    out_name = sys.argv[1]
else:
    out_name = sys.argv[2]

with open(in_name, 'rb') as input:
    content = input.read().replace('\x0a', '\x0d\x0a')

with open(out_name, 'wb') as output:
    output.write(content)
