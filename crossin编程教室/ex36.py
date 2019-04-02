# -*- coding: UTF-8 -*-
from sys import exit

def  bear_room():
	while True:
		choice = raw_input('your choice: ')
		if choice == "take money":
			print "you are dead!"
		elif choice == "taunt bear":
			print "you are luck guy!"
			choose = raw_input('your choose: ')
			if choose == "open door":
				gold_room()
			else:
				print "you are dead!"
		else:
			"try again!!!"

def  cthulhu_room():
	numbers = ['eat head', 'flee']
	choice = raw_input('>>>>>')
	if choice == numbers[0]:
		print "you are dead!"
	elif choice == numbers[1]:
		start()
	else:
		print "No exit!"
		exit(0)

def gold_room():
	print "CONGRATULATION!:)"
	print "Please input your number:"
	number = int(raw_input('>>>>>> '))
	if number < 50:
		print "Yeah! you get %d golds" % number
		exit(0)
	else:
		print "you are so greedy that you are beat...."

def start():
	print "You can see two doors."
	choice = raw_input('right or left:\n')
	
	if "right" in choice:
		bear_room()
	elif "left" in choice:
		cthulhu_room()
	else:
		print "please try again....."

start()