# 循环取值 （遍历）
# 列表、字典、字符串、元组、集合、...
'''
for 变量名 in 可迭代对象:
    子代码块
    ...
'''
l = ['张大仙', '张宏发', '张冰心', '张坦克']
# for a in l:
#     print(a, a[2])

# i = 0
# while i < 4:
#     print(l[i])
#     i += 1

# dic = {'name': "张大仙", 'age': 84, 'height': 150}
# for i in dic:
#     print(i)
#     print(dic[i])

# str1 = 'hello word'
# for i in str1:
#     print(i)
#     print(str1[0])

# for i in [1, 2, 3, 4, 5]:
#     # print(i)
#     print('aaa')

# range()
# for i in range(10): # 左闭右开 默认步长为1
#     print(i,"张大仙")

# for i in range(1, 10):
#     print('外层循环<==>', i)
#     for j in range(1, 10):
#         print('内层循环==>', j)

# print('你好啊\n') # \n 换行
# print('你好啊',end= '\t') # \t 制表符
# print('你好啊\n')
# 99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}x{i}={i * j}', end='\t')
    print()
