from win32gui import *
import win32gui
import win32con
import win32api

windows = []
def get_windows(hwnd,param):
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd): # 用来过滤
        windows.append(GetWindowText(hwnd))  # 获得窗口标题
EnumWindows(get_windows, 0)
fzs=[]
for i in windows:
    #截取头部判断是否为游戏
    #topi=i[1:6]
    #if topi == "新天龙八部":
        fz = win32gui.FindWindow(None, i)
        fzs.append(fz)

print(fzs)