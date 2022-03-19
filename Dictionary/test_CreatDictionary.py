"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
'字典的第一种创建方式'
score1 = {"张三": 100, '李四': 110, '王五': 119, '徐老六': 120}
for i in score1:
    print(i, score1[i])
'字典的第二种创建方式'
score2 = dict(name='jack', score=150)
print(score2)
print('jack的成绩为' + str(score2.get('score')))
'字典的第三种创建方式（空字典）'
score3 = {}
print(score3)

print('徐老六' in score1)
print("徐老六" not in score1)

score2.clear()
print(score2)

score2 = dict(name='jack', score=130)
score2['tom'] = 128
print(score2)

del score2['tom']
print(score2)
# del score2
# print(score2)
