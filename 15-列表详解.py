# msg = ['张大仙', 84, 1.88, False]
# print(type(msg))
#
# print(list('hello'))
# print(list({'A': 'aaa', 'B': 'bbb', 'C': 'ccc'}))

# 内置方法
# 唐代韩愈、柳宗元和宋代欧阳修、苏洵、苏轼、苏辙、王安石、曾巩八位
l1 = ['韩愈', '柳宗元', '欧阳修']
l2 = ['苏洵', '苏轼', '苏辙', '曾巩']

# 按索引取值
# print(l1[0], l1[-1])
# l1[1] = '史诗'

# 追加
# l1.append('苏洵')

# 插入
# print(l1)
# l1.insert(1, '王安石')

# ['韩愈', '王安石', '柳宗元', '欧阳修', ['苏洵', '苏轼', '苏辙', '曾巩']]
# l1.append(l2)

# ['韩愈', '王安石', ['苏洵', '苏轼', '苏辙', '曾巩'], '柳宗元', '欧阳修']
# l1.insert(2, l2)

# ['韩愈', '王安石', '柳宗元', '欧阳修', '苏洵', '苏轼', '苏辙', '曾巩']
# for i in l2:
#     l1.append(i)
# l1.extend(l2)
# l1 + l2

# 删除  del  pop remove
# 删除索引为1的值    ['韩愈', '柳宗元', '欧阳修']
# del l1[1]
# del l1
# print(l1)
# res = l1.pop(1)

# l1.remove('欧阳修')

# 切片
# print(l1[0:2])

# len()统计长度
# print(len(l1))

# 成员运算
# print('韩愈' in l1)

# 循环
# for i in l1:
#     print(i)

# 其他操作 count
# l3 = ['韩愈', '柳宗元', '欧阳修','韩愈', '柳宗元', '柳宗元','欧阳修']
# print(l3.count('柳宗元'))

# index
# print(l1.index('欧阳修'))

# reverse()
# print(l1)
# l1.reverse()
# print(l1)

# sort  默认从小到大
l4 = [11, 22, 55, 99, 66, 77, 88]
# l4.sort()
# l4.sort(reverse=True)  # 关键字参数 reverse=True  反转
# l5 = ['a', 's', 'd', 'f', 'g', 'h', 'j']
# l5.sort()
# print(l5)

# print('abcde' > 'abc')
# print('abcde' > 'abcg')
# print('abcde' > '110')
# print('abcde'>99)

