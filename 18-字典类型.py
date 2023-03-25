# dic = {'aaa': 1, 2: 2, 3.1: 3, (4, 5, 6): 4}
# dict({'a': 'aaa', 'b': 'bbb'})
# print(dic, type(dic))
# print(dic['aaa'])
# print(dict(a=1, b=2, c=3))

keys = ['name', 'gender', 'age']
# dic={}
# for key in keys:
#     dic[key] = None
# print(dic)
# print({}.fromkeys(keys, None))

# 类型转换
# l = [('hello','world'),['age',18],['a','b']]
# print(dict(l))

# dic = {'a': 1, 'b': 2, 'c': 3}
# dic['d'] = 4
# print(dic)

# get取值
dic = {'a': 1, 'b': 2, 'c': 3}
# print(dic.get('a'))
# print(dic.get('d'))
# del dic['a']
# print(dic.get('a'))
# print(dic.pop('a'))
# print(dic.popitem())
# dic.clear()
# print(dic)

# print(len(dic))
# print('a' in dic)

# 字典内置方法
# keys
# print(dic.keys())
# for key in dic.keys():
#     print(key)
# # values
# print(dic.values())
# for value in dic.values():
#     print(key)
# # items
# print(dic.items())
# for key, value in dic.items():
#     print(key, value)
# print(dict(dic.items()))

# dic.update()
# hero = {'名字': '李白',
#         '职业': '刺客',
#         '移速': 550,
#         '攻速': 130}
# new = {'攻速': '120',
#        '技能1': '将进酒',
#        '技能2': '神来之笔',
#        '技能3': '青莲剑歌'}
# hero.update(new)
# print(hero)

# setdefault 设置默认值
info = {'name': '张大仙', 'age': 18}
info.setdefault('age')
info.setdefault('gender','保密')
print(info)