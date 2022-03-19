"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
'''第一种创建方式'''
# range(stop)
r1=range(10)
print(r1)
print(list(r1))
'''第二种创建方式'''
# range(start,stop)
r2=range(1,10)
print(r2)
print(list(r2))
'''第三种创建方式'''
# range(start,stop,step)
r3=range(1,10,2)
print(r3)
print(list(r3))
'''判断指定整数是否在序列中存在，（in，not in）'''
print(2 in r1)
print(2 in r3)
print(2 not in r1)
print(2 not in r3)