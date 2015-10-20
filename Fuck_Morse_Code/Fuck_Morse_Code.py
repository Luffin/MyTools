# coding=utf8

__auther__ = 'Luffin'

import sys
import getopt
from os import system

# 全局变量==>密码表
global MAP
global re_MAP

# 摩斯电码映射表
MAP = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', '--.':'g', '....':'h', '..':'i',
		'.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r',\
		'...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z', '.----':'1',\
		'..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7','---..':'8', '----.':'9',\
		'-----':'0', '.-.-.-':'.', '..--..':'?', '-.-.--':'!', '-.--.':'(', '.--.-.':'@', '---...':':',\
		'-...-':'=', '-....-':'-', '-.--.-':')', '.-.-.':'+','--..--':',', '.----.':"'", '..--.-':'_', \
		'...-..-':'$', '-.-.-.':';', '-..-.':'/', '.-..-.':'"', '.-...':'&'}
re_MAP = {v:k for k, v in MAP.iteritems()}

# 帮助说明
def usage():
	print '*'*35+'Fuck_Morse_Code'+'*'*35
	print '这是一个用于翻译摩斯码的脚本'
	print 
	print 'Usage: Fuck_Morse_Code.py -s string'
	print '-h,--help		-帮助说明'
	print '-c,--cmd		-进入交互式界面，一个个翻译摩斯密码(具体看cmd下的命令)'
	print '-s,			-后接摩斯密码，将之翻译成字符串'
	print '-r,			-后接字符串，将之翻译成摩斯密码'
	print 
	cmd_help()
	print 
	print 'Example:'
	print 'Fuck_Morse_Code.py -s ".-. .-- - --- ...."'
	print 'Fuck_Morse_Code.py -r "hello world"'
	print 'Fuck_Morse_Code.py -c'
	sys.exit(0)

# 命令解析
def main():
	# 全局变量
	global cmd
	global ciphertext
	global plaintext

	if not sys.argv[1:]:
		usage()

	# 读取并解析命令
	try:
		opts,args = getopt.getopt(sys.argv[1:], 'chs:r:', ['cmd', 'help'])
	except getopt.GetoptError as e:
		print str(e)
		usage()
	# print opts
	# print args
	# 根据参数选择功能
	for o,a in opts:
		if o in ('-c', '--cmd'):
			cmd()
		elif o in ('-s'):
			Encrypto(a)
		elif o in ('-r'):
			Decrypto(a)
		elif o in ('-h', '--help'):
			usage()

# 解密摩斯电码为明文
def Encrypto(cryptotext):
	global MAP
	
	split_cryptotext = cryptotext.split(' ')
	plaintext = ''
	for c in split_cryptotext:
		try:
			m = MAP[c]
		except KeyError:
			m = c + ' '
		finally:
			plaintext += m
	print '[+] Plaintext ==> %s' % plaintext

# 加密明文成摩斯电码的密文
def Decrypto(plaintext):
	global re_MAP
	
	cryptotext = ''
	for m in plaintext:
		try:
			c = re_MAP[m]
		except KeyError:
			c = m
		finally:
			cryptotext += c + ' '
	print '[+] Cryptotext ==> %s' % cryptotext

# 交互式界面解密摩斯电码
def cmd():
	global MAP
	# 命令提示
	cmd_help()

	text = ''

	# 循环接收用户输入并根据命令进行具体操作
	while True:
		# system('clear')
		input_text = raw_input('>>')
		# 退出命令
		if input_text in ('exit', 'q'):
			print '[+] Good Bye :)'
			sys.exit(0)
		# 打印输出当前明文
		elif input_text == 'print':
			print '[+] Result ==> %s' % text
		# 打印cmd下的命令帮助文档
		elif input_text == 'help':
			cmd_help()
		# 清空命令
		elif input_text == 'cls':
			cmd()
			break
		# 执行“退格”操作
		elif input_text == 'del':
			text = text[ :-1]
			print '[+] Result ==> %s' % text
		else:
			# 根据密文到映射表中查找明文
			if MAP.has_key(input_text):
				text += MAP[input_text]
			else:
				text += input_text
			print '[+] Result ==> %s' % text
# cmd中的命令提示
def cmd_help():
	print 'cmd下的命令:'
	print 'exit,q			结束脚本'
	print 'cls			清空之前的输入，重新开始翻译'
	print 'del			若输入错误，可使用此命令，效果类似键盘的Backspace键'
	print 'help			显示交互界面的帮助信息'
	print 'print			查看当前解密的密文'
	print '若输入的既非以上命令，也不是摩斯电码，则直接输出在屏幕上(可用于输入空格以便于分割单词)'


if __name__ == '__main__':
	main()