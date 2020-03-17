import unittest

from test_runner import test_runner
from process_packages import Request, Buffer, process_requests


class TestCheckBrackets(unittest.TestCase):
    def test_main(self):
        test_data = test_runner('./tests')
        for test in test_data:
            data, result, file = test

            buffer_size, n_requests = map(int, data[0].split())
            requests = []

            for i in range(n_requests):
                arrived_at, time_to_process = map(int, data[i + 1].split())
                requests.append(Request(arrived_at, time_to_process))

            buffer = Buffer(buffer_size)
            responses = list(map(lambda x: x.started_at, process_requests(requests, buffer)))
            expected = list(map(int, result))
            print('file', file)
            self.assertCountEqual(responses, expected)

    if __name__ == '__main__':
        unittest.main()
