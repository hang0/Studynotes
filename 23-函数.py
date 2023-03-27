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
# 默认参数（默认形参） 在定义函数阶段 就为其赋予了默认值的形参
# 默认参数的值 实在函数定义阶段被赋值的
# a = 2
# def func(x, y=2):
#     print(x, y)
# a = 3
# func(1)
# def func(x, y, z):
#     print(x, y, z)

# 位置实参
# func(1, 2, 3)
# 关键字参数（关键字实参） 可以不按照顺序
# func(z=3, x=1, y=2)
# 位置实参与关键字实参混用  ！！！ 位置实参一定放在关键字实参之前
# func(1, 2, z=3)

# python里所有的值的传递 都是内存地址的传递 内存地址是对值的引用
# python里面所有的值的传递 都是引用传递

# def func(x, y, l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     l.append(y)
#     print(l)
# l2 = [3, 4, 5]
# func(1, 2, l2)

# 可变长度的参数 在调用函数的时候 传入的实参的个数是不固定的
# 可变长度的位置参数
# 用法 *形参名
# def func(x, y, *z):
#     print(x, y, z)  # z=(3,4,5)
# func(1, 2, 3, 4, 5)
# 求和
# def func(*args):
#     res = 0
#     for i in args:
#         res +=i
#     return res
# sum = func(1,2,3,4,5)
# print(sum)

# 可变长度的关键字参数
# 用法 **kwargs
# def func(x, y, **kwargs):
#     print(x, y, kwargs)  # {'a': 1, 'b': 2, 'c': 3, 'name': '行'}
# func(1, y=2, a=1, b=2, c=3, name='行')

# def func(x, y, z):
#     print(x, y, z)
# l = [1, 2, 3]
# func(*l)  # func(1,2,3)

# def func(x, y, *args):
#     print(x, y, args)
# # func(1, 2, *[3, 4, 5])
# func(*'愿疫情早点结束！')

# def func(x, y,**kwargs):
#     print(x, y, kwargs)
# func(**{'x': 1, 'y': 2, 'z': 3})  # func(x=1,y=2,z=3)

# 可变长参数混用
# **kwargs 必须在*args之后
# def func(*args,**kwargs):
#     print(args)
#     print(*args)
#     print(kwargs)
#     print(*kwargs)
# func(1, 2, a=1, b=2, c=3, name='行')
# def func1(x, y, z):
#     print('func1>>>', x, y, z)
# def func2(*args, **kwargs):  # args=(1,2) kwargs={'z'=3}
#     func1(*args, **kwargs)  # fun(1,2,z=3)
# # func(1,2,3)
# # func2(1, 2, z=3)

# 命名空间 namespace 和作用域
# 内置命名空间： python解释器内置的名字
# python解释器启动 就会创建内置名称空间
# python解释器关闭 就会销毁内置名称空间

# 全局命名空间 python文件(模块)内定义的变量名，包括函数名、类名、模块名
# 只要不是函数内部定义的名字、或是内置的名字，剩下的全都是全面命名空间的名字
# 全局命名空间会在python文件执行之前产生 python文件运行完毕后销毁

# 局部命名空间函数内部定义的名字，包括函数的参数
# 函数定义时产生 调用后销毁


# 名称空间的查找优先级
# 局部名称空间>全局名称空间>内置名称空间
# input = 1
# def func():
#     input = '张大仙'
#
# print(input)
#
# func()


# def func():
#     print(x)
#
#
# func()
# x = 10


# x = 10
# def func1():
#     print(x)
#
#
# def func2():
#     x = 20
#     func1()
#
#
# func2()


# input = 10
# def func1():
#     # input = 20
#     def func2():
#         # input = 30
#         print(input)
#
#     func2()
#     input = 20
#
#
# func1()


# 作用域
# 全局作用域：内置名称空间，全局名称空间
# 1、全局存活
# 2、全局有效
# z = 30
# def func1():
#     x = 10
#     print(z, id(z))
#
#
# def func2():
#     y = 20
#     print(z, id(z))
#
# print(z, id(z))
# func1()
# func2()


# 局部作用域：局部名称空间
# 1、临时存活
# 2、局部有效

# 内置：built-in
# 全局：global
# def func1(x):
#     # enclosing
#     def func2():
#         # enclosing
#         def func3():
#             # local
#             print(x)

# def func4():
#     print(x)


# LEGB
# B:built-in
# G:global
# E:enclosing
# L:local


# x = 10
# def func():
#     global x
#     x = 20
#
# func()
# print(x)


# l = [1,2,3]
# def func():
#     l.append(4)
#
# func()
# print(l)


# nonlocal
# x = 10
# def func1():
#     # x = 20
#     def func2():
#         nonlocal x
#         x = 30
#     print('调用func2之前的x：', x)
#     func2()
#     print('调用func2之后的x：', x)


# func1()
# print('全局的x', x)
