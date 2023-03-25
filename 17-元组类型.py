# 元组 不可变类型:索引所指向的内存地址 不可变
# t = (1, 1.2, 'abc', [4, 5, 6], {'a': 1, 'b': 'BBB'}, (7, 8, 9))
# print(t, type(t))
# t1 = ()
# print(t1, type(t1))
# t2 = (1,)
# t3 = (1)
# print(t2, type(t2), t3, type(t3))

x = (36, 'y', 1.68, ['a', 'b', 'c'])
# # x[1] = 'q'
# # print(x)
# x[3][1] = 'H'
# print(x)

# 类型转换
# print(tuple('韩愈柳宗元'))
# print(tuple(['1, 2, 3']))
# print(tuple({'a': 1, 'b': 'BBB'}))
# print(tuple(range(5)))

# 元组的内置方法
msg = ('金木','水','火','土')
# msg.