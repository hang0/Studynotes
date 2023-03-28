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

# 变量名：指向的是变量值的内存地址
# 函数名：指向的是函数的内存地址
# def func():
#     print('我是func')
# # x = func
# # print(x, func)
# # x()
# def func2(x):
#     # print(x)
#     # x()
#     return x
# a = 10
# res = func2(func)    # func2(func的内存地址)   res拿到的是func的内存地址
# # print(res)
# res()

# def func():
#     print('我是func')
# l = [func]
# print(l[0])
# l[0]()
# d = {'k':func}
# print(d)
# d['k']()

# 电子钱包功能
# def login():
#     print('执行登录功能')
#
#
# def scan():
#     print("执行扫码支付功能")
#
#
# def transfer():
#     print("执行转账功能")
#
#
# def query():
#     print("执行查询余额功能")
#
#
# def recharge():
#     print("执行充值功能")


# func_dic = {
#     # '0': exit,
#     # '1': login,
#     # '2': scan,
#     # '3': transfer,
#     # '4': query,
#     # '5': recharge
#     '0': (None, '退出'),
#     '1': (login, '登录'),
#     '2': (scan, '扫码支付'),
#     '3': (transfer, '转账'),
#     '4': (query, '查询余额'),
#     '5': (recharge, '充值')
# }

# func_dic['1']()
# while True:
# print("""
# 0 退出
# 1 登录
# 2 扫码
# 3 转载
# 4 查询余额
# 5 充值
# """)
# for key in func_dic:
#     print(key, func_dic[key][1])
# opt = input('请输入功能编号>>>')
# if opt == '0':
#     break
# if opt == '1':
#     login()
# elif opt == '2':
#     scan()
# elif opt == '3':
#     transfer()
# elif opt == '4':
#     query()
# elif opt == '5':
#     recharge()
# else:
#     print('请按规则输入')
# if opt not in func_dic:
#     print("不存在")
#     continue
# func_dic[opt][0]()

# 闭包函数
# 闭函数：闭 封闭的意思 函数被封闭起来的
# 包函数：函数内部包含对 外层函数  作用域名字的引用
# def f1(x):
#     def f2():
#         print(x)
#     return f2
# res = f1(10)
# # print(res)
# x = 20
# res()
# f1()()

# 装饰器 不修改被装饰对象的源代码，也不修改调用方式的前提下，给被装饰对象添加新的功能
# 器： 器具 、 工具
# 装饰： 为其他事物添加额外的功能
# 定义一个函数 这个函数的功能就是用来装饰其他函数的
# 也就是说这个函数是用来给其他函数添加额外功能的
# 开放封闭原则
# 开放：对扩展功能（增加功能）开放，扩展功能的意思是在源代码不做任何改变的情况下，为其增加功能
# 封闭：对修改源代码是封闭的
import time


# 方案一：没有修改调用方式 但是修改了源代码
# def inside(group, s):
#     start = time.time()
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
#     end = time.time()
#     res = end -start
#     print(f"函数运行{res}秒")
#
# inside('红色',3)

# 方案二 没有修改源代码和调用方式 同时还加上了新的功能 但是有大量重复代码，代码冗余
# def inside(group, s):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')

# start = time.time()
# inside('红色', 3)
# end = time.time()
# print(f"函数运行{end-start}秒")

# 方案三：解决了方案二的代码冗余问题，也没有修改被装饰对象的源代码，同时还为其增加了新的功能
# 但是被装饰对象的调用方式被修改了
# def inside(group, s):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print('全军出击')
# def wrapper():
#     start = time.time()
#     inside('红色', 3)
#     end = time.time()
#     print(f"函数运行{end-start}秒")
# wrapper()

# # 方案四
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
# def wrapper(*args, **kwargs):
#     start = time.time()
#     inside(*args, **kwargs)
#     end = time.time()
#     print(f"函数运行{end - start}秒")
# wrapper('蓝色', 5, '全军')

# # 方案五
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
#
# print("原来的inside的内存地址>>>", inside)
#
#
# def outer(func):
#     # func = inside
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f"函数运行{end - start}秒")
#
#     return wrapper
#
#
# # res = outer(inside)
# # res('蓝色', 5, z='全军')
# inside = outer(inside)
# print("新的inside的内存地址>>>", inside)

# # 方案六
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
#
#
# def recharge(num):
#     for i in range(num, 101):
#         time.sleep(0.05)
#         print(f'\r当前电量:{">" * i}{i}%', end=' ')
#     print('\n电量已充满！！！')
#
#
# print("原来的inside的内存地址>>>", inside)
#
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f"函数运行{end - start}秒")
#
#     return wrapper
#
#
# # res = outer(inside)
# # res('蓝色', 5, z='全军')
# inside = outer(inside)
# print("新的inside的内存地址>>>", inside)
# inside('蓝色', 5, z='全军')
#
# recharge = outer(recharge)
# recharge(20)

# 方案7
# def inside(group, s, z):
#     print('欢迎来到王者荣耀')
#     print(f'你出生在{group}阵营')
#     print(f'敌军还有{s}秒到达战场')
#     time.sleep(s)
#     print(f'{z}出击')
# def recharge(num):
#     for i in range(num, 101):
#         time.sleep(0.05)
#         print(f'\r当前电量:{">" * i}{i}%', end=' ')
#     print('\n电量已充满！！！')
#     return 100
# print("原来的inside的内存地址>>>", inside)
# def outer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         response = func(*args, **kwargs)
#         end = time.time()
#         print(f"函数运行{end - start}秒")
#         return response
#     return wrapper
# res = outer(inside)
# res('蓝色', 5, z='全军')
# inside = outer(inside)
# print("新的inside的内存地址>>>", inside)
# inside('蓝色', 5, z='全军')
#
# recharge = outer(recharge)
# res = recharge(20)
# print(res)

# 语法糖

def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        response = func(*args, **kwargs)
        end = time.time()
        print(f"函数运行{end - start}秒")
        return response

    return wrapper


@count_time  # inside = outer(inside)
def recharge(num):
    for i in range(num, 101):
        time.sleep(0.05)
        print(f'\r当前电量:{">" * i}{i}%', end=' ')
    print('\n电量已充满！！！')
    return 100


@count_time  # recharge = outer(recharge)
def inside(group, s, z):
    print('欢迎来到王者荣耀')
    print(f'你出生在{group}阵营')
    print(f'敌军还有{s}秒到达战场')
    time.sleep(s)
    print(f'{z}出击')

inside('蓝色', 5, z='全军')
recharge(20)