import os
song_list=[]
song_dict={}

#歌曲查询系统界面
def jiemian():
    print("---------------------------")
    print("      歌曲查询系统 V1.0")
    print("                           ")
    print("      1:添加歌曲"            )
    print("      2:删除歌曲"            )
    print("      3:修改歌曲"            )
    print("      4:查询歌曲"            )
    print("      5:显示所有"         )
    print("      6:保存数据"            )
    print("      7:退出系统"            )
    print("                           ")
    print("---------------------------")


#添加歌曲 歌曲名称、类型、曲目、作词、作曲、演唱、语言
#Song name, type, track, lyrics, composition, singing, language
def add():
    name=input("请输入录入歌曲名称:")
    form=input("请输入歌曲类型:")
    trac=input("请输入录入歌曲曲目:")
    lyri=input("请输入录入歌曲作词:")
    comp=input("请输入录入歌曲作曲:")
    sing=input("请输入录入歌曲演唱:")
    lang=input("请输入录入歌曲语言:")

    song_dict={"songname":name,"form":form,"track":trac,"lyrics":lyri,"composition":comp,"singing":sing,"language":lang}

    song_list.append(song_dict)
    print()
    print("-----添加歌曲信息界面-----")
    print()
    print("歌名\t\t","类型\t\t","曲目\t\t","作词\t\t","作曲\t\t","演唱\t\t","语言\t\t")
    for song_dict_t in song_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" %(song_dict_t["songname"],
                                                         song_dict_t["form"],
                                                         song_dict_t["track"],
                                                         song_dict_t["lyrics"],
                                                         song_dict_t["composition"],
                                                         song_dict_t["singing"],
                                                         song_dict_t["composition"],))
    print()
    print("录入成功!")
    print()

#删除歌曲
def dele():
    name_del=input("请输入想要删除的歌曲名称:")
    for song_dict_t in song_list:
        if name_del in song_dict_t["name"]:
            song_list.remove(song_dict_t)
            print()
            print("删除%s信息成功!" % name_del)
            print()
            break
    else:
        print()
        print("您输入的歌曲名称错误，请重新输入")
        print()
#修改学生
def updata():
    name_updata=input("请输入想要修改的歌曲名称:")
    for song_dict_t in song_list:
        if name_updata in song_dict_t["name"]:
            print()
            print("-----修改界面-----")
            print()
            print("歌名\t\t","类型\t\t","曲目\t\t","作词\t\t","作曲\t\t","演唱\t\t","语言\t\t")
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" %(song_dict_t["songname"],
                                                             song_dict_t["form"],
                                                             song_dict_t["track"],
                                                             song_dict_t["lyrics"],
                                                             song_dict_t["composition"],
                                                             song_dict_t["singing"],
                                                             song_dict_t["composition"],))
            #回车不修改
            song_dict_t["songname"]=new_input(song_dict_t["songname"],"请输入修改后的歌曲名称[回车不修改]:")
            song_dict_t["form"]=new_input(song_dict_t["form"],"请输入修改后的歌曲类型[回车不修改]:")
            song_dict_t["track"]=new_input(song_dict_t["track"],"请输入修改后的歌曲曲目[回车不修改]:")
            song_dict_t["lyrics"]=new_input(song_dict_t["lyrics"],"请输入修改后的歌曲作词[回车不修改]:")
            song_dict_t["composition"]=new_input(song_dict_t["composition"],"请输入修改后的歌曲作曲[回车不修改]:")
            song_dict_t["singing"]=new_input(song_dict_t["singing"],"请输入修改后的歌曲演唱[回车不修改]:")
            song_dict_t["composition"]=new_input(song_dict_t["composition"],"请输入修改后的歌曲语言[回车不修改]:")

            print()
            print("修改成功!")
            print()
            break
    else:
        print()
        print("您输入的歌曲名称错误，请重新输入")
        print()

#查找学生
def find():
    find_name=input("请输入需要查找的歌曲名称:")
    for song_dict_t in song_list:
        if find_name == song_dict_t["name"]:
            print()
            print("-----查询结果界面-----")
            print()
            print("歌名\t\t","类型\t\t","曲目\t\t","作词\t\t","作曲\t\t","演唱\t\t","语言\t\t")
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" %(song_dict_t["songname"],
                                                             song_dict_t["form"],
                                                             song_dict_t["track"],
                                                             song_dict_t["lyrics"],
                                                             song_dict_t["composition"],
                                                             song_dict_t["singing"],
                                                             song_dict_t["composition"],))
        else:
            print()
            print("-----查询结果界面-----")
            print()
            print("无此歌曲信息")

#显示所有学生信息
def showall():

    if len(song_list)>0:
        print()
        print("-----显示所有歌曲信息-----")
        print()
        print("歌名\t\t","类型\t\t","曲目\t\t","作词\t\t","作曲\t\t","演唱\t\t","语言\t\t")
        for song_dict_t in song_list:
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" %(song_dict_t["songname"],
                                                             song_dict_t["form"],
                                                             song_dict_t["track"],
                                                             song_dict_t["lyrics"],
                                                             song_dict_t["composition"],
                                                             song_dict_t["singing"],
                                                             song_dict_t["composition"],))
    else:
        print()
        print("暂无数据！")
        print()
# #设置用户不输入内容返回原值，输入内容返回新内容
# def new_input(yuanzhi,message):
#     input_str=input(message)

#     if len(input_str)>0:
#         return input_str
#     else:
#         return yuanzhi


#保存数据至文件中
def save_file():

    f = open("song.txt", 'w', encoding='utf-8')
    f.write(str(song_list))
    f.close()
    print("数据保存至song.txt文件成功！")


#将数据读取至变量中
def read_file():
    if os.path.exists('song.txt'):
        f = open('song.txt', 'r', encoding='utf-8')
        ret = f.read()
        global song_list
        song_list=eval(ret)
        f.close()
        print("数据读取成功!")


#歌曲查询系统
def song():
    while True:
        #调用界面函数
        jiemian()
        #调用读取文件函数
        read_file()
        x=input("请输入您的选择:")
        #添加歌曲
        if x=='1':
            add()
        #删除歌曲
        elif x=='2':
            dele()
        #修改歌曲
        elif x=='3':
            updata()
        #查询歌曲
        elif x=='4':
            find()
        #显示所有歌曲
        elif x=='5':
            showall()
        #保存数据至文件中
        elif x=='6':
            save_file()
        #退出歌曲查询系统
        elif x=='7':
            print()
            print("成功退出歌曲查询系统!")
            break
        else:
            print()
            print("输入错误，请重新输入")
            print()

#调用最先执行的登录界面函数
song()