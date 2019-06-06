import tkinter
import tkinter.messagebox
import win32gui,win32con,win32api
from timeit import timeit
import win32gui,win32con,win32api




def funcwin():
    win32api.MessageBox(0, '随机', 'dfgdf', win32con.MB_OK)
    win32gui.PostMessage(win32lib.findWindow(None, 'dfgdf'), win32con.WM_CLOSE, 0, 0)
twin=timeit('funcwin()','from __main__ import funcwin',number=1)

def functk():
    tkinter.messagebox.showinfo('提示', '人生苦短')
    win32gui.PostMessage(win32lib.findWindow(None, '提示'), win32con.WM_CLOSE, 0, 0)
ttk=timeit('functk()','from __main__ import functk',number=1)

def funckey():
    win32gui.PostMessage(win32lib.findWindow(None, '360导航_一个主页，整个世界'), win32con.WM_CLOSE, 0, 0)
tkey=timeit('funckey()','from __main__ import funckey',number=1)

#
# def func():
#     s = 0
#     for i in range(1000):
#         s += i
#     print(s)
#
# # timeit(函数名_字符串，运行环境_字符串，number=运行次数)
# t = timeit('func()', 'from __main__ import func', number=1000)
print(twin,ttk,tkey)