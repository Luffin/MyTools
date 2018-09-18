# Dereplication
---

在整理资产时经常有去重的需求，干脆写一个脚本方便做去重。去重之后用`\r\n`作为每行分隔符，保证Windows下也能正常查看。且最后会输出去重前去重后的数量，有个对比

	Usage:
			python dereplication.py filename {output_name}
			filename			要去重的文件
			output_name	输出文件名，不指定的话默认用filename