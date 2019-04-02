# -*- coding: utf-8 -*-

class Node(object):
	"""节点"""
	def __init__(self, elem):
		self.elem = elem
		self.next = None

class SingleLinkList(object):  # 判空、长度、遍历、插入、删除、查找
	"""单链表"""
	def __init__(self, node=None):
		self.__head = node
		
	def is_empty(self):
		"""链表是否为空"""
		return self.__head == None
		
	def length(self):
		"""链表长度"""
		# cur游标，用来遍历节点
		cur = self.__head
		# count记录数量
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count
	
	def travel(self):
		"""遍历整个列表"""
		cur = self.__head
		while cur != None:
			print cur.elem,
			cur = cur.next
		print
	
	def add(self, item):  # O(1)
		"""链表头部增加一个元素，头插法"""
		node = Node(item)
		node.next = self.__head
		self.__head = node
	
	def append(self, item):  # O(n)
		"""链表尾部插入一个元素，尾插法"""
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node

	def insert(self, pos, item):
		"""指定位置添加元素"""
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			pre = self.__head
			count = 0
			while count < (pos-1):
				count += 1
				pre = pre.next
			node = Node(item)
			node.next = pre.next
			pre.next = node
	
	def remove(self, item):  # 先初始化两个结点，然后写遍历操作，然后写删除操作，然后写循环，最后加入判断、考虑特殊情况
		"""删除节点"""
		cur = self.__head
		pre = None
		while cur != None:  # 链表非空 
			if cur.elem == item:
				if cur == self.__head:
					# 先判断此结点是否为头结点
					# 头结点
					self.__head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next
	
	def search(self, item):
		"""查找节点是否存在"""
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False

if __name__ == "__main__":
	ll = SingleLinkList()
	print ll.is_empty()  # True
	print ll.length()  # 0
	
	ll.append(1)
	print ll.is_empty()  # False
	print ll.length()  # 1
	
	ll.append(2)
	ll.add(8)
	ll.append(3)
	ll.append(4)
	ll.append(5)
	ll.append(6)
	ll.insert(-1, 9)
	ll.travel()  # 9 8 1 2 3 4 5 6
	ll.insert(3, 100)
	ll.travel()  # 9 8 1 100 2 3 4 5 6
	ll.insert(10, 200)
	ll.travel()  # 9 8 1 100 2 3 4 5 6 200
	ll.remove(100)
	ll.travel()  # 9 8 1 2 3 4 5 6 200
	ll.remove(9)
	ll.travel()  # 8 1 2 3 4 5 6 200
	ll.remove(200)
	ll.travel()  # 8 1 2 3 4 5 6