"""
调用学生类。
"""
from com.joker.learn.basics.oop.Animal import *
from com.joker.learn.basics.oop.Student import Student

# 创建实体类学生对象
joker = Student("joker", 98.5, 23)
# 打印学生属性
print(joker.name)
print(joker.source)
# 调用方法，打印姓名和成绩
joker.print_name_source()
# 访问私有变量__age,不予许访问，报错,可以使用实例对象._类名变量来访问
# print(joker.__age) 报错
print(joker._Student__age)
print(joker.get_age())


print("华丽的分割线".center(100,"="))
# 调用Animal,Dog,Cat
animal = Animal()
animal.run()
dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 多态类型判断
dic = dict()
print(isinstance(dic,Animal))
print(isinstance(dog,Animal))
print(isinstance(dog,Dog))
print(isinstance(animal,Dog))


print("华丽的分割线".center(100,"="))
# isinstace判断是多种类型中的一种
print(isinstance(animal,(Animal,dict,list)))
# dir(object)获取对象的所有属性和方法,返回一个字符串列表[]
print(dir(dog))
print(dir("abc"))