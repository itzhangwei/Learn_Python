# 对于高阶函数的使用，练习题

# 练习题1： 利用 map() 函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入： ['adam', 'LISA', 'barT'] ，输出： ['Adam',
# 'Lisa', 'Bart'] ：


# 指定参数的参数类型，和返回值类型都是str
from functools import reduce
from numbers import Number

print("练习题1".center(100, "="))


def upper_first_letter(letter: str) -> str:
    """
    upper_first_letter(str) ->str


    Return  将输入进来的字符串转换为首字母大写的单子
    """
    if not isinstance(letter, str):
        raise TypeError("传入字符串！")

    # 切片字符串，然后首字母大写，其余的小写

    return letter[:1].upper() + letter[1:].lower()

    pass


s = ['adam', 'LISA', 'barT']
print(list(map(upper_first_letter, s)))

# 采用lambda写法

print(list(map(lambda x: x[:1].upper() + x[1:].lower(), s)))

# print(upper_first_letter(1)) 参数类型不对应，直接异常


print("练习题2".center(100, "="))


# 练习题2：请编写一个 prod() 函数，可以接受一个 list 并利用 reduce() 求积


def prod(l: list) -> Number:
    """
    可以接受一个 list 并利用 reduce() 求积


    :param l: 接受一个list参数，里面数数值型
    :return: 返回list中的所有数值的乘积
    """
    # 数据类型判断
    if not isinstance(l, list):
        raise TypeError("需要一个列表类型,你给了一个：" + str(type(l)))

    def product(x: Number, y: Number) -> Number:
        if not isinstance(x, Number) and not isinstance(y, Number):
            raise TypeError("需要一个数值类型，你给了一个" + str(type(y)))

        return x * y
        pass

    # lambda写法,没有办法抛异常
    # return reduce(lambda x, y: x * y if isinstance(x, Number) and isinstance(y, Number) else "type error", l)
    # return reduce(lambda x, y: product(x,y), l)
    return reduce(product, l)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# prod({}) 错误数据类型测试
# prod(["1","2","3"]) 错误数据类型测试


# 回数是指从左向右读和从右向左读都是一样的数，例如 12321 ， 909 。请利用 filter() 滤掉1000以内非回数
print("练习题3".center(100, "="))
num_list = list(x for x in range(1000))
# filter返回的Iterator 需要使用list转换下，Iterator对象是一个数据流对象
# 凡是可作用于 for 循环的对象都是 Iterable 类型；
# 凡是可作用于 next() 函数的对象都是 Iterator 类型，它们表示一个惰性

# lambda 写法，采用转换字符串后切片比较是否一致，等于是反转字符串，方法多种多样
num_list2 = list(filter(lambda x: str(x)[::-1] != str(x), num_list))

print(num_list2)


# 定义方法的方式,转换字符串，然后切片的歩长为-1，表示从后往前切片
def back_number(num: int) -> bool:
    """

    :param num: int 类型参数
    :return: 如果是回数返回false，不是回数返回true
    """
    if not isinstance(num, int):
        raise TypeError \
            ("need an int type parameter, but give an parameter of " + str(type(num)))
    return not str(num)[::-1] == str(num)
    pass


# 调用方法，使用filter过滤出非回数
num_list3 = list(filter(back_number, num_list))
print(num_list3)

# sorted排序函数
print("sorted排序函数".center(100, "="))
# sorted 函数：排序参数，默认升序
# 参数1.iterable：可以迭代的对象
# 参数2.key：用于排序的字段值，可调用函数来修改排序字段
# 参数3.reverse:布尔类型，True是降序，false是升序，默认False
sort_list1 = [12, 7, -6, 23, 43, -7, 0, 8]
print(sorted(sort_list1))
# 倒叙
print(sorted(sort_list1, reverse=True))
# 对排序值取绝对值排序
print(sorted(sort_list1, key=abs, reverse=True))

sort_list2 = ['bob', 'about', 'Zoo', 'Credit']
# 按照ASCII码来排序
print(sorted(sort_list2))
# 不区分大小写，全部转换为小写或者大写
print(sorted(sort_list2, key=str.lower))

# 字典排序,必须制定字典里面的排序字段，否则排序不了
sort_dict = [
    {"name": "joker", "age": 23},
    {"name": "jack", "age": 12},
    {"name": "rose", "age": 25},
    {"name": "tom", "age": 18},
]
print(sorted(sort_dict, key=lambda d: d["age"]))

print("sort练习题".center(100, "="))

# 假设我们用一组 tuple 表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用 sorted() 对上述列表分别按名字排序：
# 再按成绩从高到低排序：
sort_score = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88), ('Bob', 88), ]

# 默认排序使用元祖里面属性（名字，成绩）升序，
# 结果：[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Bob', 88), ('Lisa', 88)]
print(sorted(sort_score))

# 名字升序，成绩降序，
# 结果：[('Adam', 92), ('Bart', 66), ('Bob', 88), ('Bob', 75), ('Lisa', 88)]
print(sorted(sort_score, key=lambda x: (x[0], -x[1]), reverse=False))

# 先成绩升序，名字升序（字符串，无法去获取负数）降序，
# 结果：[('Bart', 66), ('Bob', 75), ('Bob', 88), ('Lisa', 88), ('Adam', 92)]
print(sorted(sort_score, key=lambda x: (x[1], x[0],), reverse=False))

# 先成绩升序，名字降序（字符串，无法去获取负数）降序，
# 结果：[('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Bob', 88), ('Adam', 92)]
# 字符串，无法去获取负数，可修改后面的reverse,但是如果遇到两个字符串，一个升序一个降序的问题就需要解决下，
# 采用ord()函数获取字符的ASCII，每一个字符转换一个ASCII，取负数，组成一个元祖
print(sorted(sort_score,
             key=lambda x: (x[1], tuple(map(lambda c: -ord(c), x[0]))),
             reverse=False))
