# -*- coding: utf-8 -*-

class Node(object):
	"""结点"""
	def __init__(self, item):
		self.elem = item
		self.next = None
		self.prev = None

class DoubleLinkList(object):
	"""双链表"""
	def __init__(self, node=None):
		self.__head = node
		
	def is_empty(self):
		"""链表是否为空"""
		return self.__head is None
		
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
	
	def add(self, item):
		"""链表头部增加一个元素，头插法"""
		node = Node(item)
		node.next = self.__head
		self.__head.prev = node
		self.__head = node
	
	def append(self, item):
		"""链表尾部插入一个元素，尾插法"""
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.prev = cur

	def insert(self, pos, item):
		"""指定位置添加元素"""
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			cur = self.__head
			count = 0
			while count < pos:
				count += 1
				cur = cur.next
			node = Node(item)
			node.next = cur
			node.prev = cur.prev
			cur.prev = node
			node.prev.next = node
			# node.next = cur
			# ode.prev = cur.prev
			# cur.prev.next = node
			# cur.prev = node
			
	def remove(self, item):
		"""删除节点"""
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				# 先判断此结点是否为头结点
				if cur == self.__head:
					self.__head = cur.next
					if cur.next:
						# 判断链表是否只有一个结点
						cur.next.prev = None
				else:
					cur.prev.next = cur.next
					if cur.next:
						cur.next.prev = cur.prev
				break
			else:
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
	ll = DoubleLinkList()
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