# python3

import sys


class Solver:
    def __init__(self, s):
        self.s = s
        self.m1 = 10 ** 9 + 7
        self.m2 = 10 ** 9 + 9
        self.x1 = 2
        self.x2 = 3
        self.h1 = dict()
        self.h2 = dict()
        self.h1[0] = 0
        self.h2[0] = 0

        for i in range(1, len(self.s) + 1):
            self.h1[i] = (self.x1 * self.h1[i - 1] + ord(s[i - 1])) % self.m1
        for j in range(1, len(self.s)):
            self.h2[j] = (self.x2 * self.h2[j - 1] + ord(s[j - 1])) % self.m2

    def ask(self, a, b, l):
        z = pow(self.x1, l, self.m1)
        x = pow(self.x2, l, self.m2)
        return (self.h1[a + l] - z * self.h1[a]) % self.m1 == (self.h1[b + l] - z * self.h1[b]) % self.m1 \
               and (self.h2[a + l] - x * self.h2[a]) % self.m2 == (self.h2[b + l] - x * self.h2[b]) % self.m2


if __name__ == '__main__':
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)

    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, l) else "No")
