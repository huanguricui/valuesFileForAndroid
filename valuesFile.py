#!/usr/bin/python3
import sys

# 打开文件
x = 320
y = 480
targetX = int(sys.argv[1])
targetY = int(sys.argv[2])
fo = open(sys.argv[3], "w")
print("文件名为: ", fo.name)
fo.writelines('<?xml version="1.0" encoding="utf-8"?>\n')
fo.writelines('<resources>\n')
i = 1
while(i < (x + 1)):
	var1 = '<dimen name = "x' + str(i) +'">'+ str(i * float(targetX) / float(x)) + 'px</dimen>'
	var2 = '\n'
	var = var1 + var2
	fo.writelines(var)
	i += 1
j = 1
while(j < (y + 1)):
	var1 = '<dimen name = "y' + str(j) +'">'+ str(j * float(targetY) / float(y)) + 'px</dimen>'
	var2 = '\n'
	var = var1 + var2
	fo.writelines(var)
	j += 1
fo.writelines('</resources>\n')
# 关闭
fo.close()