"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
lst = ['Melbourne', 'ZhaoGe', 'XiAn', 'EdgeOfTheSky', 'CornerOfTheSea']
print(lst)
print(sorted(lst))  # 保留列表元素的排列顺序，同时以特定的顺序（按照字母顺序）呈现，不影响列表中的原始排列顺序
print(lst)
print(sorted(lst, reverse=True))  # 按照字母相反的顺序呈现，且不影响列表中的原始排列顺序
print(lst)
lst.reverse()  # 以相反的顺序打印列表（列表中的元素位置已与原来相反）
print(lst)
lst.reverse()  # 再次以相反的顺序改变列表元素的位置，则列表顺序与初始相同
print(lst)
lst.sort()  # 按照字母顺序排列列表中的元素
print(lst)
lst.sort(reverse=True)  # 按照字母相反的顺序排列列表中的元素
print(lst)
