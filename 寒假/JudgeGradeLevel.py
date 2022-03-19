"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
score=int(input("请输入学生的成绩："))
if score<=100and score>=90:
    print("该学生的成绩等级为优！！！")
elif score<90and score>=80:
    print("该学生的成绩等级为良！！！")
elif score<80and score>=70:
    print("该学生的成绩等级为不错！！！")
elif score<70and score>=60:
    print("该学生的成绩等级为及格！！！")
elif score<60and score>=50:
    print("该学生的成绩等级为不及格，有挂科风险！！！")
elif score<50and score>=0:
    print("该学生的成绩等级为严重不及格，请提醒该学生重修此科！！！")
else:
    print("请输入正确的学生成绩！！！")