# 通过判断得到的布尔值或直接使用布尔值作为条件的布尔值称为  显示布尔值
# 所有的值都可以当成布尔值去用  显示布尔值
# 0 None 空（空字符串、空列表、字典）——>False
"""
if 条件:
    代码1
    代码2
    ...
"""

# is_human = input("你是不是个人，请输入是或者不是：")
# gender = input("请输入你的性别：")
# age = int(input("请输入你的年龄："))
#
# if is_human == "是" and gender == "女" and 16 <= age <= 20:
#     print("妙龄少女")
# else:
#     print("不是妙龄少女")
#
# print("hello")

# elif

"""
if 条件1:
    代码1
elif 条件2
    code2
elif 条件3:
    code3
...
else：
    coden

xxx
"""
grade = 1
if grade == 100:
    print("A")
elif 80 <= grade < 100:
    print("B")
elif 60 <= grade < 80:
    print("x")
else:
    print("不及格")
