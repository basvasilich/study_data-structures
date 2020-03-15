# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def Push(self, a):
        if len(self.__stack) == 0 or self.__max_stack[-1] <= a:
            self.__max_stack.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert (len(self.__stack))
        a = self.__stack.pop()
        if self.__max_stack[-1] == a:
            self.__max_stack.pop()

    def Max(self):
        assert (len(self.__stack))
        return self.__max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert (0)
