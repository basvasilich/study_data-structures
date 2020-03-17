import unittest

from test_runner import test_runner
from check_brackets import find_mismatch


class TestCheckBrackets(unittest.TestCase):
    def test_main(self):
        test_data = test_runner('./tests')

        for args, answer in test_data:
            self.assertEqual(find_mismatch(*args), answer if answer == 'Success' else int(answer[0]))


if __name__ == '__main__':
    unittest.main()
