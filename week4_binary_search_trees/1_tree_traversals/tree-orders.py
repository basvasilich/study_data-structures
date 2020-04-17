# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []

        def helper(index):
            if index == -1:
                pass
            elif self.left[index] == -1 and self.right[index] == -1:
                self.result.append(self.key[index])
            elif self.left[index] == -1:
                self.result.append(self.key[index])
                helper(self.right[index])
            elif self.right[index] == -1:
                helper(self.left[index])
                self.result.append(self.key[index])
            else:
                helper(self.left[index])
                self.result.append(self.key[index])
                helper(self.right[index])

        helper(0)
        return self.result

    def preOrder(self):
        self.result = []

        def helper(index):
            if index == -1:
                pass
            elif self.left[index] == -1 and self.right[index] == -1:
                self.result.append(self.key[index])
            elif self.left[index] == -1:
                self.result.append(self.key[index])
                helper(self.right[index])
            elif self.right[index] == -1:
                self.result.append(self.key[index])
                helper(self.left[index])
            else:
                self.result.append(self.key[index])
                helper(self.left[index])
                helper(self.right[index])

        helper(0)
        return self.result

    def postOrder(self):
        self.result = []

        def helper(index):
            if index == -1:
                pass
            elif self.left[index] == -1 and self.right[index] == -1:
                self.result.append(self.key[index])
            elif self.left[index] == -1:
                helper(self.right[index])
                self.result.append(self.key[index])
            elif self.right[index] == -1:
                helper(self.left[index])
                self.result.append(self.key[index])
            else:
                helper(self.left[index])
                helper(self.right[index])
                self.result.append(self.key[index])

        helper(0)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
