# -*- coding: utf-8 -*-
"""
    this is a student,学习面向对象.

    变量：__两个下划线开头的变量表示是私有变量。不能在类的外部使用或直接访问。
    方法：类方法必须包含参数self,__两个下划线开头方法是私有方法。
    __xx__:以双下划线开头，和双下划线结尾的是特殊变量，可以直接访问，赋值
"""
from typing import Any


class Student(object):
    def __init__(self, name: str, source: float, age: int =20) -> object:
        """
         __init__ 方法是用来创建实力对象向的构造器

         __init__ 方法内部，就可以把各种属性(变成公有属性)绑定到 self ，因为 self就指向创建的实例本身。

        :param name: 学生的姓名
        :param source: 学生的成绩
        """
        self.name = name
        self.source = source
        # 设置私有年龄属性 __两个下划线是私有（private）的
        self.__age = age
        pass

    def print_name_source(self):
        """
            打印学生的姓名和成绩

        :return: None
        """
        print("%s:%s" % (self.name, self.source))
        print("age:%s" % self.__age)
        pass

    def get_age(self)-> int:
        """
        访问私有变量__age变量的方法

        :return: int age
        """
        return self.__age

