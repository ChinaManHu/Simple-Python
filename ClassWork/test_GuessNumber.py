"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
import random

count = 0
true_number = random.randint(1, 100)
while count < 5:
    real_number = int(input("请输入您猜想的数字："))
    if true_number == real_number:
        print("猜对了，您总共猜想了", count, "次！！！")
        break
    while true_number != real_number:
        if true_number > real_number:
            print("您猜想的数字偏小，请重新猜想！")
        elif true_number < real_number:
            print("您猜想的数字偏大，请重新猜想！")
        count += 1
        if count == 5 and real_number != true_number:
            print("您的可猜想次数已用玩，请重新启动游戏！")
        break
