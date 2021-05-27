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


read_file()
app = wx.App()
window = wx.Frame(None, title="PID=" + pid + "  FILE:" + file_name, size=(400, 300))
panel = wx.Panel(window)
menubar = wx.MenuBar()
fileMenu = wx.Menu()
fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
# window.Bind(wx.EVT_MENU, fitem)
window.Show(True)
app.MainLoop()

# class OS(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self, title="PID=" + pid + "  FILE:" + file_name, size=(400, 300))
#         self.icon = wx.Icon(name = '')
