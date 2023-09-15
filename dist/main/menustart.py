import tkinter as tk
from tkinter import ttk
import resfreshPort as rf
import multiprocessing as mul
import autoJointRally as jr
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
        port=self.input_port.get()
        ip=self.input_ip.get()
        get_port = rf.Resfresh_Port()
        portexsit = get_port.ResfreshPort()
        
        if self.statusRun == False:
            if port == '' or ip == '':
                self.buttonAccount.config(text="Error",bg="red")
                return
            else:
                check = 0 
                for account in portexsit:
                    if int(port) == account:
                        check += 1
                if check == 0:
                    self.buttonAccount.config(text="NOT EXIST",bg="red")
                    return
                    
                listPort = self.accHaveRun.return_Acc()
                for account in listPort:
                    if port == account:
                        self.buttonAccount.config(text="HAVE RUN",bg="red")
                        return
                    
                self.accHaveRun.updateAccByIndex(self.number,port)
                self.buttonAccount.config(text=f'{port}',bg="#00B2BF")
                self.statusRun = True
                self.changeColorStart()
                
            self.exitsMul.clear()
            if self.doAuto == 1:
                self.mulRun = mul.Process(target=jr.AutoJointRally, args=(self.exitsMul,self.setingJointRally.get_variables(),ip,port,))
                self.mulRun.start()
            if self.doAuto == 2:
                print("sap ra")
            if self.doAuto == 3:
                print("sap ra")
                
        else:
            self.accHaveRun.updateAccByIndex(self.number,None)
            self.exitsMul.set()
            if self.mulRun != None:
                self.mulRun.join()
            self.buttonAccount.config(text=f'{self.buttonText}',bg='#E0E0E0')
            self.statusRun = False
            self.changeColorStart()
