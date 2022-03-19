"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
# 不用break
password = '666'
timeForTry = 1
word = input("请输入密码：")
if word == password:
    print("密码正确！！！")
else:
    while timeForTry < 3:
        print("密码错误，请重新输入！！！")
        word = input("请输入密码：")
        timeForTry += 1

# 用break
