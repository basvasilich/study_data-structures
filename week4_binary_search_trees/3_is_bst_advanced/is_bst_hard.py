#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 9)  # max depth of recursion
threading.stack_size(2 ** 28)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    global prev
    if len(tree) == 0:
        return True

    def helper(index, mn, mx):
        if index == -1:
            return True
        val = tree[index][0]

        if val < mn or val > mx:
            return False
        return helper(tree[index][1], mn, val - 1) and helper(tree[index][2], val, mx)

    return helper(0, -2147483648, 2147483647)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
