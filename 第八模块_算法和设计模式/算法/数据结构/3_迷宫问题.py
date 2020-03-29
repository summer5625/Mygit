# -*- coding: utf-8 -*-
# @Time    : 2020/1/14  14:22
# @Author  : XiaTian
# @File    : 3_迷宫问题.py
# 走迷宫：给定一个起点和终点，找到一条通往终点的路径
# ##################################使用栈：回溯法（深度优先）
'''

每前进一个点都寻找该店四个方向上可以通行的路径，当没有路径时就回退到上一个点，回退到上一个点时寻找可通行方向时原来走过的方向就变成
不可通行方向，这样直接回退到有科通行方向的点，然后在向前走，直到找到终点。

'''
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
dirs = [
    lambda x, y: (x-1, y),
    lambda x, y: (x+1, y),
    lambda x, y: (x, y-1),
    lambda x, y: (x, y+1)
]


def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print(p)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print('没有路')
        return False


# maze_path(1, 1, 8, 8)


# #############################队列解决迷宫问题：广度优先,找到的路径时最短路径
'''

多分支前进：在起始点查找所有可通行的方向上的下一个点，并将其存放到队列中，多个方向同时前进，每前进一格就将上一个点出队列，并新建一个新列表存放
前进的这格对应的上一格的点位，找到终点后，向后退找出对应表中的路径点输出

'''
from collections import deque


def print_r(path):

    real_path = []
    i = len(path) - 1
    while i >= 0:
        real_path.append(path[i][0:2])
        i = path[i][2]
    real_path.reverse()
    for i in real_path:
        print(i)


def maze_path_queue(x1, y1, x2, y2):

    q = deque()
    path = []
    q.append((x1, y1, -1))

    while len(q) > 0:
        cur_node = q.popleft() # 当前点位
        path.append(cur_node)

        if cur_node[0] == x2 and cur_node[1] == y2:
            print_r(path)
            return True
        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                q.append((next_node[0], next_node[1], len(path)-1))
                maze[next_node[0]][next_node[1]] = 2
    return False


maze_path_queue(1, 1, 8, 8)






