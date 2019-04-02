# -*- coding: utf-8 -*-
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args  # 参数解包
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):  # 跳过函数解包的过程，直接使用括号里面的名称作为变量名
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):  # 函数接受单个参数
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():  # 可以不接受任何参数
	print "I got nothing."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()