import unittest

from test_runner import test_runner
from is_bst_hard import IsBinarySearchTree


class TestCheckBrackets(unittest.TestCase):
    def test_1(self):
        self.assertIs(IsBinarySearchTree([[4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]]), False)

    def test_2(self):
        self.assertIs(
            IsBinarySearchTree([[4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]),
            True)

    def test_3(self):
        self.assertIs(
            IsBinarySearchTree([[1, -1, -1], [2, 3, 4], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]),
            True)

    def test_4(self):
        self.assertIs(
            IsBinarySearchTree([]),
            True)

    def test_5(self):
        self.assertIs(
            IsBinarySearchTree([[2, 1, 2], [1, -1, -1], [2, -1, -1]]),
            True)

    def test_10(self):
        self.assertIs(
            IsBinarySearchTree([[2, 1, 2], [2, -1, -1], [3, -1, -1]]),
            False)


    def test_9(self):
        self.assertIs(
            IsBinarySearchTree([[1, 1, 2], [2, -1, -1], [3, -1, -1]]),
            False)

    def test_8(self):
        self.assertIs(
            IsBinarySearchTree([[2147483647, -1, -1]]),
            True)

    def test_6(self):
        self.assertIs(
            IsBinarySearchTree([[1, 1, 2], [2, -1, -1], [3, -1, -1]]),
            False)

if __name__ == '__main__':
    unittest.main()
