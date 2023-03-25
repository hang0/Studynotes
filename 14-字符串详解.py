name = '张大仙'
# print(name,type(name))
# print(type(str(['aaa ','bbb'])))

# 索引取值
info = 'good good study,day day up!'
# print(info[0])
# print(info[4])
# print(info[-1])
# print(info[-2])
# 字符串是不可变类型  不能通过索引修改值

# 切片 左闭右开
# print(info[0:4])
# print(info[0:])
# print(info[:4])
# print(info[4:])
# print(info[:])
# print(info[0::2])
# print(info[0:4:-1]) # 从右往左取  步长为-1
# print(info[4:0:-1]) # 从右往左取  步长为-1

# strip 去除左右两端空格
# name = '   张 大 仙   '
# res = name.strip()
# print(res)
#
# name1 = '!!!   张大仙   !!!'
# res1 = name1.strip('!')
# print(res1)

# 登录案例
# input_username = input('请输入用户名: ').strip()
# input_pwd = input('请输入密码: ').strip()
# if input_username == 'hang' and input_pwd == 'hang1234':
#     print('登录成功！')
# else:
#     print('用户名或密码错误')


# split拆分
# names = '李白-韩信-露娜-孙悟空'
# res = names.split('-')
# print(res, type(res))
#
# res = names.split('-', 2)
# print(res, type(res))


# 长度len
# info = 'good good study,day day up!'
# longs = len(info)
# print(longs, type(longs))

# 成员运算in  not in

# 字符穿其他常见功能
# strip,lstrip,rstrip
# name = '   xing  '
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())

# split rsplit
# names = '李白-韩信-露娜-孙悟空'
# print(names.split('-',1))
# print(names.rsplit('-',1))

# lower upper
# msg = 'AbCd'
# print(msg.lower())
# print(msg.upper())

# startswith endswith
# print('君不见，黄河之水天上来，奔流到海不复回'.startswith('君不见'))
# print('君不见，黄河之水天上来，奔流到海不复回'.endswith('君不见'))

# join
# l1 = ['李白', '杜甫', '白居易', '陶渊明']
# res = '-'.join(l1)
# print(res, type(res))

# replace
# names = '李白-杜甫-白居易-陶渊明'
# print(names.replace('-','****'))
# print(names.replace('李白','诗仙'))
# print(names.replace('-','****',1))
# print(names)

# isdigit  判断字符串是否有纯数字组成
# print('84'.isdigit())
# print('84.5'.isdigit())
# print('84.a'.isdigit())
while 1:
    num = input('请输入你猜到数字：').strip()
    if num.isdigit():
        num = int(num)
    else:
        print('非法输入')
        continue
    if num > 36:
        print('猜大了')
    elif num < 36:
        print('猜小了')
    else:
        print('恭喜你猜对了！')
        break
