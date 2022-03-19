"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
score = {"张三": 100, '李四': 110, '王五': 119, '徐老六': 120}
keys = score.keys()
print(keys)
print(type(keys))
print(tuple(keys))
print('\n')
values = score.values()
print(values)
print(type(values))
print(tuple(values))
print('\n')
items = score.items()
print(items)
print(type(items))
print(tuple(items))
for i in score:
    print(i,score[i])
'''key可重复，但是values不可重复'''
score1 = {"zhangsan":100,"zhangsan":110}
score2 = {'zhangsan':120,'lisi':119}
print(score1)
print(score2)
print('\n')
'''当key数量和values不同时，以数量少的为基准'''
lst1 = ['张三','李四','王五']
lst2 = [666,777,888]
dictionary = {lst1:lst2 for lst1,lst2 in zip(lst1,lst2)}
print(dictionary)