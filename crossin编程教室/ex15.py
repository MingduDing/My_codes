# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv  # argument variable 参数变量，需要事先输入

txt = open(filename)  # open函数用于打开一个文件，创建一个file对象

print "Here's your file %r" % filename
print txt.read()  # read函数

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

