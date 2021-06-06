# -*- coding: utf-8 -*- 
# @Time : 2021/6/2 21:29 
# @Author : jarvis
# @email: 309194437@qq.com
# @File : wxPthon.py

import wx

import os
import glob
import shutil
import re

# 自定义窗口类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='照片修改工具', size=(400, 200))
        # 设置窗口居中
        self.Center()
        panel = wx.Panel(self)
        jpeg = wx.StaticText(panel, label='jpeg文件夹路径：', pos=(20, 15))
        cr2 = wx.StaticText(panel, label='cr2文件夹路径：', pos=(20, 50))
        self.tc1 = wx.TextCtrl(panel, pos=(130, 15))
        self.tc2 = wx.TextCtrl(panel, pos=(130, 50))
        b = wx.Button(panel, label='修改', pos=(20, 100))
        # 绑定按钮事件
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

    # 点击按钮事件方法
    def on_click(self, event):
        # 修改后的cr2格式文件保存路径，保存到当前脚本下的路径
        outDir = os.path.abspath('./outdir/')
        print(outDir)
        isExists = os.path.exists(outDir)
        # 判断文件夹是否存在
        if not isExists:
            os.makedirs(outDir)

        # 指定第一个文件夹的位置
        imageDir1 = self.tc1.GetValue()
        print(imageDir1)
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
        imageDir2 = self.tc2.GetValue()
        print(imageDir2)
        image2 = []
        imgname2 = []
        imageList2 = glob.glob(os.path.join(imageDir2, '*.cr2'))

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
                matchObj = re.match('[^\u4e00-\u9fa5]+', item1, re.I)  # 通过正则过滤中文，获取字母加数字的名称
                print(matchObj.group())
                if matchObj.group() == item2:
                    dir = imageList2[imgname2.index(item2)]
                    print(dir)
                    name = os.path.basename(dir)
                    shutil.copy(dir, outDir)
                    old_name = os.path.join(outDir, name)
                    new_item = item1 + '.cr2'
                    new_name = os.path.join(outDir, new_item)
                    os.rename(old_name, new_name)
        print("修改完毕")

class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    # 进入主循环事件
    app.MainLoop()
