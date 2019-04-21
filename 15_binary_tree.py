# -*- coding: utf-8 -*-

class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None
class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None
        
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
           else:
            	queue.append(cur_node.lchild)
           if cur_node.rchild is None:
            	cur_node.rchild = node
                return
           else:
            	queue.append(cur_node.rchild)
                
    def breath_travel(self):
        """广度遍历"""
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
		"""先序遍历"""
        if node is None:
            return
        print(node.item, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    
    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        print(node.item, end=' ')
        self.inorder(node.lchild)
        self.ineorder(node.rchild)
        
    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        print(node.item, end=' ')
        self.postorder(node.lchild)
        self.postorder(node.rchild)

if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.breath_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)