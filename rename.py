# -*- coding: utf-8 -*- 
# @Time : 2021/5/8 21:44 
# @Author : jarvis
# @email : 309194437@qq.com
# @File : rename.py

import os
# 1.输入文件名称，输入修改的中文名
# path = input("请输入文件夹地址：")
path = r'C:\Users\jarvis\Desktop\新建文件夹'
search_name = input("请输入待修改照片名字：")
alter_name = input("请输入模板名称（封面、照片墙等）：")
# 对目录下的文件进行遍历
for file in os.listdir(path):
# 按照输入的文件名搜索文件
    if file.split('.')[0] == search_name:
# 设置新文件名
        new_name = file.split('.')[0] + alter_name + file.split('.')[1]
# 重命名
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
# 结束
print("End")
