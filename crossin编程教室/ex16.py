# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl-C (^C)."
print "If you do want that, hit Enter."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')  # 打开文件,w执行写操作

print "Truncating the file. Goodbye!"
target.truncate()  # 删除文本中的内容

print "Now I'm going to write these to the file."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()  # 关闭文件