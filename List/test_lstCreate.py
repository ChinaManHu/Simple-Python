"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
'''创建列表的第一种方法，使用[]'''
lst1 = ["潮圆信寂", 'list', 666, 8.0]
print(type(lst1))
print(id(lst1))
print(lst1)

'''创建列表的第二种方法，使用内置函数list()'''
lst2 = list(["天下", 'help', 888, 6.0, 'help'])
print(lst2[1])
print(lst2[-3])  # 列表元素也可以逆序输出，最后序号为-1，倒数第二个为-2，以此类推
print(type(lst2))
print(id(lst2))
print(lst2)
print(lst1.index("潮圆信寂"))
print(lst2.index('help', 1, 5))  # 当运用列表名.index函数在列表中查找指定元素的下标时，优先显示先查到的下标，且遵循左闭右开原则
print(lst2[1:5])
print(lst1[::2])
print(lst2[1::1])
for item1 in lst1:
    print(item1)
for item2 in lst2:
    print(item2)
for item3 in lst1:
    for item4 in lst2:
        print(item3,item4)
print('help' in lst2)    # help在列表中以字符串的形式出现，而下方代码的help为变量形式
print(help in lst2)