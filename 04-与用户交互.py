# input会接受输入的值  任何值都会被保存为字符串
name = input("Please enter your name: ")
print(name, type(name))

age = input("Please enter your ages: ")
print(age, type(age))
age = int(age)  # int只能将纯数字的字符串转换为整型   小数也不行
print(age + 1, type(age))

