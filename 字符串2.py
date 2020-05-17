# s=input("请输入字符串：")
# num=0
# for i in s:
#     if i in ['A','E','I','O','U' ,'a','e','i','o','u']:
#         num+=1
# print(num)

import re
x=["13915556234", "13025621456", "15325645124", "15202362459"]
for i in x:
    matchObj=re.match(r"13[4-9][0-9]{8}$|15[0, 1, 2, 8, 9][0-9]{8}$", i)
    if matchObj:
        print(i, " ：是移动号码")
    else:
        print(i, " ：不是移动号码")