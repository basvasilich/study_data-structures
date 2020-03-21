import unittest

from test_runner import test_runner
from job_queue import assign_jobs


class TestCheckBrackets(unittest.TestCase):
    def test_main(self):
        test_data = test_runner('./tests')
        for test in test_data:
            data, result, file = test

            n_workers, _ = list(map(int, data[0].split()))
            jobs = list(map(int, data[1].split()))
            result = list(map(lambda item: tuple(map(int, item.split())), result))
            assigned_jobs = assign_jobs(n_workers, jobs)
            print('file', file)
            self.assertCountEqual(result, assigned_jobs)

    if __name__ == '__main__':
        unittest.main()
