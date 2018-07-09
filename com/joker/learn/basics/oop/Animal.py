#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
学习Python的面向对象中的继承和多态的属性。

@author: Joker

@projectName: learn

@fileName: Animal.py

@createTime: 2018/7/9 17:24

"""


class Animal(object):
    def run(self):
        """
        动物类的run方法，简单打印

        :return:
        """
        print("Animal is running...")
        pass

    pass


class Dog(Animal):

    def run(self):
        print("Dog is running...")


class Cat(Animal):
    def run(self):
        print("Cat is running...")
    pass
