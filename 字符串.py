# c=input("请输入字符");
# A=""
# for  a in c[::2]:
#     A=A+a
# print(A)

# import string
# import random
# n_int=15
# letters_list = []
# while len(letters_list) < n_int :
#     a_str = string.ascii_letters
#     random_letter = random.choice(a_str)
#     if (random_letter not in letters_list) :
#         letters_list.append(random_letter)
#     else:
#         pass
# print(letters_list)

# import re
# text ='site sea sue sweet see case sse ssee loses'
# print(re.findall(r'\bs\S*?e\b',text))

import random
s = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"0","1","2","3","4","5","6","7","8","9","$","#","&","_","~"]
for i in range(15):
    for i in range(10):
        print (random.choice(s),end="")
    print("")