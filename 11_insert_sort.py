# -*- coding: utf-8 -*-

def insert_sort(alist):
	"""插入排序"""
	for j in range(1, len(alist)):
		for i in range(j, 0, -1):
			if alist[i] < alist[i-1]:
				alist[i], alist[i-1] = alist[i-1], alist[i]

if __name__ == "__main__":
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print li
	insert_sort(li)
	print li 