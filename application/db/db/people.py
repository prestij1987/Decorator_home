#
from logger import func_logger_w_path

@func_logger_w_path('func_logs.txt')
def get_employees():
    print('get outta here')

import logging

import datetime
import functools
def timer(func):
    """Этот декоратор выведет в консоли время выполнения вызываемого кода."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Выполнение функции {func.__name__} завершено через {run_time:.4f} секунд.")
        return val
    return wrapper
@timer
def dothings(n_times):
    for _ in range(n_times):
        return sum((i ** 3 for i in range(100_000)))

