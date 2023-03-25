'''
while 条件:
    子代码1
    子代码2
    子代码3
    ...
'''

# num = 0
# while num < 10:
#     print(num)
#     num += 1
# print("while 循环结束了")


# 死循环的效率问题

# while True:
#     info = input('请输入内容: ')
#     print(info)

# while 1:
#     10+10


# 退出while循环的两种方法

username = 'hang'
password = '123456'
err_count = 0
# condition = True
# while condition:
while err_count < 3:
    input_username = input('请输入用户名: ')
    input_password = input('请输入密码: ')
    if input_username == username and input_password == password:
        print('登录成功!')
        while True:
            action = input('请输入你的操作(enter Q to exit)：')
            if action == 'Q':
                break
            print(f'正在{action}')
        break  # 立即结束本层循环
        # condition = False
    else:
        print('用户名或密码错误，请重新输入。')
        err_count += 1
        # if err_count == 3:
        #     print('密码连续输入错误3次，账号已被锁定。')
        #     break
else:
    print('密码连续输入错误3次，账号已被锁定。')
print('退出了while循环。')

# while + continue
# num = 0
# while num <= 9:
#     if num == 4:
#         num += 1
#         continue
#     print(num)
#     num += 1

# while + else
'''
while True:
    ...
else:
    ...
'''
# num = 0
# while num <= 9:
#     if num == 4:
#         num += 1
#         # continue
#         break # 不会执行else
#     print(num)
#     num += 1
# else:
#     print('这里是else')
