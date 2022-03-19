"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
lst = ['牧寒','萧破军','龙傲天']
print("共进晚餐：",lst)
print(lst[1],'无法赴约')
lst[1]='萧天启'
print('共进晚餐：',lst)
lst.insert(0,'骨傲天')
lst.insert(2,'燕王')
lst.append('丁元英')
print('共进晚餐：',lst)
print(lst.pop(),'很遗憾，无法共进晚餐！')
print(lst.pop(),'很遗憾，无法共进晚餐！')
print(lst.pop(),'很遗憾，无法共进晚餐！')
print(lst.pop(),'很遗憾，无法共进晚餐！')
print(lst[0],lst[1],'共进晚餐')
'''
lst.clear()
print(lst)
del lst
print(lst)
'''
print('共邀请了以下人员共进晚餐：',lst)
print('共',len(lst),'人')
