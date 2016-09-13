#GetIPFromNmapResult-2016.09.13
---

当目标量较大时，通常会使用nmap批量对目标进行扫描。这样生成的扫描结果由于数量较大内容杂乱，不方便梳理关键的某个服务、某个端口出来进行进一步测试。

例如，想要找出所有开放了`ftp`服务的IP来进行批量匿名登录测试，手工方法自然是在文本编辑器中使用`Ctrl + f`查找`ftp`，然后把相应的IP复制出来生成一个新的txt。这样太麻烦了，特别是在目标量大的时候。

所以写了这个脚本，根据给出的`info`信息，匹配出对应的IP并打印出来，`info`信息可以是端口号或者端口对应的服务

	Usage:
	python getip.py filename info
	filename	nmap scan result file
	info		the info you want to find.(e.g. 22;ssh;telnet;3306)