# Base64Dict-2016.07.25
---

在对如Tomcat管理界面爆破时，由于使用的是HTTP认证，用户名和密码是以下面的形式组成在`base64`编码而成进行请求的
	
	username:password

所以需要将用户名密码字典组合并且进行base64编码，这就是这个脚本的功能

	Usage:
		python base64dict.py username.txt password.txt
		脚本会在当前目录下生产一个result.txt的结果文件
