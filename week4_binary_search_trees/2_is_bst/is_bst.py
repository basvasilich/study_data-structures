#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 9)  # max depth of recursion
threading.stack_size(2 ** 28)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    global prev
    if len(tree) == 0:
        return True

    def helper(index):
        global prev
        if index == -1:
            return True

        if not helper(tree[index][1]):
            return False

        if prev is not None and prev > tree[index][0]:
            return False
        prev = tree[index][0]
        return helper(tree[index][2])
    prev = None
    return helper(0)


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
