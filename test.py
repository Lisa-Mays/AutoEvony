import threading
import tkinter as tk
from tkinter import ttk

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
        
        # Biến share toàn cục
        self.existAccount = 0
        
        self.doneGuild()
        
    def doneGuild(self):
        self.init_ui()
        self.left_frame()
        self.right_frame()
        # Gán biến đồng bộ True khi hoàn thành cài đặt ban đầu
        self.ready_to_show.set()
        # Xử lý sự kiện đóng cửa sổ
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def init_ui(self):
        self.root.geometry("1000x800")
        self.root.resizable(width=True, height=True)
        self.root.title("Evony Tool")
        
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"+{x}+{y}") # Cập nhạt lại vị trí, giao diện

    def left_frame(self):
        # Tạo frame trái
        self.frame_left = tk.Frame(self.root, bg='#F9F9F9')
        self.frame_left.pack(side='left', fill='y')
        
        # Nút nhấn cho frame trái
        tk.Button(self.frame_left, text='0', bg='white', fg='black', width=10, borderwidth=1, relief='ridge', command=lambda num=0:1).pack(pady=0.1)
        
        self.temp_controltab = 0
        self.newAcc = tk.Button(self.frame_left, text='+', bg='#E0E0E0', fg='black', width=10, borderwidth=1, relief='ridge', command=self.add_new_tab)
        self.newAcc.pack(pady=0)

    def add_new_tab(self):
        self.existAccount += 1
        new_tab_Start = ttk.Frame(self.tab_control, style='My.TFrame')
        self.tab_control.add(new_tab_Start, text=f'Account {self.existAccount}')
        
    def right_frame(self):
        # Tạo frame phải
        self.frame_right = tk.Frame(self.root, bg='#F9F9F9', borderwidth=1, relief='ridge')
        self.frame_right.pack(side='left', fill='both', expand=True)
        
        self.tab_control = ttk.Notebook(self.frame_right)
        
        self.tab_Start = ttk.Frame(self.tab_control,style='My.TFrame')
        self.tab_control.add(self.tab_Start, text='Bắt đầu')
        
        self.tab_control.pack(expand=1, fill='both', pady=1, padx=1)
        
    def on_closing(self):
        self.root.quit()

    def run(self):
        self.root.deiconify()  # Hiển thị cửa sổ sau khi đã sẵn sàng
        self.root.mainloop()

guide = Guide()
guide.run()
