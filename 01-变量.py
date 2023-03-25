'''
变量
    先定义、后引用
'''
name = "hang"
print(name)
age = 23
print(age)

"""
垃圾回收机制 ：回收没有关联任何变量名的值
引用计数 ：统计值当前被引用的个数；若为0，则视为垃圾
"""

# 引用技术的增加   内存空间是同一块
a = 100
b = a
c = b
print(id(a))
print(id(b))
# 引用技术的减少
# del a
# 实际del的作用是解除变量名a与值100的绑定关系

'''
变量的三大组成部分
1、变量名
        变量名由英文字母、下划线_或数字组成，
        并且第一个字符必须是英文字母或下划线。
        变量名不能是 Python 关键字（又称关键词）。 
2、赋值符号 =
3、变量值
'''
# id 根据变量值的内存地址 所计算出的id号码  可理解为内存地址的映射
print(id(name))
# type
print(type(name))

'''
is与==的区别
is 用于辨别变量的id是否相同
== 用于辨别变量的值是否相同
'''
name1 = "书行"
name2 = "书行"
print(name1, name2)
print(id(name1), id(name2))  # 这里是因为pycharm做了优化  在cmd执行 id不同

print(name1 == name2)
print(name1 is name2)  # pycharm结果是相同的

"""
小整数池  -5~256
python解释器在启动的那一刻 申请一堆内存空间 创建小整数池
小整数池内的数被重复使用时  不会再重新申请新的内存空间
小整数也永远不会被垃圾回收机制回收
"""