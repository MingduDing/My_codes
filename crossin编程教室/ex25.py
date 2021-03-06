# -*- coding: UTF-8 -*-
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')  # 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
	return words

def sort_words(words):
	"""Sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。 0是第一个
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)  # -1是最后一个元素
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)