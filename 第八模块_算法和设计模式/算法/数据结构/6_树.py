# -*- coding: utf-8 -*-
# @Time    : 2020/1/15  14:13
# @Author  : XiaTian
# @File    : 6_树.py


class Node:

    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree:

    def __init__(self):
        self.root = Node('/')
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != '/':
            name += '/'
        if name == '../':
            self.now = self.now.parent
            return self.now
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return self.now
        raise ValueError('invalid dir %s' % name)


tree = FileSystemTree()
tree.mkdir('user/')
tree.mkdir('app/')
tree.mkdir('code/')
tree.cd('code/')
tree.cd('../')
print(tree.now.children)





















