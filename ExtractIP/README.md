# ExtractIP-2016.09.12
---

这个脚本通过简单的正则表达式匹配，把给出的URL文件中的所有IP提取出来并且去重，生成一份IP列表。

适用场景是在对公司内部资产进行测试时，面对大量资产列表，快速从中提取出IP，生成IP列表，交给nmap进行端口扫描或其他用处。

		Usage：
			python ip.py filename [output]
			filename		要转换的文件名
			output			要生成的文件名