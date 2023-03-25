# 集合  主要用来去重以及做关系运算
# 只能存不可变类型
# s = {1, 2, 3, 's'}
# print(s)
# a = set()
# b = {}
# print(type(a), type(b))

# 关系运算
# hobbies1 = ['吃饭', '睡觉', '看书', '钢琴', '跳舞', '游泳', '旅行']
# hobbies2 = ['吃饭', '睡觉', '追剧', '打游戏']
# both_like = []
# for i in hobbies1:
#     if i in hobbies2:
#         both_like.append(i)
# print(both_like)
# h1 = set(hobbies1)
# h2 = set(hobbies2)
# print(type(h1), type(h2))

# & 取交集
# print(h1 & h2)
# h1.intersection(h2)

# 取并集  |
# print(h1 | h2)
# h1.union(h2)

# 取差集 -  h1中独有
# print(h1 - h2)
# h1.difference(h2)

# 对称差集  去除公共部分
# print((h1 - h2) | (h2 - h1))
# print(h1 ^ h2)
# h1.symmetric_difference(h2)

# 父子集  不存在包含关系可定位False
# s1 = {1, 2, 3}
# s2 = {1, 2}
# print(s1 > s2)


# 去重
hobbies1 = ['吃饭', '睡觉', '看书', '看书', '看书', '看书', '旅行']
print(set(hobbies1))

# info = [
#     ['张三', 18],
#     ['李四', 18],
#     ['张三', 18],
#     ['王五', 18],
#     ['王五', 18]
# ]
# new_info = []
# for i in info:
#     if i not in new_info:
#         new_info.append(i)
# print(new_info)

s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5}
# s.update([0, 5, 7, 8, 9])  # update传一个集合 或 其他可迭代对象
# print(s)
# print(s.intersection(s2))
# print(s)
# s = s.intersection(s2)
# s.pop()
# s.remove(4)
# print(s.discard(7))  # 若删除不存在的数 返回None
s.add(8)  # add只能传一个单独的值
s3 = {1, 2, 3}
s4 = {4, 5, 6}
# isdisjoint 集合交集为空  返回True
print(s3.isdisjoint(s4))
print(s)
