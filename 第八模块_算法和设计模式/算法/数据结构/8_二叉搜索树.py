# -*- coding: utf-8 -*-
# @Time    : 2020/1/15  15:20
# @Author  : XiaTian
# @File    : 8_二叉搜索树.py
# 二叉搜索树的左边节点都比父节点小，右边的都比父节点大


class BiTreeNode:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:

    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_not_rec(val)

    # 查询
    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        elif node.data == val:
            return node

    def query_not_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            elif p.data == val:
                return p
        return None

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node

        return node

    # 不通过递归实现插入
    def insert_not_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def pre_order(self, root):
        if root:
            print(root.data, end=', ')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=', ')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=', ')

    def __remove_node_1(self, node):
        # 情况1：node是叶子节点
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
        elif node == node.parent.rchild:
            node.parent.rchild = None

    def __remove_node_21(self, node):
        # 情况2：node只有一个左孩子
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况3：node只有一个右孩子
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.lchild.parent = node.parent

    def delete(self, val):
        if self.root:
            node = self.query_not_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild:
                self.__remove_node_21(node)
            elif not node.lchild:
                self.__remove_node_22(node)
            else:
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


tree = BST([1,2,3,4,5,6,7,8,9])
tree.pre_order(tree.root)
print('\n')
tree.in_order(tree.root)
tree.delete(1)
tree.delete(2)
print('\n')

tree.post_order(tree.root)
print('\n')











































