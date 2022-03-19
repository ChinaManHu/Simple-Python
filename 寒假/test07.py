"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
money = float(input("请输入顾客的消费金额："))
answer = input("该顾客是否会员？yes/no：")
if answer == 'yes':
    if (money >= 200):
        print("该顾客的应付金额为：", money * 0.8)
    elif (money >= 100):
        print("该顾客的应付金额为：", money * 0.9)
    elif (money > 0):
        print("该顾客的应付金额为：", money * 0.95)
    else:
        print("请输入正确的金额数目！！！")
elif answer == 'no':
    if (money >= 200):
        print("该顾客的应付金额为：", money * 0.9)
    elif (money >= 100):
        print("该顾客的应付金额为：", money * 0.95)
    elif (money > 0):
        print("该顾客的应付金额为：", money)
    else:
        print("请输入正确的金额数目！！！")
else:
    print("请选择相应的选项回答！！！")
