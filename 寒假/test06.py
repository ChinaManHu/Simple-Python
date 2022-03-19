"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
x=int(input("请输入您想要取出的金额："))
AccountBalance=9999
NewAccountBalance=AccountBalance-x
if AccountBalance>=x:
    print("取款成功，您现在的余额为：",NewAccountBalance)
else:
    print("您的余额不足，请重新输入取出的金额！！！")