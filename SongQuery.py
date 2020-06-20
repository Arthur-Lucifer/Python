from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 20)

class Application(tk.Tk):
    def __init__(self):

        super().__init__()

        self.wm_title("歌曲查询系统")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #循环功能界面
        for F in (PageZero, PageOne, PageTwo, PageThree,PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(PageZero)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处


#主页面
class PageZero(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="歌曲查询系统", font=LARGE_FONT)
        label.pack(pady=100)
        label.pack(padx=100)
        ft2=tkFont.Font(size=16)
        Button(self, text="添加歌曲信息",font=ft2,command=lambda: root.show_frame(PageOne),width=30,height=2,fg='red',bg='black',activebackground='yellow',activeforeground='black').pack()
        Button(self, text="删除歌曲信息",font=ft2,command=lambda: root.show_frame(PageTwo),width=30,height=2,fg='yellow',bg='black',activebackground='yellow',activeforeground='black').pack()
        Button(self, text="修改歌曲信息",font=ft2,command=lambda: root.show_frame(PageThree),width=30,height=2,fg='green',bg='black',activebackground='yellow',activeforeground='black').pack()
        Button(self, text="查询歌曲信息",font=ft2,command=lambda: root.show_frame(PageFour),width=30,height=2,fg='blue',bg='black',activebackground='yellow',activeforeground='black').pack()
        Button(self, text='退出查询系统',height=2,font=ft2,width=30,command=root.destroy,fg='purple',bg='black',activebackground='yellow',activeforeground='black').pack()


#添加歌曲信息
#添加歌曲 歌曲名称、类型、曲目、作词、作曲、演唱、语言
#Song name, type, track, lyrics, composition, singing, language
class PageOne(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="添加歌曲信息", font=LARGE_FONT)
        label.pack(pady=110)
        label.pack(padx=100)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        Label(self,text='歌曲名称：',font=ft3).pack(side=TOP)
        global e1
        e1=StringVar()
        Entry(self,width=30,textvariable=e1,font=ft4,bg='Ivory').pack(side=TOP)
        Label(self,text='曲目类型：',font=ft3).pack(side=TOP)
        global e2
        e2=StringVar()
        Entry(self,width=30,textvariable=e2,font=ft4,bg='Ivory').pack(side=TOP)
        Label(self,text='作词人：',font=ft3).pack(side=TOP)
        global e3
        e3=StringVar()
        Entry(self, width=30, textvariable=e3, font=ft4, bg='Ivory').pack(side=TOP)
        Label(self, text='作曲人：', font=ft3).pack(side=TOP)
        global e4
        e4 = StringVar()
        Entry(self, width=30, textvariable=e4, font=ft4, bg='Ivory').pack(side=TOP)
        Label(self, text='演唱者：', font=ft3).pack(side=TOP)
        global e5
        e5 = StringVar()
        Entry(self,width=30,textvariable=e5,font=ft4,bg='Ivory').pack(side=TOP)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(PageZero)).pack(pady=20)
        Button(self, text="确定保存",width=8,font=ft4,command=self.save).pack(side=TOP)
#添加歌曲 歌曲名称、类型、曲目、作词、作曲、演唱、语言
#Song name, type, track, lyrics, composition, singing, language
    def save(self):
        with open('songdata.txt','a+') as songdata:
            name=str(e1.get())
            track=str(e2.get())
            lyrics=str(e3.get())
            composition=str(e4.get())
            singing=str(e5.get())
            songdata.write(name+' '+track+' '+lyrics+' '+composition + ' ' +singing+ '\n')
        songdata.close()

#删除歌曲信息
class PageTwo(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="删除歌曲信息", font=LARGE_FONT)
        label.pack(pady=100)
        label.pack(padx=100)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        Label(self,text='请输入你要删除的歌曲名称：',font=ft3).pack(side=TOP)
        global e6
        e6=StringVar()
        Entry(self,width=30,textvariable=e4,font=ft3,bg='Ivory').pack(side=TOP)
        Button(self, text="确定删除",width=8,font=ft4,command=self.del1).pack(pady=20)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(PageZero)).pack()
    def del1(self):
        de=str(e6.get())
        with open('songdata.txt','r') as f:
            lines=f.readlines()
            with open('songdata.txt','w') as f_w:
                for line in lines:
                    if de in line:
                        continue
                    f_w.write(line)
            f_w.close()


#修改歌曲信息
class PageThree(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        tk.Label(self, text="修改歌曲信息", font=LARGE_FONT).pack(pady=100,padx=100)

        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        Label(self,text='请输入你要修改的歌曲名称：',font=ft3).pack(side=TOP)
        self.e7=StringVar()
        Entry(self,width=30,textvariable=self.e7,font=ft3,bg='Ivory').pack(side=TOP)
        Label(self,text='曲目类型：',font=ft3).pack(side=TOP)
        self.e8=StringVar()
        Entry(self,width=30,textvariable=self.e8,font=ft3,bg='Ivory').pack(side=TOP)
        Label(self,text='作词人：',font=ft3).pack(side=TOP)
        self.e9 = StringVar()
        Entry(self, width=30, textvariable=self.e9, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='作曲人：', font=ft3).pack(side=TOP)
        self.e10 = StringVar()
        Entry(self, width=30, textvariable=self.e10, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='演唱者：', font=ft3).pack(side=TOP)
        self.e11=StringVar()
        Entry(self,width=30,textvariable=self.e11,font=ft3,bg='Ivory').pack(side=TOP)
        Button(self, text="确定修改",width=8,font=ft4,command=self.modify).pack(pady=20)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(PageZero)).pack()
    def modify(self):
        newname=str(self.e7.get())
        newtrack=str(self.e8.get())
        newlyrics=str(self.e9.get())
        newcomposition=str(self.e10.get())
        newsinging=str(self.e11.get())


        with open('songdata.txt','r') as r_w:
            lines1=r_w.readlines()
            with open('songdata.txt','w') as rr_w:
                for line1 in lines1:
                    if newname in line1:
                        rr_w.write(newname+' '+newtrack+' '+newlyrics+' '+newcomposition + ' ' +newsinging+ '\n')
                        continue
                    rr_w.write(line1)
            rr_w.close()

#查询歌曲
class PageFour(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="查询歌曲信息", font=LARGE_FONT)
        label.pack(pady=100)
        label.pack(padx=100)
        tree_data=ttk.Treeview()
        ft4=tkFont.Font(size=12)
        #滚动条

        scro=Scrollbar(self)
        scro.pack(side=RIGHT,fill=Y)
        lista=Listbox(self,yscrollcommand=scro.set,width=60)

        f=open('songdata.txt','r')
        text=("%-20s%-20s%-20s%-20s%-20s"%("歌名","类型","作词","作曲","演唱"))

        li=[]
        for i in f.readlines():
            j=i.split(' ')
            j[2]=j[2].replace('\n','')
            li.append(j)
            li.sort(key=lambda x:x[2],reverse=False)
            for i in li:
                text1=("%-18s%-18s%-18s%-18s%-18s"%(i[0],i[1],i[2],i[3],i[4]))
                lista.insert(0,text1)
            f.close()
            lista.insert(0,text)
            lista.pack()
            Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(PageZero)).pack(pady=40)


if __name__ == '__main__':
    # 实例化Application
    app = Application()

     # 主消息循环:
    app.mainloop()