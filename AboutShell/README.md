#AboutShell-2015.12.3
---

自己写的简单工具，没有想得特别多，所以写的比较简单粗暴，算是当时编写的分析能力的记录吧

###Del_shell.py(在服务器上简单查杀shell的工具)

运行，`path`参数即需要检测webshell的文件夹路径

	python Del_shell.py path

脚本运行之后会先遍历所有文件，找出最迟创建的文件的创建时间，记录它的创建时间的时间戳到`time.txt`文件中(以便在之后脚本意外中断之后不会重新记录文件时间)

之后脚本开始间隔5秒循环遍历文件夹，若发现有文件的创建时间迟于`time.txt`记录的时间，则判定为非法文件(当然这也太简单粗暴了，姑且这样吧)。同时，脚本也会对文件大小小于200字节的文件内容进行正则匹配，匹配以下语句:

	eval($_POST[xxx])
	eval($_GET[xxx])
	system($_POST[xxx])
	system($_GET[xxx])

匹配到的话也会记录为非法文件。

这些非法文件的文件内容都会被记录到`log.txt`，以便查看webshell内容，方便其他操作

以上`time.txt`和`log.txt`文件都创建在运行脚本的文件夹下
###Continue_Connecting.py(持续访问网站文件的脚本)

Usage：

	-u				访问的URL
	-f				要访问的文件名字
	-n				访问次数
	
Example：
	
	python Continue_Connecting.py -u http://192.168.3.4 -f ooxx.php -n 10000
###Not_Easy_Go_Die.php(不死马)

PHP不死马，间隔1秒循环检查`1.php`是否存在，若不存在则创建它，并写入指定内容。