# -*- coding: utf-8 -*- 
# @Time : 2021/5/9 12:48 
# @Author : jarvis
# @email: 309194437@qq.com
# @File : autocompare.py

import os
import glob
import shutil

from PIL import Image
import re

# 修改后的crq格式文件保存路径，保存到当前脚本下的路径
outDir = os.path.abspath('E:/project/RenamePicture/outdir')
# print(outDir)
# 指定第一个文件夹的位置
imageDir1 = os.path.abspath('E:/project/RenamePicture/jpeg')

# 定义要处理的第一个文件夹变量
image1 = []  # image1指文件夹里的文件，包括文件后缀格式；
imgname1 = []  # imgname1指里面的文件名称，不包括文件后缀格式

# 通过glob.glob来获取第一个文件夹下，所有'.jpg'文件
imageList1 = glob.glob(os.path.join(imageDir1, '*.jpg'))
# print(imageList1)
# 遍历所有文件，获取文件名称（包括后缀）
for item in imageList1:
    image1.append(os.path.basename(item))

# 遍历文件名称，去除后缀，只保留名称
for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)
# print(image1)
# 对于第二个文件夹路径，做同样的操作
imageDir2 = os.path.abspath('E:/project/RenamePicture/cr2')
image2 = []
imgname2 = []
imageList2 = glob.glob(os.path.join(imageDir2, '*.psd'))

for item in imageList2:
    image2.append(os.path.basename(item))

for item in image2:
    (temp1, temp2) = os.path.splitext(item)
    imgname2.append(temp1)
# print(image2)
# 通过遍历，获取第一个文件夹下，文件名称的非中文部分（不包括后缀）与第二个文件夹相同的文件，并另存在outDir文件夹下。文件名称改成与第一个文件夹里的文件相同，后缀格式亦保持不变。
for item1 in imgname1:
    # print(item1)
    for item2 in imgname2:
        matchObj = re.match('[^\u4e00-\u9fa5]+',item1,re.I) #通过正则过滤中文，获取字母加数字的名称
        print(matchObj.group())
        if matchObj.group() == item2:
            dir = imageList2[imgname2.index(item2)]
            print(dir)
            name = os.path.basename(dir)
            shutil.copy(dir, outDir)
            old_name = os.path.join(outDir,name)
            new_item = item1 + '.psd'
            new_name = os.path.join(outDir,new_item)
            os.rename(old_name,new_name)
