# # 格式化字符串
# # 1、 %s   可以接受任意类型的值 都当成字符串填充   速度最慢
# info = 'My name is %s, I am from %s.' % ('hang', '四川')
# info1 = 'My name is %s, I am from %s.' % ('四川', 'hang')
# info2 = 'My name is %s' % 'hang'
# info3 = 'My name is %(name)s, I am from %(hometown)s.' % {'hometown': '四川', 'name': 'hang'}
# print(info)
# print(info1)
# print(info2)
# print(info3)
#
# # %d    只能接受整型
#
#
# # 2、format()  可以接受任意类型的值 都当成字符串填充
# info4 = 'My name is {}, I am from {}.'.format('hang', '四川')
# info5 = 'My name is {0}, I am from {1}.'.format('Xing', '广安')
# info6 = 'My name is {1}{0}, I am from {0}.'.format('Xing', '广安')
# print(info4)
# print(info5)
# print(info6)
#
# # 格式化填充
# # ****开始****
# a = '{0:*^10}'.format('开始')  # ^表示居中   <右填充    左填充>
# print(a)
#
# b = '{num:.2f}'.format(num=3.1415926)
# print(b)

# 3、 f   速度最快
name = input('请输入你的名字： ')
hometown = input("你来自哪里： ")
info = f'我的名字是{name}, 来自{hometown}'
print(info)


# 4、string-Template
