# text=input("请输入一个字符串 :")
# result = []
# for t in text:
#     result.append(ord(t))
# print ("字符串的 ASCII 为：", result)

# str_1 = input("请输入字符串：")
# n = 1
# if n< len(str_1):
#     n=n+1
#     for i in str_1:
#         m = str_1.count(' ')
# print("其中的单次总数是：{}个".format(m+1))   

# s=input('请输入一个字符串:\n')
# letters=0
# space=0
# digit=0
# others=0
# for c in s:
#     if c.isalpha():
#         letters+=1
#     elif c.isspace():
#         space+=1
#     elif c.isdigit():
#         digit+=1
#     else:
#         others+=1
# print('英文字母:%d 个,空格:%d 个,数字:%d 个,其他:%d 个'%(letters,space,digit,others))

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print(i,j,k,sep='', end=' ')
    print()