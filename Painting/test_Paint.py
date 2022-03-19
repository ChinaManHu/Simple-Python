"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
# Python专业版才会显示效果图！！！
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
x_center, y_center, r = 320, 240, 100
x, y = [], []
for i in range(12):
    x.append(x_center + r * math.cos(30 * i * math.pi / 180))
    y.append(y_center + r * math.sin(30 * i * math.pi / 180))
for i in range(12):
    for j in range(12):
        canvas.create_line(x[i], y[i], x[j], y[j])
tk.mainloop()
