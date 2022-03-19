"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
sum = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
for i in range(100, 999):
    num_2 = i // 100
    num_3 = i % 100 // 10
    num_4 = i % 100 % 10
    if i == num_2 ** 3 + num_3 ** 3 + num_4 ** 3:
        sum += i
        print(i)
print(sum)
