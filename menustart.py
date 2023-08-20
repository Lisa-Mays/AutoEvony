import tkinter as tk
from tkinter import ttk
import resfreshPort as rf

class startMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.startGuild()
        
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

        self.button_refresh = tk.Button(self.tabStart , text="Refresh",command=lambda :1)
        self.button_refresh.place(x=90,y=300)
        
        self.buttonJoinrally=tk.Button(self.tabStart, text="JoinRalies",bg='blue',width=10,command=lambda : 1)
        self.buttonJoinrally
        self.buttonJoinrally.place(x=400,y=10)
        
        self.buttonJoinrally=tk.Button(self.tabStart, text="FramRss",bg='#E0E0E0',width=10,command=lambda : 1)
        self.buttonJoinrally
        self.buttonJoinrally.place(x=400,y=60)
        
        self.buttonJoinrally=tk.Button(self.tabStart, text="Market",bg='#E0E0E0',width=10,command=lambda : 1)
        self.buttonJoinrally
        self.buttonJoinrally.place(x=400,y=110)
        
        self.buttonJoinrally=tk.Button(self.tabStart, text="KillBoss",bg='#E0E0E0',width=10,command=lambda : 1)
        self.buttonJoinrally
        self.buttonJoinrally.place(x=400,y=160)
        
        self.buttonJoinrally=tk.Button(self.tabStart, text="FindBoss",bg='#E0E0E0',width=10,command=lambda : 1)
        self.buttonJoinrally
        self.buttonJoinrally.place(x=400,y=210)
        
        self.buttonJoinrally=tk.Button(self.tabStart, text="Save",bg='#E0E0E0',width=10,command=lambda : 1)
        self.buttonJoinrally
        self.buttonJoinrally.place(x=400,y=260)
        
        self.buttonJoinrally=tk.Button(self.tabStart, text="Load",bg='#E0E0E0',width=10,command=lambda : 1)
        self.buttonJoinrally
        self.buttonJoinrally.place(x=400,y=310)
        
        self.buttonStart = tk.Button(self.tabStart, text="Start/Stop",width=20,height=2,command=lambda: 1)
        self.buttonStart.place(x=190,y=700)
        
        self.list_view()
        
    def list_view(self):
        self.listview = (ttk.Treeview(self.tabStart, columns=('col1', 'col2'), show='headings'))
        self.listview.heading('col1', text='EMULATOR')
        self.listview.heading('col2', text='PORT')

        self.listview.column('col1', width=100, minwidth=1)
        self.listview.column('col2', width=100, minwidth=1)
        
        self.listview.place(x=10,y=70)
        
        self.get_inputs()
    
    def get_inputs(self):
        get_port = rf.Resfresh_Port(1)
        a = get_port.ResfreshPort()
        self.listview.delete(*self.listview.get_children())
        if a != 0:
            for i in a:
                self.listview.insert('', 'end', values=('Bluestack', f'{i}'))
        # print(a)
    
    