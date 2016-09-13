#MacCRLF-2016.08.23
---

由于系统原因，Mac下生成的txt文件的换行符是'\n'也就是0x0a，而Windows下的换行使用的是0x0d0x0a。这样在Windows系统下打开文件就不会有换行，比较困扰。所以写了这个脚本，将Mac下生成的txt内容中的0x0a替换成0x0d0x0a。

	Usage:
		python crlf.py filename output
		filename        要转换的文件
		output          要生成的文件名
