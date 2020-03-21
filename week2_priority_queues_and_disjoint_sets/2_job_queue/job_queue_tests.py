import unittest

from test_runner import test_runner
from job_queue import assign_jobs, assign_jobs_naive
import random


class TestCheckBrackets(unittest.TestCase):
    def test_main(self):
        test_data = test_runner('./tests')
        for test in test_data:
            data, result, file = test
            if result is not None:
                n_workers, _ = list(map(int, data[0].split()))
                jobs = list(map(int, data[1].split()))
                result = list(map(lambda item: tuple(map(int, item.split())), result))
                assigned_jobs = assign_jobs(n_workers, jobs)
                print('file', file)
                self.assertCountEqual(result, assigned_jobs)

    def test_naive(self):
        test_data = test_runner('./tests')
        for test in test_data:

            data, result, file = test

            if '08' not in file:
                n_workers, _ = list(map(int, data[0].split()))
                jobs = list(map(int, data[1].split()))
                assigned_jobs = assign_jobs(n_workers, jobs)
                assigned_jobs_naive = assign_jobs_naive(n_workers, jobs)
                print('file', file)
                self.assertCountEqual(assigned_jobs, assigned_jobs_naive)

    def test_stress(self):
        for i in range(5000):
            n_workers = random.randint(1, 10 ** 2)
            jobs = [random.randint(0, 10 ** 3) for _ in range(random.randint(1, 10 ** 3))]
            assigned_jobs_naive = assign_jobs_naive(n_workers, jobs)
            assigned_jobs = assign_jobs(n_workers, jobs)
            print('test', i, n_workers, jobs)
            self.assertCountEqual(assigned_jobs, assigned_jobs_naive)

    if __name__ == '__main__':
        unittest.main()
