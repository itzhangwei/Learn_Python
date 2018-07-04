# 关于Python的字符串操作
from string import Template
import string

s = "hello ,%s.%s enough for ya?"
values = ('world', 'Hot')
print(s % values)
print('-' * 200)

tem1 = Template('Hello $who . $what enough for ya?')
s2 = tem1.substitute(who='Mars', what='dusty')
print(s2)
print('-' * 200)
print('' * 200)

# 使用{}站位:
s3 = '{},{} and {}'
s3 = s3.format('first', 'second', 'third')
print('使用{}站位: ' + s3)
print('-' * 200)
print('' * 200)

# 使用{索引}站位
s4 = '{0},{2} and {1}'
s4 = s4.format('first', 'second', 'third')
print("# 使用{索引}站位: " + s4)
print('-' * 200)
print('' * 200)

# 使用{key}占位
s4 = 'my name is {name},I am {age} year old ,I am very  {character}'
s4 = s4.format(name='joker', character='cute', age=24)
print("# 使用{key}站位: " + s4)
print('-' * 200)
print('' * 200)

# string.digits为数字（0~9字符串）
print(string.digits)
# string.ascii_letters 大小写英文字母字符串
print(string.ascii_letters)
# ASCII_uppercase 大写英文字母字符串
print(string.ascii_uppercase)
# ascii_lowercase 小写英文字母字符串
print(string.ascii_lowercase)
# punctuation 英文标点字符串
print(string.punctuation)
print('-' * 200)
print('' * 200)
# Python 中字符串常用的api

# center让字符串两边填充字符，使字符串居中
# 参数1：宽度，宽度要求是居中后的新的字符串长度，如果宽度没有原始宽度长，默认什么也不做
# 参数2：填充两边的的字符，默认是空格
print("center： 居中函数，参数1：宽度，宽度要求是居中后的新的字符串长度，如果宽度没有原始宽度长，默认什么也不做；参数2：用什么字符来填充宽度，默认是空格！")
st = "I am so handsome!"
print(st.center(50))
print(st.center(50, "*"))

print('-' * 200)
print('' * 200)

# find 函数查找字字符串函数在原始函数中出第一次现的索引位置，不存在就返回-1
# 参数sub：查找的字字符串
# 参数start:其实索引位置
# 参数end：终止索引位置,
# python 关于起始和终止索引一起时候用的时候都是包头不包尾
print("find 函数：查找字符串出现的第一次索引")
st = "my name is joker , I am 24 years old and very handsome! I like Python very mach!"
print(st.find('joker'))
print(st.find('I'))
print(st.find('I', 20))
print(st.find('I', 18, 20))

print('-' * 200)
print('' * 200)

# join函数：合并序列的元素,要求合并的元素都是字符串类型，否则报错
print("join函数：合并序列的元素,要求合并的元素都是字符串类型，否则报错")
seq = ['1', '2', '3', '4', '5']
st = '+'
# 以st为拼接符号，对中的每一个元素拼接。结果：1+2+3+4+5
print(st.join(seq))

print('-' * 200)
print('' * 200)

# lower 返回字符串小写的版本,和其相反的函数upper
print('lower 返回字符串小写的版本')
# 结果：2aaecf%^
print('2aAECf%^'.lower())
print('2aAECf%^'.upper())

print('-' * 200)
print('' * 200)



# replace替换函数
# 参数old：原始字符串
# 参数new: 需要替换成的新的字符串
# 参数count: 需要替换几个字符串，默认全部替换
print("replace替换函数 ")
# 结果：I am very cute，cute!
print("I am very handsome，handsome!".replace("handsome", "cute"))
# 结果：I am very cute，handsome!
print("I am very handsome，handsome!".replace("handsome", "cute", 1))

print('-' * 200)
print('' * 200)

# spilt 函数，字符串切割成一个序列，返回一个字符串序列
# sep :切割字符串，默认是空，返回原始字符串的序列
# maxsplit :切割过后序列存在的最大索引
print("spilt 函数，字符串切割成一个序列，返回一个序列")
# 结果：['1', '2', '3', '4', '5']
print("1+2+3+4+5".split("+"))
# 结果：['1', '2', '3+4+5']
print("1+2+3+4+5".split("+", 2))

print('-' * 200)
print('' * 200)

# strip()去除字符串收尾指定字符的函数,只能对字符串的首尾字符操作，中间的字符去除不了
# 参数chars：默认是空格，可传递其他的字符，当传入多个的时候是把字符切开一个一个去去除
print(" strip()去除字符串收尾指定字符的函数,只能对字符串的首尾字符操作，中间的字符去除不了")
st = " **!#s I'm * a * good boy  !#**sa  "
# 结果：**!#s I'm * a * good boy  !#**sa
print(st.strip())
# 去除首尾的空格、#、*、!、s、a这么多字符的，并不是把他们看做一个字符串的
# 结果：I'm * a * good boy
print(st.strip(" #*!sa"))
print("")
print('-' * 200)
print("")

# 结构：False
print("   1".isspace())
print("1234".isdigit())