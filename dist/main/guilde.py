import threading
import tkinter as tk
from tkinter import ttk
import menustart as mn
import menuJoinRalies as jr
import menuMarket as mk
import menuRelic as rl
import numpy as np
import resfreshPort as rf
import savefile as sf
class accHaveRun:
    def __init__(self):
        self.Accrun = []
    def addAccRun(self,account):
        self.Accrun.append(account)
    def updateAccByIndex(self, index, new_value):
        try:
            self.Accrun[index] = new_value
        except IndexError:
            return -1
    def return_Acc(self):
        return self.Accrun
        
class Guide:
    def __init__(self):
        # Tạo giao diện
        self.root = tk.Tk()
        self.root.withdraw()  # Ẩn cửa sổ tạm thời

        self.ready_to_show = threading.Event()  # Tạo biến đồng bộ
        self.style = ttk.Style()
        self.style.configure('My.TFrame', background='white')
        self.style.configure('My2.TFrame', background='#F9F9F9',borderwidth=1,relief='groove')
        self.style.configure('My3.TButton', background='blue',border=2)
        self.test=100
        # Biến share toàn cục
        self.accRun = accHaveRun()
        
        self.frame_left = None
        self.frame_right = None
        self.frame_right2 = None
        self.existAccount = 0 # Biến luu acc đang chạy
        self.temp_controltab = 0
        self.tabControl = []
        self.clickAcc = []
        self.newAcc = None
        self.accSave = sf.saveFIle(self)
        self.doneGuild()   

    def doneGuild(self):
        self.init_ui()
        self.callfFrame(self.existAccount)
        # Gán biến đồng bộ True khi hoàn thành cài đặt ban đầu
        self.ready_to_show.set()
        # Xử lý sự kiện đóng cửa sổ
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def callfFrame(self,number):
        self.left_frame(number)
        self.right_frame(number)
        
    def init_ui(self):
        self.root.geometry("800x400")
        self.root.resizable(width=False, height=False)
        self.root.title("Evony Tool")
        
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"+{x}+{y}") # Cập nhạt lại vị trí, giao diện
        
    def left_frame(self,number):
        if self.frame_left is None:
            self.frame_left = tk.Frame(self.root, bg='#F9F9F9')
            self.frame_left.pack(side='left', fill='y')

            self.canvas = tk.Canvas(self.frame_left, width=75)  # Đặt chiều cao cho Canvas
            self.canvas.pack(side='right', fill='both', expand=1)

            self.scrollbar = ttk.Scrollbar(self.frame_left, orient='vertical', command=self.canvas.yview)
            # self.scrollbar.pack(side='right', fill='y')

            self.canvas.config(yscrollcommand=self.scrollbar.set)

            self.scroll_frame = tk.Frame(self.canvas)
            self.canvas.create_window((0, 0), window=self.scroll_frame, anchor='nw')

            # Áp dụng sự kiện cuộn chuột cho canvas
            self.canvas.bind("<MouseWheel>", self.on_mousewheel)
            self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
            self.scrollbar.bind("<MouseWheel>", self.on_mousewheel)

        # Nút nhấn cho frame trái
        self.accRun.addAccRun(None)
        self.accSave.addTab(None,None,None)
        if number == 0:
            self.clickAcc.append(tk.Button(self.scroll_frame, text=f'{number}', bg='white', fg='black', width=10,borderwidth=1, relief='ridge',command=lambda num=number: self.checkClickAcc(num)))
            self.clickAcc[number].pack(pady=0.1)
        else:
            self.clickAcc.append(tk.Button(self.scroll_frame, text=f'{number}', bg='#E0E0E0', fg='black', width=10,borderwidth=1, relief='ridge',command=lambda num=number: self.checkClickAcc(num)))
            self.clickAcc[number].pack(pady=0.1)
        self.newAcc = tk.Button(self.scroll_frame, text='+', bg='#E0E0E0', fg='black', width=10, borderwidth=1, relief='ridge', command=self.addAccount)
        self.newAcc.pack(pady=0)

        self.scroll_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
    
    def get_inputs(self):
        get_port = rf.Resfresh_Port()
        a = get_port.ResfreshPort()
        self.listview.delete(*self.listview.get_children())
        if a != 0:
            a = list(a)
            a.sort()
            for i in a:
                self.listview.insert('', 'end', values=('Bluestack', f'{i}'))
                
    def list_view(self):
        self.listview = (ttk.Treeview(self.frame_right2, columns=('col1', 'col2'), show='headings',height=13))
        self.listview.heading('col1', text='EMULATOR')
        self.listview.heading('col2', text='PORT')

        self.listview.column('col1', width=100, minwidth=1)
        self.listview.column('col2', width=100, minwidth=1)
        
        self.listview.place(x=9,y=23)

        self.get_inputs()
        
    def right_frame(self,number):
        # Tạo frame phải
        if self.frame_right is None:
            self.frame_right = tk.Frame(self.root, bg='#F9F9F9', borderwidth=1, relief='ridge')
            self.frame_right.pack(side='left', fill='both', expand=0)
            
            self.frame_right2 = tk.Frame(self.root, bg='#CCFFFF', borderwidth=1, relief='ridge')
            self.frame_right2.pack(side='right', fill='both', expand=1)
            
            self.startAll=tk.Button(self.frame_right2, text="Start All",width=6,command=lambda:self.callRunAll())
            self.startAll.place(x=90,y=330)

            self.saveWork=tk.Button(self.frame_right2, text="Save",width=6,command=lambda:self.callSaveAcc())
            self.saveWork.place(x=9,y=365)
            
            self.loadWork=tk.Button(self.frame_right2, text="Load",command=lambda:self.callLoadAcc())
            self.loadWork.place(x=160,y=365)
            
            self.button_refresh = tk.Button(self.frame_right2 , text="Refresh") #1
            self.button_refresh.place(x=90,y=365)
            
            self.list_view()
        
        self.tabControl.append(ttk.Notebook(self.frame_right))
        
        # menu start
        mnstart = mn.startMenu(self.tabControl[number],self.clickAcc[number],self.accRun,number)

        #menu joinRalies
        mnrally = jr.joinRaliesMenu(self.tabControl[number])
    
        # menu relic
        mnrelic = rl.relicMenu(self.tabControl[number])
        
        # #menu market
        
        # mk.marketMenu(self.tabControl[number])
        # lấy giá chị chọn boss truyền vào startMenu
        mnstart.setter(mnrally,mnrelic)
        # Đóng acc save
        self.accSave.updateTab(mnstart,mnrally,mnrelic,number)
        if number == 0:
            self.tabControl[0].pack(expand=1, fill='both', pady=1, padx=1)
            
    def callSaveAcc(self):
        self.accSave.upload()
    def callLoadAcc(self):
        self.accSave.loadfile()
    def callRunAll(self):
        if self.startAll.cget("text") == "Start All":
            self.startAll.config(bg='#00B2BF',text="Stop All")
            self.accSave.RunAll()
        else:
            self.startAll.config(bg='SystemButtonFace',text="Start All")
            self.accSave.RunAll()
            
    def checkClickAcc(self,number):
        if self.temp_controltab != number:
            self.tabControl[self.temp_controltab].pack_forget()
            self.clickAcc[self.temp_controltab].config(bg='#E0E0E0')
            
            self.temp_controltab=number
            self.clickAcc[number].config(bg='white')
            self.tabControl[number].pack(expand=1, fill='both', pady=1, padx=1)
        
    def addAccount(self):
        self.existAccount+=1
        self.newAcc.destroy()
        self.callfFrame(self.existAccount)
        
    def on_closing(self):
        self.root.quit()
    
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def run(self):
        self.root.deiconify()  # Hiển thị cửa sổ sau khi đã sẵn sàng
        self.root.mainloop()

