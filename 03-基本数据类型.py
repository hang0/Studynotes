# 数字类型
# 整型
#  -1、0、1、2、3、1000、10000
age = 23
temperature = -1
print(type(age))
print(type(temperature))
# 浮点型float
price = 9.15
print(type(price))

level = 1
level = level + 1
print(level)
print(type(level))

a = 3
b = 1.5
c = a + b
d = -3
e = 3
print(c, type(c))
print(a / d, type(a / d))
print(d / a, type(d / a))
print(a / e, type(a / e))
print(age > 18)

# 字符串类型 str
'xxx'
"xxx"
'''xxx'''
"""xxx"""
quotes = """
人的差别在于业余时间，
而一个人的命运决定在晚上8点到10点之间。
因为一开始大家都在同一高度，做的工作一样，拿的薪水一样，
大部分人下班后想休息，然后一直刷视频、打游戏，这样得到了即时满足，很爽，但你最终就什么都没有得到。
但是如果你能每天把握住这两个小时好好学习，能够习惯延迟满足，每天进步1%，
那么一年后你将比现在的自己优秀3倍。
"""
print(type(quotes))
ages = '23'
print(type(ages))

a = 'my name is "陈书行"'
b = 'my name is \'陈书行\''
print(a)
print(b)
c = "my name is "
d = "陈书行"
print(c + d)  # 效率低 不建议这样使用
print('书行' * 5)  # 相当于该字符串打印了五遍
# print(a + age)  # 字符串和数字不能相加

hobbies = '吃饭、睡觉、打豆豆'

# 列表
#    0    1     2      3
l = [23, 3.5, '书行', ["aaa", "bbb"], 1, 5, 'c', 'd', 'a']
print(l)
print(l[1], l[2])
print(l[3][1])

hobbies = ['吃饭、睡觉、打豆豆']
print(hobbies[0])

person = [
    ['书行', 23, 170, ['吃饭', '睡觉', '打豆豆']],
    ['李白', 66, 175, ['挖仙草', '炼仙丹', '打豆豆']],
    ['韩信', 99, 180, ['打仗', '练剑']]
]
print(person[1][2])
print(person[2][3][1])

# 名字 年龄 身高 体重 薪资
person = ['张三', 23, 171, 144, 11000]

# 字典类型dict
dic = {
    "name": "hang",
    "age": 23,
    "height": 144,
    'salary': "11k"
}
print(type(dic))

print(dic['name'])
print(dic["salary"])
person = [
    {"name": '书行', "age": 23, "height": 170, 'hobbies': ['吃饭', '睡觉', '打豆豆']},
    {"name": '李白', "age": 66, "height": 175, 'hobbies': ['挖仙草', '炼仙丹', '打豆豆']},
    {"name": '韩信', "age": 99, "height": 180, 'hobbies': ['打仗', '练剑']}
]
print(person[0]['hobbies'][1])

# 布尔类型bool

a = True
b = False
print(type(a))
c = None
print(type(c))
#  0 None  空字符串'' 空列表[] 空字符串{} 都视为false

name = "hang"
ls = ["a", "b", name]  # 此处的name 相当于将 hang的内存地址
print(ls[2])
print(id(name))  # 直接引用
print(id(ls[2]))  # 间接引用

'''
a = 100
b = a
c = a
l = ['a', 'b', 'c', a]
在内存中
索引 ->  内存地址   ->  值   
 0     a的内存地址      a
 1     b的内存地址      b 
 2     c的内存地址      c
 a     值100的内存地址   100
'''

'''
name = 'hang'
ls = ['a', 'b', name]
name = '李白'
print(ls[2])

在内存中
索引 ->  内存地址   ->  值   
 0     a的内存地址      a
 1     b的内存地址      b 
 2     hang的内存地址   hang
name 最初绑定 hang
后来name 绑定 李白
但不管怎么改变 ls[2]都指向hang

'''
l1 = ['a', 'b']
l2 = ['x', 'y']
l1.append(l2)
# print(l1)
print(id(l2), id(l1[2]))
l2.append(l1)
print(l2)  # ['x', 'y', ['a', 'b', [...]]]
print(id(l1), id(l2[2]))  # 循环引用
del l1
del l2  # l1 l2 的直接引用全部解绑
"""
栈区     直接引用           堆区
                   *******************
l1       ------>   *内存地址0x00000001 *<-------------
                   *  0：'a'的内存地址  *             |
                   *  1：'b'的内存地址 *              |
                   *  2：l2的内存地址  *-----         |
                   *******************    |         |
                                          |间接引用  |
                   *******************    |         |
l2       ------>   *内存地址0x00000002 * <--         |
                   *  0：'a'的内存地址  *             |
                   *  1：'b'的内存地址 *              |
                   *  2：l1的内存地址  *--------------|
                   *******************      

栈区     直接引用           堆区
                   *******************
l1       ---x-->   *内存地址0x00000001 *<-------------
                   *  0：'a'的内存地址  *             |
del l1             *  1：'b'的内存地址 *              |
                   *  2：l2的内存地址  *-----         |
                   *******************    |         |
                                          |间接引用  |
                   *******************    |         |
l2       ---x-->   *内存地址0x00000002 * <--         |
                   *  0：'a'的内存地址  *             |
del l2             *  1：'b'的内存地址 *              |
                   *  2：l1的内存地址  *--------------|
                   *******************        
                   此时这内存泄漏       
标记清除   在python程序内存空间不够使用的时候 
          让整个程序暂停下来   扫描栈区
          把通过栈区所有能引用到的值（直接/间接）都标记为存活状态
          若发现通过栈区引用不到的值  都标记为死亡状态---会被直接清理迪掉 即使引用计数不为0

分代回收机制  权重达到设定值   检查频率降低
"""

name = 'hang'
"""
内存中存在两个区
栈区     直接引用           堆区
                   ******************
name       ->      *内存地址0x00000001 *
                   *     hang        *
                   *******************
当堆区的内存地址的引用计数为0时 被清除时 对应栈区的变量名也会被清除            
"""


