# -*- coding: utf-8 -*-

def bubble_sort(alist):
	"""冒泡排序"""
	n = len(alist)
	for j in range(n-1):  # 0 ~ n-2
		# 从头到尾要走n-1次，走一次冒个数
		count = 0
		for i in range(0, n-1-j):  # 0 ~ n-2-j
			# 从头走到尾
			if alist[i] > alist [i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
				count += 1
		if count == 0:
			return

if __name__ == "__main__":
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print li
	bubble_sort(li)
	print li
	
# for j in range(len(alist)-1, 0, -1):
	# # j表示每次遍历需要比较的次数
	# for i in range(j):
		# if alist[i] > alist[i+1]:
			# alist[i], alist[i+1] = alist[i+1], alist[i]