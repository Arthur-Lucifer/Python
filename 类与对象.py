# class Circle:
#     radius = 0
#     def __init__(self,radius):
#         self.radius = radius
#     def CircleArea(self):
#         return self.radius**2*3.1415926
#     def CirclePerimeter(self):
#         return 2*3.1415926*self.radius
# for i in range (1,11):
#     c = Circle(i)
#     print("半径为",i,"的圆，",end='')
#     print('面积：',format(c.CircleArea(),'.2f'),end='')
#     print('周长：',format(c.CirclePerimeter(),'.2f'))

class Account:
    ID = 0
    balance = 0
    rate = 0
    def __init__(self,ID,balance,rate):
        self.ID = ID
        self.balance = balance
        self.rate = rate
    def Save(self,money):
        self.balance += money
    def Draw(self,money):
        self.balance -= money
        if self.balance < 0:
            return False
        return True
    def Print(self):
        print("账号：",self.ID,end=' ')
        print("余额：",self.balance,end=' ')
        print("年利率：",self.rate,end=' ')
        print("月利率：",self.rate/12,end=' ')
        print("月息：",self.rate/12*self.balance)
account = Account(998866,2000,0.045)
account.Print()
account.Save(150)
account.Print()
account.Draw(1500)
account.Print()