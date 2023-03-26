# 函数 先定义再调用
"""
def 函数名(参数1,参数2,参数3，......)：
    '''
    文档描述
    '''
    函数体
    return 值
"""


# def func1():
#     print('my first function!')
# print(func1())
# print(func1)
# func1()

# a = 18
# def func2():
#     print('我是func2')
# def func1():
#     print(func2)
#     func2()
#     print('我是func1')
# func1()

# def func1(x, y):
#     print(x + y)
# func1(8, 6)

# def add(x, y):
#     res = x + y
#     # print(res)
#     return res
# s = add(24, 6)
# print(s)

# def func():
#     name = input('name>>>')
#     age = input('age>>>')
#     res = f'name:{name}, age:{age}'
#     return res
# res = func()
# print(res)

# def add(x, y):
#     res = x + y
#     return res
# s = add(add(6, 4), 5) * 2
# print(s)

# def func():
#     return 18, 'hang', True, [1, 2, 3]
# print(func(), type(func()))


# 定义函数阶段的参数：形式参数，简称形参
# def func1(x, y):
#     return x + y
# 掉用函数阶段传入的参数：实际参数，简称：实参
# func1(6, 8)

# 位置参数
# 位置形参：定义函数的时候，从左往右依次定义的形参  不能多也不能少
def func(x, y, z):
    print(x, y, z)

# 位置实参
# func(1, 2, 3)
# 关键字参数（关键字实参） 可以不按照顺序
# func(z=3, x=1, y=2)
# 位置实参与关键字实参混用  ！！！ 位置实参一定放在关键字实参之前
# func(1, 2, z=3)
