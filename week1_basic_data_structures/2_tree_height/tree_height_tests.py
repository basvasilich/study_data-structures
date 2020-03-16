import unittest

from test_runner import test_runner
from tree_height import compute_height


class TestCheckBrackets(unittest.TestCase):
    def test_main(self):
        test_data = test_runner('./tests')

        for args, answer in test_data:
            n, parents = args
            self.assertEqual(compute_height(int(n), [int(i) for i in parents.split()]), int(answer))

    if __name__ == '__main__':
        unittest.main()
