# python3

from collections import namedtuple
from heapq import heappush, heappop

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
FreeWorker = namedtuple("FreeWorker", ["finish_time", "worker_id"])


def assign_jobs_naive(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs(n_workers, jobs):
    result = []
    heap = []
    for i in range(n_workers):
        heappush(heap, FreeWorker(0, i))

    def get_next_free_worker(workers):
        next_finish_time, next_worker_id = heappop(workers)

        if len(workers) > 0 and workers[0][0] == next_finish_time:
            tmp_free_workers = [(next_worker_id, next_finish_time)]

            while len(workers) > 0 and workers[0][0] == next_finish_time:
                tmp_finish_time, tmp_worker_id = heappop(workers)
                heappush(tmp_free_workers, (tmp_worker_id, tmp_finish_time))

            next_worker_id, next_finish_time = heappop(tmp_free_workers)

            while len(tmp_free_workers) > 0:
                tmp_worker_id, tmp_finish_time = heappop(tmp_free_workers)
                heappush(workers, FreeWorker(tmp_finish_time, tmp_worker_id))

        return next_finish_time, next_worker_id

    for i, job in enumerate(jobs):
        if i < n_workers:
            finish_time, worker_id = heappop(heap)
        else:
            finish_time, worker_id = get_next_free_worker(heap)

        result.append(AssignedJob(worker_id, finish_time))
        heappush(heap, FreeWorker(finish_time + job, worker_id))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
