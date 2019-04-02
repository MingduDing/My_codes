# -*- coding: utf-8 -*-
name = 'Zed A. Shaw'  # 单引号表示结构体
age = 35  # 整型不需要单引号
height = round(74) * round(2.54)  # cm
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name  # %s表示结构体
print "He's %dcm tall." % height
print "He's %dkg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, 
	height, weight, age + height + weight)
