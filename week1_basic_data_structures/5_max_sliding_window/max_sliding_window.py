# python3

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def Push(self, a):
        if len(self.__stack) == 0 or self.__max_stack[-1] <= a:
            self.__max_stack.append(a)
        self.__stack.append(a)

    def Pop(self):
        a = self.__stack.pop()
        if self.__max_stack[-1] == a:
            self.__max_stack.pop()
        return a

    def Max(self):
        if len(self.__max_stack) == 0:
            return -1 * float("Inf")
        return self.__max_stack[-1]

    def Len(self):
        return len(self.__stack)


def max_sliding_window(sequence, m):
    maximums = []
    stack_1 = StackWithMax()
    stack_2 = StackWithMax()

    def enQueue(v):
        stack_1.Push(v)

    def deQueue():
        if stack_1.Len() == 0 and stack_2.Len() == 0:
            pass

        if stack_2.Len() == 0:
            while stack_1.Len() > 0:
                stack_2.Push(stack_1.Pop())

        return stack_2.Pop()

    for i, v in enumerate(sequence):
        if i < m:
            enQueue(v)
        else:
            maximums.append(max(stack_1.Max(), stack_2.Max()))
            enQueue(v)
            deQueue()
    maximums.append(max(stack_1.Max(), stack_2.Max()))
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
