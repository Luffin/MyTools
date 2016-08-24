#!/usr/bin/env python
# coding=utf8

import sys

name_file = ''
pass_file = ''

if len(sys.argv) < 3:
    print 'usage: %s username.txt password.txt' % sys.argv[0]
    sys.exit(0)

# 从命令行输入参数
name_file = sys.argv[1]
pass_file = sys.argv[2]

names = open(name_file, 'r').read().split('\n')[:-1]
passwords = open(pass_file, 'r').read().split('\n')[:-1]
names_len = len(names)
pass_len = len(passwords)
total = names_len * pass_len
# 结果文件
res = open('result.txt', 'w')
count = 0
for name in names:
    for password in passwords:
        count += 1
        res.write(('%s:%s' % (name, password)).encode('base64'))
        sys.stdout.write('\r %.2f%s | %d done | %d remain | %d total' % (count/float(total) * 100, '%', count, total - count, total))
        sys.stdout.flush()

res.close()
