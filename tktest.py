from tkinter import *
mygui = Tk(className="歌曲查询系统")
text=Text(width=30,height=3)
text.pack()

btn=Button()
btn['text']='查询'
btn.pack()

mymenu=Menu()
mymenu.add_command(label="open")
mymenu.add_command(label="add")
mymenu.add_command(label="delete")
mygui.config(menu=mymenu)
mainloop()