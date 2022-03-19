"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
'''集合的第一种创建方式'''
set1 = {1,3,5,7,9,7,5,3,1}
print(set1)    # 集合中的元素不可重复

'''集合的第二种创建方式'''
set2 = set(range(2,10,2))
print(set2)
set3 = set([1,2,3,4,5])
print(set3)
set4 = set((1,1,110))
print(set4)
print('\n')
tuple1 = (1,1,120)
print(tuple1)
set5 = set(tuple1)
print(set5)    # 元组的元素虽然不可变，但是在转化成集合后还是以集合显示
print(tuple1)
print('\n')
'''集合的增加和删除操作'''
set1.add(11)
print(set1)
set1.update([13,15])
print(set1)
set1.update((17,19))
print(set1)
print('\n')
set1.remove(19)
print(set1)
set1.discard(19)
set1.discard(17)
print(set1)
set1.pop()    # 此方法的删除元素为任意一个，不存在指定
print(set1)
set1.clear()
print(set1)
#del set1
#print(set1)