arr_old = [10 , 23 , 35 , 46 , 57 , 68 , 79 , 80 , 92 , 103 ]
print("原始数组是：")
print(arr_old)
arr = int(input("请输入一个新的数："))
ind = 0
ans = arr_old.copy()
for i in range(0,len(arr_old)):
    if arr < arr_old [i]:
        ans.insert(i,arr)
        break
print("插入新数后的数组是：")
print(ans)

# num=input("请输入一个 5 位的数:")
# num2 = num[::-1]
# if(num == num2):
#     print("是一个回文数。")
# else:
#     print("不是一个回文数。")

# import math
# m = int(input("请输入一个正整数："))
# k = int(math.sqrt(m))
# flag = True
# i = 2
# while (i <= k and flag == True):
#     if (m % i == 0): flag = False
#     else: i += 1
# if (flag == True): print(m, "是素数！")
# else: print(m, "是合数！")


# for x in range(0,34):
#     for y in range(0,51):
#         for z in range(0,100):
#             if 3*x+2*y+z/2==100 and x+y+z==100:
#                    print("大马有",x,"匹,""中马有",y,"匹,""小马有",z,"匹")
