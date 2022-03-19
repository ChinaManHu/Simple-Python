"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
set1 = {1,3,5,7,9}
set2 = {1,3,5,7,9}
set3 = {1,3,5,7,9,11}
set4 = {1,3,5,7,9,12}
print(set1==set2)    # 判断集合是否相同（判断的标准为集合的元素
print(set1.issubset(set3))    # 判断是否为子集
print(set1.issuperset(set2))    # 判断是否为超集（父集）
print(set3.issuperset(set1))
print(set1.issuperset(set3))
print(set1.isdisjoint(set4))    # 判断是否为交集，是则返回False，不是则返回True
print('\n')
set5 = {10,20,30,40,50}
set6 = {30,40,50,60,70}
print(set5.intersection(set6))    # 交集
print(set5 & set6)
print(set5.union(set6))    # 并集
print(set5 | set6)
print(set5.difference(set6))    # 差集
print(set5-set6)
print(set5.symmetric_difference(set6))    # 对称差集
print(set5^set6)
print('\n')
'''集合生成式'''
set7 = {i*i for i in range(1,10)}
print(set7)