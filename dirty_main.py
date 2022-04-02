
 from Decorator_home import *

from datetime import datetime
import time

def decorating_func(own_func):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return own_func

@decorating_func
def addition(num1,num2):
    return num1 + num2

@decorating_func
def multiply(num1,num2):
    return num1 * num2

print(addition(10,5))
time.sleep(71)
print(multiply(10,5))