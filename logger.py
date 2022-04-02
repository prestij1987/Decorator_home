
import os
import atexit
from time import time, strftime, localtime
from datetime import timedelta
from datetime import datetime
#
# # логгер по первому заданию
#
def func_logger(some_func):
    def actual_logger(*args, **kwargs):
        log_entry = {}
        log_date_time = str(datetime.today())
        log_entry['datetime'] = log_date_time
        log_func_name = some_func.__name__
        log_entry['called function'] = log_func_name
        log_args = str(*args)
        log_entry['args'] = log_args
        log_kwargs = str(*kwargs)
        log_entry['kwargs'] = log_kwargs
        result = some_func(*args, **kwargs)
        log_entry['result'] = result
        with open(file_path, 'a', encoding = 'utf-8') as file:
            file.write(str(log_entry) + '\n')
        return result
    return actual_logger


# окончательный логгер

def func_logger_w_path(file_path):
    def func_logger(some_func):
        def actual_logger(*args, **kwargs):

            log_entry = {}

            log_date_time = str(datetime.today())
            log_entry['datetime'] = log_date_time

            log_func_name = some_func.__name__
            log_entry['called function'] = log_func_name

            log_args = str(*args)
            log_entry['args'] = log_args

            log_kwargs = str(*kwargs)
            log_entry['kwargs'] = log_kwargs

            result = some_func(*args, **kwargs)
            log_entry['result'] = result

            with open(file_path, 'a', encoding = 'utf-8') as file:
                file.write(str(log_entry) + '\n')

            return result

        return actual_logger
    return func_logger






# начало конструктора

def loger_constructor_decor(file_name, file_path=None):
    if file_path is None:
        file_place = os.path.join(os.getcwd())
    else:
        file_place = os.path.join(os.path.abspath(file_path))

    file_path = os.path.join(file_place, file_name)

    # начало декоратора
    def loger_decorator(old_function):

        def addition_def(*args, **kwargs):
            log_date = datetime.now().strftime("%d %B %Y  time %H:%M:%S")
            func_name = old_function.__name__
            input_data = f'вводные данные:{args} и {kwargs}'
            output_data = old_function(*args, **kwargs)
            result_line = f'вызвана функция {func_name} \n' \
                          f'дата и время вызова : {log_date} \n' \
                          f'{input_data} \n' \
                          f'результирующее значение функции {func_name}: {output_data}\n' \
                          f'-----------------------------------\n'

            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(result_line)

            return output_data

        return addition_def

    # конец декоратора
    return loger_decorator


import atexit
from time import time, strftime, localtime
from datetime import timedelta


def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))


def log(s, elapsed=None):
    line = "=" * 40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print()


def endlog():
    end = time()
    elapsed = end - start
    log("End Program", secondsToStr(elapsed))


start = time()
atexit.register(endlog)
log("Start Program")  # python3
import atexit
from time import time, strftime, localtime
from datetime import timedelta


def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))


def log(s, elapsed=None):
    line = "=" * 40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print()


def endlog():
    end = time()
    elapsed = end - start
    log("End Program", secondsToStr(elapsed))


start = time()
atexit.register(endlog)
log("Start Program")

