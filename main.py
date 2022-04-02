
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from logger import func_logger_w_path


@func_logger_w_path('func_logs.txt')
def its_some_oclock(arg):
    current_date = datetime.date(datetime.today())
    print(f'it\'s {current_date} already')
    return f'it\'s {current_date} already'


if __name__ == '__main__':
    its_some_oclock('some_arg')
    get_employees()
    calculate_salary()