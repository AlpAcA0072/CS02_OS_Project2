#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

global pid, \
    file_name, \
    in_use_at_exit_bytes, \
    in_use_at_exit_blocks, \
    total_alloc, \
    total_free, \
    total_bytes, \
    peak_bytes, \
    leak_bytes, \
    leak_blocks


def read_file():
    global pid, \
        file_name, \
        in_use_at_exit_bytes, \
        in_use_at_exit_blocks, \
        total_alloc, \
        total_free, \
        total_bytes, \
        peak_bytes, \
        leak_bytes, \
        leak_blocks
    f = open('output', encoding='utf-8')
    [pid, file_name] = f.readline().strip().split(' ')
    [in_use_at_exit_bytes, in_use_at_exit_blocks] = f.readline().strip().split(' ')
    [total_alloc, total_free, total_bytes] = f.readline().strip().split(' ')
    peak_bytes = f.readline().strip()
    [leak_bytes, leak_blocks] = f.readline().strip().split(' ')


#
# read_file()
# app = wx.App()
# window = wx.Frame(None, title="PID=" + pid + "  FILE:" + file_name, size=(400, 300))
# panel = wx.Panel(window)
# # window.Bind(wx.EVT_MENU, fitem)
# window.Show(True)
# app.MainLoop()

def menuHandler(event):
    id_event = event.GetId()
    if id_event == wx.ID_NEW:
        print("NEW")
    if id_event == wx.ID_EXIT:
        exit(0)


class OS(wx.Frame):
    def __init__(self, parent, title):
        super(OS, self).__init__(parent, title=title)
        self.InitUI()

    def InitUI(self):
        menuBar = wx.MenuBar()

        # 创建一个菜单 1
        fileMenu = wx.Menu()

        # 创建一个菜单项 1-1
        newItem = wx.MenuItem(fileMenu, id=wx.ID_NEW, text='New', kind=wx.ITEM_NORMAL)
        fileMenu.Append(newItem)

        # 添加一行线
        fileMenu.AppendSeparator()

        # 创建一个子菜单 1-2
        editMenu = wx.Menu()

        # 创建三个子菜单的菜单项目 1-2-1 and 1-2-2 and 1-2-3
        cutItem = wx.MenuItem(editMenu, id=122, text="Cut", kind=wx.ITEM_NORMAL)
        copyItem = wx.MenuItem(editMenu, id=121, text="Copy", kind=wx.ITEM_NORMAL)
        pasteItem = wx.MenuItem(editMenu, id=123, text="Paste", kind=wx.ITEM_NORMAL)
        editMenu.Append(copyItem)
        editMenu.Append(cutItem)
        editMenu.Append(pasteItem)

        # 把子菜单 1-2 添加到菜单 1 中
        fileMenu.Append(wx.ID_ANY, "Edit", editMenu)

        # 添加一行线
        fileMenu.AppendSeparator()

        # 添加两个单选框 1-3 and 1-4
        radio1 = wx.MenuItem(fileMenu, id=13, text="Radio_One", kind=wx.ITEM_RADIO)
        radio2 = wx.MenuItem(fileMenu, id=14, text="Radio_Two", kind=wx.ITEM_RADIO)
        fileMenu.Append(radio1)
        fileMenu.Append(radio2)
        # PS.单选框 只在自己区域之间（两行线之间） 相互作用

        # 添加一行线
        fileMenu.AppendSeparator()

        # 添加一个 可选中 的菜单项 1-5
        fileMenu.AppendCheckItem(id=15, item="Check")

        # 添加一个 菜单项 1-6 并注册快捷键
        quitItem = wx.MenuItem(fileMenu, id=wx.ID_EXIT, text="Quit\tCtrl+Q", kind=wx.ITEM_NORMAL)
        fileMenu.Append(quitItem)

        # 将 fileMenu 菜单添加到菜单栏中
        menuBar.Append(fileMenu, title='File')

        # 设置窗口框架的菜单栏为 menuBar
        self.SetMenuBar(menuBar)

        # 绑定事件处理
        self.Bind(wx.EVT_MENU, menuHandler)

        # 让其在屏幕中间打开调整大小展示
        self.SetSize((300, 400))
        self.Centre()
        self.Show()


if __name__ == "__main__":
    ex = wx.App()
    OS(None, 'Menu - Test')
    ex.MainLoop()
