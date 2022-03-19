"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
fp=open('D:/Python测试文件夹/a.txt','a+')
print('Hello, world!',file=fp)
fp.close
"""
已运行两次
"""
fq=open('D:/Python测试文件夹/x/b.txt','a+')
print('Hello, world!',file=fq)
fq.close
"""
已运行一次
"""