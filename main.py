from worker import Worker
from ui import list_workers, pay_per_day, num_workers_must_int

num_workers = num_workers_must_int()

worker = Worker('', '', 0, 0)
worker_info_list = []
# print(num_workers)
for i in range(0, num_workers):
    res = list_workers()
    worker_info_list.append(res)
print(f"Final List: {worker_info_list}")

for i in range(len(worker_info_list)):
    pay_per_day(worker_info_list[i])
