# python的基本用法
print('hello python')  # 输出语句
print('//整除', 1 // 2)  # //是整除的意思
print('/运算结果为浮点数', 5 / 2)
print('%求余数', 10 % 3)
print('m**n,m的n次方', (-3) ** 4)  # -m**n 等价为-(m**n)
x = 9  # python的变量没有默认值，在使用的时候必须给变量赋值
print(x)

# input控制台输入语句
inputStr = input("请你输入你想要输入的：")
print(inputStr)

if 1 == 1 & 2 == 3:
    print("hahhaha")
else:
    print("heheheh")


name = input("what is your name ?")
print("hello ,"+name)
print("you can enter to exit !" )
input("Press <enter>")

print("""123""")

# 输出一只猫，使用的是Unicode编码输出的，前缀为\N
print("this is a \N{cat}")
 
