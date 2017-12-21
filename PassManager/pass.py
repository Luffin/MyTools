#!/usr/bin/env python
# coding=utf8

from string import digits, lowercase, uppercase
from hashlib import md5
from random import seed, sample
from getpass import getpass
from os import system
from subprocess import mswindows


Dictionary = digits + lowercase + uppercase + '_/+-'


def usage():
    print u'这是我自己的密码管理工具\n作为一些地方的密码的管理与生成工具\n'
    print u'跟着程序的提示'
    print u'输入常用的密码或者自己容易记住的密码作为基础密码'
    print u'再输入一个与生成密码有关的信息作为代号'
    print u'随后程序会生成一个由0-9、a-z、A-Z以及其他符号组成的密码\n\n'


def genPass(base_pass, symbol, length=32):
    md5_hash = md5(base_pass + symbol).hexdigest()[:16]
    num = int(''.join([x for x in md5_hash if x in digits]))
    seed(num)
    final_pass = ''.join(sample(Dictionary, length))
    return final_pass


def main():
    usage()
    msg1 = u'请输入基础密码'
    msg2 = u'请输入密码代号'
    msg3 = u'不显示密码将密码直接传入剪切板?(y/n)或直接回车：'
    msg4 = u'输入密码长度，直接回车默认32位：'

    print msg1
    base_pass = getpass()
    while not base_pass:
        print u'[!] 输入错误！还没有输入基础密码，请重新输入'
        print msg1
        base_pass = getpass()

    print msg2
    symbol = getpass()
    while not symbol:
        print u'[!] 输入错误！还没有输入密码代号，请重新输入'
        print msg2
        symbol = getpass()

    print msg4
    length = raw_input()
    if not length:
        length = 32
    else:
        length = int(length)

    final_pass = genPass(base_pass, symbol, length)

    print msg3
    display_pass = raw_input()
    while display_pass not in ('y', 'Y', 'n', 'N', ''):
        print u'[!]输入错误！请输入(Y/N)或(y/n)或直接回车'
        print msg3
        display_pass = raw_input()
    if display_pass in ('y', 'Y', ''):
        if mswindows:
            cmd = 'echo %s| clip' % final_pass.strip()
        else:
            cmd = 'echo "%s" | tr -d "\n" | pbcopy' % final_pass.strip()
        system(cmd)
    elif display_pass in ('n', 'N'):
        print u'\n[+] 密码已生成：' + final_pass


if __name__ == '__main__':
    main()
