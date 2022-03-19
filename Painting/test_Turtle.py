"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
import turtle

turtle.title("你也来一个？？？")  # 设置绘图窗口的标题信息
# 绘制一个红色填充的三角形
turtle.pensize(4)  # 设置画笔的粗细
turtle.penup()  # 抬起画笔，接下来画笔的移动不会留下痕迹
turtle.goto(-400, 300)  # 画笔移动到坐标位置（-400,300）
turtle.pendown()  # 落下画笔，接下来画笔的移动就会产生图形
turtle.begin_fill()  # 为填充封闭图形做好准备
turtle.color('red')  # 设置填充色为红色
turtle.circle(40, steps=3)  # 以40为半径，绘制一个被圆括住的三角形
turtle.end_fill()  # 填充结束
# 绘制一个没有颜色填充的圆
turtle.penup()
turtle.goto(-300, 300)  # 画笔位置定位到坐标位置（-300,300）处
turtle.pendown()
turtle.color('purple')
turtle.circle(40)  # 绘制以40为半径的圆
# 绘制一个蓝色填充的五边形
turtle.penup()
turtle.goto(-300, 300)  # 画笔定位到位置（-300,300）处
turtle.pendown()
turtle.begin_fill()  # 为填充封闭图形做好准备
turtle.color('blue')  # 设置填充色为蓝色
turtle.circle(40, steps=5)  # 以40为半径，绘制一个被圆括住的五边形
turtle.end_fill()  # 填充结束
# 输出文字
turtle.penup()
turtle.goto(-340, 260)  # 画笔定位到坐标位置（-340,260）处
turtle.pendown()
turtle.color('Magenta')  # 设置输出的字体颜色
turtle.write("世界上最好看的图形！！！", align="center", font=("微软雅黑", 18, "bold"))
turtle.hideturtle()  # 隐藏画笔箭头
turtle.done()
