import tkinter as tk
from PIL import Image, ImageTk

class AppUI():
	def __init__(self):
		self.root = tk.Tk()
		self.x = 0
		self.y = 0
		self.init_ui()

	def init_ui(self):
		#self.root.overrideredirect(True) #去除边框
		#self.root.attributes("-alpha", 0) #整个窗口透明
		#self.root.iconbitmap('favicon.ico')  #设置窗口图标
		#self.root.attributes("-transparentcolor", "#CDCDB4")   # 将指定颜色变成透明颜色
		#self.root.wm_attributes('-topmost',1) #窗口置顶

		self.root.title("test")
		self.root.resizable(False, False) # 此调用方法会禁止根窗体改变大小

		scnWidth, scnHeight = self.root.maxsize() #获取屏幕的大小
		x, y = (scnWidth-1000)/2, (scnHeight-648)/2 #定位窗口居中显示的坐标

		self.root.geometry("1000x648+%d+%d" % (x,y)) #大小为1000x648,位置在(x,y)的主窗口

		self.canvas = tk.Canvas(self.root, width = 1000,height = 648)

		#bg = tk.PhotoImage(file='img.gif') #只支持gif格式
		bdgd = Image.open('imgs/bg.png')
		bg = ImageTk.PhotoImage(bdgd)
		self.canvas.create_image(500,324,image=bg)
		self.canvas.configure(highlightthickness = 0)
		self.canvas.bind("<B1-Motion>",self.move)
		self.canvas.bind("<Button-1>",self.button_1)

		self.canvas.pack()
		self.root.mainloop()

	def move(self, event):
		new_x = (event.x-self.x)+self.root.winfo_x()
		new_y = (event.y-self.y)+self.root.winfo_y()
		s = "1000x648+" + str(new_x)+"+" + str(new_y)
		self.root.geometry(s)
		
	def button_1(self, event):
		self.x, self.y = event.x,event.y
 
if __name__=='__main__': 
	AppUI()