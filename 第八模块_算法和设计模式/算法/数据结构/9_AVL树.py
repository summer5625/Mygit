# -*- coding: utf-8 -*-
# @Time    : 2020/1/15  21:06
# @Author  : XiaTian
# @File    : 9_AVL树.py


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


class AVLNode(BiTreeNode):

    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0


class AVLTree(BST):
    # 左减右
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        g = c.lchild
        s2 = g.lchild
        s3 = g.rchild

        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        if g.bf >0:
            c.bf = 0
            p.bf = -1
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        g.bf = 0

        return g

    def rotate_left_right(self, p, c):
        g = c.rchild
        s2 = g.lchild
        s3 = g.rchild
        c.rchild = s2
        if s2:
            s2.parent = c

        g.lchild = c
        c.parent = g

        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        if g.bf > 0:
            c.bf = -1
            p.bf = 0
        elif g.bf < 0:
            p.bf = 1
            c.bf = 0
        g.bf = 0

        return g

    def insert_not_rec(self, val):
        p = self.root
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:
                return

        # 更新树高度，并旋转使其平衡
        while node.parent:

            if node.parent.lchild == node: # 如果插入到父节点的左子树上
                if node.parent.bf < 0: # 原来插入节点的父节点有一个右子树
                    g = node.parent.parent # 旋转后需要连接的父节点
                    x = node.parent # 旋转前的子树的根
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                elif node.parent.bf > 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else: # 如果插入到父节点的右子树上
                if node.parent.bf > 0: # 原来插入节点的父节点有一个左子树
                    g = node.parent.parent  # 旋转后需要连接的父节点
                    x = node.parent  # 旋转前的子树的根
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                elif node.parent.bf > 0: # 原来插入节点的父节点有一个右子树
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue
            # 连接旋转后的子树
            n.parent = g
            if g:
                if g.lchild == x:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


tree = AVLTree([9,8,7,6,5,4,3,2,1])
tree.pre_order(tree.root)
print('\n')
tree.in_order(tree.root)
































