"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
#单行注释
"""
多行注释
多行注释
多行注释
"""

"""
present=input("鲁智深的法号？")
print(present)
"""

#False,0,0.0,None,'',"",[],list(),(),tuple(),{},dict(),set()   （这些对象的bool值均为False，除此外均True）
print(bool(False))        #False
print(bool(0))            #False
print(bool(0.0))          #False
print(bool(None))         #False
print(bool(''))           #False
print(bool(""))           #False
print(bool([]))           #空列表
print(bool(list()))       #空列表
print(bool(()))           #空元组
print(bool(tuple()))      #空元组
print(bool({}))           #空字典
print(bool(dict()))       #空字典
print(bool(set()))        #空集合