# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next, i))

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1

            last, last_index = opening_brackets_stack.pop()

            if not are_matching(last, next):
                return i + 1

    if len(opening_brackets_stack) != 0:
        last, last_index = opening_brackets_stack.pop()
        return last_index + 1

    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
