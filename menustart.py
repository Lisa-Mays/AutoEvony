import tkinter as tk
from tkinter import ttk
import resfreshPort as rf
import multiprocessing as mul
import autoJointRally as jr
from queue import Queue


class VaribleShare:
    def __init__(self) -> None:
        self.ip = ""
        self.port = ""
        self.starmenu = startMenu()
    def update(self,ip,port):
        self.ip = ip
        self.port = port
        
    def getip(self):
        return self.ip
    
    def getport(self):
        return self.port
    
    
class startMenu:
    def __init__(self,tabControl,buttonAccount,accHaveRun,number) -> None:
        self.tabControl = tabControl
        self.doAuto = 1
        self.mulRun = None
        self.buttonAccount = buttonAccount
        self.accHaveRun = accHaveRun
        self.statusRun = False
        self.buttonText = self.buttonAccount.cget("text")
        self.setingJointRally = None
        self.setingRelic = None
        self.number = number
        self.exitsMul = mul.Event()
        self.ip_port = mul.Array('i',[1,2])
        # Tạo một hàng đợi để truyền dữ liệu từ quy trình chính đến quy trình con
        
        self.startGuild()
    
    def setter(self,setingJointRally,setingRelic):
        self.setingJointRally = setingJointRally
        self.setingRelic = setingRelic
        
    def startGuild(self):
        self.tabStart = ttk.Frame(self.tabControl,style='My.TFrame')
        self.tabControl.add( self.tabStart, text='Start')
        
        label_ip = tk.Label(self.tabStart, text="Nhập Ip:",background= 'white')
        label_ip.place(x=10,y=10)
        self.input_ip = tk.Entry(self.tabStart ,border=2,width=21)
        self.input_ip.place(x=80,y=10)
        self.input_ip.insert(0, "127.0.0.1")
        
        label_port = tk.Label(self.tabStart , text="Nhập Port:",background= 'white')
        label_port.place(x=10,y=40)
        self.input_port = tk.Entry(self.tabStart ,border=2,width=21)
        self.input_port.place(x=80,y=40)
        
        self.autoJoinBoss=tk.Button(self.tabStart, text="JoinRalies",bg='blue',width=10,command=lambda num=1: self.selectWork(num))
        self.autoJoinBoss.place(x=400,y=10)
        
        self.autoMarket=tk.Button(self.tabStart, text="Market",bg='#E0E0E0',width=10,command=lambda num=2: self.selectWork(num))
        self.autoMarket.place(x=400,y=60)
        
        self.autoRelic=tk.Button(self.tabStart, text="Relic",bg='#E0E0E0',width=10,command=lambda num=3: self.selectWork(num))
        self.autoRelic.place(x=400,y=110)
        
        self.buttonStart = tk.Button(self.tabStart, text="Bắt Đầu",width=20,height=2,command=lambda: self.Start()) #3
        self.buttonStart.place(x=190,y=300)

    def selectWork(self,num):
        if num == 1:
            self.autoJoinBoss.config(bg='blue')
            self.autoMarket.config(bg='#E0E0E0')
            self.autoRelic.config(bg='#E0E0E0')
        elif num == 2:
            self.autoJoinBoss.config(bg='#E0E0E0')
            self.autoMarket.config(bg='blue')
            self.autoRelic.config(bg='#E0E0E0')
        elif num == 3:
            self.autoJoinBoss.config(bg='#E0E0E0')
            self.autoMarket.config(bg='#E0E0E0')
            self.autoRelic.config(bg='blue')
        self.doAuto = num
        
    def changeColorStart(self):
        if self.statusRun == False:
            self.buttonStart.config(bg='#F9F9F9',text="Start")
        elif self.statusRun == True:
            self.buttonStart.config(bg='#00B2BF',text="Stop")
            
    def Start(self): #3
        self.port = self.input_port.get()
        self.ip = self.input_ip.get()
        
        ip_parts = self.ip.split(".")
        # Chuyển đổi mỗi phần thành số nguyên
        ip_int_parts = [int(part) for part in ip_parts]
        # Kết hợp các số nguyên để tạo địa chỉ IP dạng số nguyên
        ip_int = (ip_int_parts[0] << 24) | (ip_int_parts[1] << 16) | (ip_int_parts[2] << 8) | ip_int_parts[3]


        with self.ip_port.get_lock():
            # Thay đổi giá trị của phần tử tại vị trí index 1 thành 42
            self.ip_port[0] = int(ip_int)
            self.ip_port[1] = int(self.port)
            
        get_port = rf.Resfresh_Port()
        portexsit = get_port.ResfreshPort()

        if self.statusRun == False:
            if self.port == '' or self.ip == '':
                self.buttonAccount.config(text="Error",bg="red")
                return
            else:
                check = 0 
                for account in portexsit:
                    if int(self.port) == account:
                        check += 1
                if check == 0:
                    self.buttonAccount.config(text="NOT EXIST",bg="red")
                    return
                    
                listPort = self.accHaveRun.return_Acc()
                for account in listPort:
                    if self.port == account:
                        self.buttonAccount.config(text="HAVE RUN",bg="red")
                        return
                    
                self.accHaveRun.updateAccByIndex(self.number,self.port)
                self.buttonAccount.config(text=f'{self.port}',bg="#00B2BF")
                self.statusRun = True
                self.changeColorStart()
                
            self.exitsMul.clear()
            if self.doAuto == 1:
                if self.mulRun is None:
                    self.mulRun = mul.Process(target=jr.AutoJointRally,args=(self.exitsMul, self.setingJointRally.get_variables(),self.ip_port))
                    self.mulRun.start()
            if self.doAuto == 2:
                print("sap ra")
            if self.doAuto == 3:
                print("sap ra")
                
        else:
            self.accHaveRun.updateAccByIndex(self.number,None)
            self.exitsMul.set()
            self.buttonAccount.config(text=f'{self.buttonText}',bg='#E0E0E0')
            self.statusRun = False
            self.changeColorStart()
            
        