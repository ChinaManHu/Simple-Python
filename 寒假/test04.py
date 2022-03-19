"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
print(110)
print(0b110)
print(0o110)
print(0x110)
#代码结果均为十进制
num1=1.1
num2=2.2
num3=2.1
print(num1+num2)
print(num1+num3)

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

str1='潮圆信寂'
str2="潮圆信寂"
str3='''潮圆信寂'''
str4="""潮圆信寂"""
str5="'潮圆信寂'"
str6="""潮圆
        信寂"""
str7='''潮圆
信寂'''
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)
str8=99
print(float(str8))
#print(float(str1))报错