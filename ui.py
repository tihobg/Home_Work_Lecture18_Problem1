from worker import Worker
from typing import List


def money_for_1_hour(payment: int, working_hours: int) -> float:
    total_payment = payment / working_hours
    return total_payment


def list_workers() -> List:
    worker = Worker('', '', 0, 0)
    worker_info_list = []
    worker.name = input('Please enter the name\n')
    worker.surname = input('Please enter the surname\n')
    worker.payment = payment_must_int()
    worker.working_hours = work_hours_must_int()
    worker_info = [worker.name, worker.surname, worker.payment, worker.working_hours]
    worker_info_list.append(worker_info)
    print(worker_info)
    return worker_info


def pay_per_day(worker_data) -> str:
    worker = Worker('', '', 0, 0)
    worker.name = worker_data[0]
    worker.surname = worker_data[1]
    worker.payment = worker_data[2]
    worker.working_hours = worker_data[3]
    payment_per_day = money_for_1_hour(worker.payment, worker.working_hours)
    print(f"{worker.name} {worker.surname} {payment_per_day}")
    return worker_data


def num_workers_must_int() -> int:
    while True:
        try:
            num_workers = int(input('Please enter the number of workers!\n'))
            break
        except ValueError:
            print('Not a number')
            print('Try again')

    return num_workers


def payment_must_int() -> int:
    while True:
        try:
            payment = int(input('Please enter the payment per hour\n'))
            break
        except ValueError:
            print('Not a number')
            print('Try again')

    return payment


def work_hours_must_int() -> int:
    while True:
        try:
            work_hours = int(input('Please enter the working hours per day\n'))
            break
        except ValueError:
            print('Not a number')
            print('Try again')

    return work_hours


