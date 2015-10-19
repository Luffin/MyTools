# Fuck_Morse_Code.py
---
这是一个用于翻译摩斯码的脚本

## Usage:

```
-h,--help		-帮助说明
-c,--cmd		-进入交互式界面，一个个翻译摩斯密码(具体看cmd下的命令)
-s,				-后接摩斯密码，将之翻译成字符串
-r,				-后接字符串，将之翻译成摩斯密码

cmd下的命令:
exit,q			结束脚本
cls				清空之前的输入，重新开始翻译
del				若输入错误，可使用此命令，效果类似键盘的Backspace键
help			显示交互界面的帮助信息
print			查看当前解密的密文
若输入的既非以上命令，也不是摩斯电码，则直接输出在屏幕上(可用于输入空格以便于分割单词)

Example:
Fuck_Morse_Code.py -s ".-. .-- - --- ...."
Fuck_Morse_Code.py -r "hello world"
Fuck_Morse_Code.py -c
```