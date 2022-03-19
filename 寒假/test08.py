"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
num_x = int(input("请输入第一个数："))
num_y = int(input("请输入第二个数："))
# 常规形式
"""
if num_x>=num_y:
    print(num_x,"大于等于",num_y)
else:
    print(num_x,"小于",num_y)
"""
# 条件表达式
print(str(num_x)+"大于等于"+str(num_y)   if num_x>=num_y else  str(num_x)+"小于"+str(num_y))