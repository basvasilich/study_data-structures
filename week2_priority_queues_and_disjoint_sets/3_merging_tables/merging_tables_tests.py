import unittest

from test_runner import test_runner
from merging_tables import Database


class TestCheckBrackets(unittest.TestCase):
    def test_main(self):
        test_data = test_runner('./tests')
        for test in test_data:
            data, result, file = test
            if result is not None:
                result = list(map(int, result))
                n_tables, n_queries = map(int, data[0].split())
                counts = list(map(int, data[1].split()))
                db = Database(counts)
                expected = []
                for i in range(2, n_queries + 2):
                    dst, src = map(int, data[i].split())
                    db.merge(dst - 1, src - 1)
                    expected.append(db.max_row_count)
                print('file', file)
                self.assertCountEqual(result, expected)

    if __name__ == '__main__':
        unittest.main()
