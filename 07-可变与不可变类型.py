# 可变类型： 值改变的情况下， id不变，说明改的是原值
# 列表  字典
# 不可变类型： 值改变的情况下， id也变，说明原值没发生改变，而是开辟了新的内存空间存值并于变量绑定
# 字符串 整型 浮点型 布尔值类型

name = 'hang'
print(id(name))
name = 'chen'
print(id(name))

l1 = ['hang', 'chen']
print(id(l1[0]), id(l1[1]))
l1[0] = 'chen'
print(id(l1[0]), id(l1[1]))

# 建议使用字符串作为字典的key
dic = {10: 'a', 3.14: 'b', 'x': 'c', True: 'd'}
print(dic[10], dic[3.14], dic["x"], dic[True])
