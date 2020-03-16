# python3

import sys
import threading


def compute_height(n, parents):
    root = 0
    tree = {}
    max_height = 0
    for index, parent in enumerate(parents):
        if parent == -1:
            root = index
        elif parent in tree.keys():
            tree[parent].append(index)
        else:
            tree[parent] = [index]
    stack = [(1, tree[root])]

    while len(stack) > 0:
        height, item = stack[-1]
        if len(item) == 0:
            stack.pop()
        else:
            max_height = max(max_height, height)
            child = item.pop()

            if child in tree.keys():
                stack.append((height + 1, tree[child]))
            else:
                max_height = max(max_height, height + 1)

    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == "__main__":
    main()
