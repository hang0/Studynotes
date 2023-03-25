# import time
#
# with open('data/user.log', mode='rb') as f:
#     # 控制文件指针调到末尾
#     f.seek(0, 2)
#     while True:
#         res = f.readline()
#         if res:
#             print(res.decode('utf-8'))
#         time.sleep(0.2)
