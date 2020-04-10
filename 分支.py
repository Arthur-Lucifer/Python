# a = float(input('输入三角形边长a: '))
# b = float(input('输入三角形边长b: '))
# c = float(input('输入三角形边长c: '))
# s = (a + b + c) / 2
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print("三角形三边分别为：a=%0.1f b=%0.1f c=%0.1f" %(a, b ,c))
# print('三角形面积为 %0.15f' %area)

# mark = int(input("请输入分数："))
# if (mark >= 90): grade = "优"
# elif (mark >= 80): grade = "良"
# elif (mark >= 70): grade = "中"
# elif (mark >= 60): grade = "及格"
# else: grade = "不及格"
# print(grade)

# x = int(input("请输入工资："))
# if (x <= 5000): y = 0
# elif (x <= 36000): y = (x - 5000) * 0.03
# elif (x <= 144000): y = (x - 5000) * 0.1 - 2520
# else: y = (x - 5000) * 0.2 - 16920
# print('%f' %y)

c = input("请输入字母：")
if (c == 'm'): week = "星期一"
elif (c == 'w'): week = "星期三"
elif (c == 'f'): week = "星期五"
elif (c == 't'): 
    c = input("请输入第二个字母：")
    if(c == 'u'): week = "星期二"
    elif (c == 'h'): week = "星期四"
elif (c == 's'): 
    c = input("请输入第二个字母：")
    if(c == 'a'): week = "星期六"
    elif (c == 'u'): week = "星期日"
print(week)