# 字符编码

# 一、计算机三大核心硬件
'''
CPU
    寄存器 告诉缓存器
内存
硬盘
'''

# 二、文本编辑器读取文件的三个步骤
# 1、启动文本编辑器
# 2、把文件内容从硬盘读入内存
# 3、把数据显示到屏幕上

# 三、运行python程序的步骤
"""
1、启动python解释器
2、把.py文件内容从硬盘读入到内存
3、把文件内容当成python语法识别

"""

# 字符编码发展史
"""
高电平 1
低电平 0

"""

# 通用标准
"""
1988 unicode
1989 usc
1990-1994 unicode(万国码)
1bit-->1位二进制数
8bit-->1Bytes(字节)
1KB = 1024Bytes
1MB = 1024KB
1GB = 1024MB 
1TB = 1024GB

电信运营商Mbps(兆比特每秒) 每秒传输的二进制位数的数量
下载速度 MBps(兆字节每秒) 每秒传输的字节数量
"""

# UTF-8
"""
编码：字符--编码-->unicode--编码-->UTF-8\GBK
解码：字符<--解码--unicode<--解码--UTF-8\GBK
"""

# 文件介绍
# open()
"""
一、控制问价你读写操作的模式
r:只读模式
w:只写模式   若文件已存在数据  会清空再写
a:只追加写模式  会在已有数据后再写
+: r+、w+、a+

二、控制文件读写内容的模式
t模式:
    读写都是以字符串（unicode）为单位的
    指定参数encoding= 'utf-8'
    只针对文本文件
b模式:
    bytes模式/二进制模式
    主要针对图片或者视频文件
    
"""

# 1、打开文件
# open('E:\\PythonNotes\\notes\\main.py')
# open('E:/PythonNotes/notes/main.py')
# f = open(r'E:\PythonNotes\notes\main.py', mode='rt', encoding='utf-8')
# print(f)
# 2、操作文件（读、写）
# res = f.read()
# print(res)

# 3、关闭文件
# f.close()

# with语法  上下文管理器

# with open('./main.py', mode='rt', encoding='utf-8') as f, \
#         open('./HelloPython.py', mode='rt', encoding='utf-8') as f2:
#     res = f.read()
#     print(res)
#     res2 = f2.read()
#     print(res2)

"""
t\b
r w a
rt wt at
"""
# rt 默认操作内容的模式
# with open('HelloPython.py', mode='rt', encoding='utf-8') as f:
#     # pass
#     print('第一次读'.center(80, '-'))
#     res1 = f.read()
#     print(res1)
#
#     print('第二次读'.center(80, '-'))
#     res2 = f.read()
#     print(res2)

# 登录程序优化
# username = 'hang'
# password = 'hang1234'

# with open('../data/user.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read()
#     username, password = res.split('---')
# if input_username == username and input_password == password:
#     print('登录成功！')
# else:
#     print('账号或密码错误')
# input_username = input('请输入账号>>>').strip()
# input_password = input('请输入密码>>>').strip()
# with open('../data/user.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         # print(line,end='')
#         username, password = line.strip().split('---')
#         # print(l)
#         if input_username == username and input_password == password:
#             print('登录成功！')
#             break
#     else:
#         print('账号或密码错误')


# wt模式
'''
若路径不存在目标文件  会新建一个   
若文件存在内容  w模式会清空原有内容
w 只写  打开文件会先清空内容   文件指针回到文件开头   多用于写新文件
'''
# with open('../data/c.txt', mode='w', encoding='utf-8') as f:
#     f.write('hello\n')
#     f.write('world')

# at 追加写
'''
文件不存在 则新建
文件存在  指针跳至末尾
多用于写旧文件  日志文件等
'''
# with open('../data/d.txt', mode='at', encoding='utf-8') as f:
#     # f.read() 不能读
#     f.write('\n行也思君坐也思君\n')
#     f.write('行也思君坐也思君\n')

# 注册
# input_username = input('请输入用户名>>>').strip()
# input_password = input('请输入密码>>>').strip()
# with open('../data/user.txt', mode='at', encoding='utf-8') as f:
#     f.write(f'{input_username}---{input_password}\n')

# 拷贝功能
# old_path = input('请输入旧路径的绝对路径：').strip()
# new_path = input('请输入新路径的绝对路径：').strip()
# with open(fr'{old_path}', mode='rt', encoding='utf-8') as f1, \
#         open(fr'{new_path}', mode='at', encoding='utf-8') as f2:
#     res = f1.read()
#     f2.write(res)

# +模式
# r+
# with open('../data/d.txt', mode='r+t', encoding='utf-8') as f:
#     # res = f.read()
#     # print(res)
#     f.write('python')
# w+ a+

# x模式
# 文件不存在就创建文件  文件存在就报错
# with open('../data/a.txt', mode='x', encoding='utf-8') as f:
#     # f.read()
#     f.write('x模式')


# b模式
'''
bytes模式/二进制模式
主要针对图片或者视频文件
'''

# with open('data/IMG63.jpg', mode='rb') as f:
#     res = f.read()
#     print(res)
#     print(type(res))

# with open('data/a.txt', mode='rb') as f:
#     res = f.read()
#     print(res, type(res))
#     print(res.decode('utf-8'))

# with open('data/b.txt', mode='wb') as f:
#     f.write('天下没有白吃的午餐'.encode('utf-8'))

# with open('data/IMG63.jpg', mode='rb') as f:
#     while 1:
#         res = f.read(1024)
#         print(res)
#         print(len(res))
#         if not res == 0:
#             break

# 拷贝功能
# old_path = input('请输入旧路径的绝对路径：').strip()
# new_path = input('请输入新路径的绝对路径：').strip()
# with open(fr'{old_path}', mode='rb') as f1, \
#         open(fr'{new_path}', mode='wb') as f2:
#     while 1:
#         res =f1.read(1024)
#         if not res:
#             break
#         f2.write(res)
# for line in f1:
#     f2.write(line)

# readline


# with open('data/a.txt', mode='rt', encoding='utf-8') as f:
# while True:
#     res = f.readline()
#     if not res:
#         break
#     print(res)

# writelines
# with open('data/i.txt', mode='wt', encoding='utf-8') as f:
#     f.writelines(['aaa\n', 'bbb\n', 'ccc\n'])

# bytes
# with open('data/j.txt', mode='wb') as f:
#     l = [b'aaa\n',
#          b'bbb\n',
#          b'ccc\n',
#          bytes('人', encoding='utf-8')]
#     f.writelines(l)
# print('人'.encode('utf-8'))
# print(bytes('人', encoding='utf-8'))

# with open('data/j.txt', mode='wt', encoding='utf-8') as f:
#     f.write('A')
#     # f.flush() 立即将数据写入硬盘
#     print(f.readable())  # readable() 判断文件是否可读
#     print(f.writable())  # writeagble() 判断文件是否可写
#     print(f.closed)  # closed 判断文件是否已关闭
#     print(f.encoding)  # 获取当前的编码方式 如果文件打卡模式为b  则没有属性
#     print(f.name)  # 获取当前文件名
# print(f.closed)


# 文件指针 pointer move
# f.seek(n,参照位置)  移动字节
'''
12字节   b模式满足一下三种模式
模式0 开头位置
f.seek(5,0) #5
f.seek(2,0) #2

模式1 当前位置   不能在t模式下使用
f.seek(5,1) #5
f.seek(2,1) #7

模式2 从末尾反向移动   不能在t模式下使用
f.seek(-5,2) #7
f.seek(-2,2) #10
'''
# with open('data/a.txt', mode='rb') as f:
#     f.seek(5, 0)
#     f.seek(3, 0)
#     print(f.tell())  # f.tell() 获取指针当前位置
#     res = f.read()
#     s = res.decode('utf-8')
#     print(s)

# tail
# with open('data/user.log',mode='at',encoding='utf-8')as f:
#     f.write('20230326---python学校\n')

# 文件修改
# 第一种修改文件的方式 文本编辑器修改文件
'''
with open('data/i.txt', mode='rt', encoding='utf-8') as f:
    res = f.read()
    # print(res)
    # l1 = list(res)
    # print(l1)
    # l1.insert(4, '不')
    # print(l1)
    # new_res = ''.join(l1)
    # print(new_res)
    new_res = res.replace('你好,我喜欢你', '你好,我不喜欢你')
    print(new_res)

with open('data/i.txt', mode='wt', encoding='utf-8') as f1:
    f1.write(new_res)
'''

# 第二种修改文件的方式
import os

with open('data/i.txt', mode='rt', encoding='utf-8') as f, \
        open('data/.i.txt.swap', mode='wt', encoding='utf-8') as f1:
    for line in f:
        res = line.replace('一天', '一年')
        f1.write(res)
os.remove('data/i.txt')
os.rename('data/.i.txt.swap', 'data/i.txt')
