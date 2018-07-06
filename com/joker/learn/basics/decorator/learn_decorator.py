#  Python 装饰器学习：在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

import datetime
import functools
import time

# 定义一个能打印日志的 decorator
from typing import Optional


def my_log(func: Optional) -> object:
    """
    包装一个函数，函数打印日志，打印函数名称

    :param func: a function
    :return: a function wrapper
    """

    def wrapper(*args, **kv) -> object:
        """
        打印参数函数的名称

        :param args: the type belongs to tuple
        :param kv: the type belongs to dict
        :return: a function
        """
        print("call %s():" % func.__name__)

        return func(*args, **kv)

    return wrapper


# 定义一个函数打印当前时间
@my_log
def now_time():
    """

        print the now time
    """
    print(time.strftime("%Y-%m-%d %H:%M:%S"))


print(type(now_time))
f = now_time
print(f.__name__)

print("分割线".center(100, "-"))
# 调用,等于调用了my_log(now_time),这个now_time是没有注解的方法
now_time()
f = my_log(now_time)
f()

print("练习".center(100, "="))


# 请编写一个 decorator，能在函数调用的前后打印出 'begin call' 和 'end call' 的日志

def log_practice(text):
    def log_before_end(func):
        print("begin call")

        @functools.wraps(func)
        def wrappre(*args, **kv):
            # 函数会在这里被调用
            res = func(*args, **kv)
            print('end call')
            return res

        return wrappre

    return log_before_end


@log_practice("handsome")
def practice():
    print("this is a practice!")

practice()
