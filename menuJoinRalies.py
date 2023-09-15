import tkinter as tk
from tkinter import ttk


class joinRaliesMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.checkboxFilterBoss = None
        self.bossFillter = None
        self.filterBossVar = tk.IntVar(0)

        # Thư viện lưu boss 
        self.ymir_num = {'No ymir':0, 'Ymir-1':1, 'Ymir-2':2,'Ymir-3':3,'Ymir-4':4}
        self.bossnor_num = {'No bossnor':0, 'bossnor-1':1, 'bossnor-2':2,'bossnor-3':3,'bossnor-4':4}
        self.golem_num = {'No golem':0, 'golem-1':1, 'golem-2':2,'golem-3':3,'golem-4':4}
        self.cerberus_num = {'No cerberus':0, 'cerberus-1':1, 'cerberus-2':2,'cerberus-3':3,'cerberus-4':4}
        self.hydra_num = {'No hydra':0, 'hydra-1':1, 'hydra-2':2,'hydra-3':3,'hydra-4':4}
        self.bayard_num = {'No bayard':0, 'bayard-1':1, 'bayard-2':2,'bayard-3':3,'bayard-4':4}
        self.turtke_num = {'No turtke':0, 'turtke-1':1, 'turtke-2':2,'turtke-3':3,'turtke-4':4}
        self.pumpkin_num = {'No pumpkin':0, 'pumpkin-1':1, 'pumpkin-2':2,'pumpkin-3':3,'pumpkin-4':4}
        self.warlord_num = {'No warlord':0, 'warlord-1':1, 'warlord-2':2,'warlord-3':3,'warlord-4':4}
        self.witch_num = {'No witch':0, 'witch-1':1, 'witch-2':2,'witch-3':3,'witch-4':4}
        
        self.ymir = ('No ymir', 'Ymir-1', 'Ymir-2','Ymir-3','Ymir-4')
        self.bossnor = ('No bossnor', 'bossnor-1', 'bossnor-2','bossnor-3','bossnor-4')
        self.golem = ('No golem', 'golem-1', 'golem-2','golem-3','golem-4')
        self.cerberus= ('No cerberus', 'cerberus-1', 'cerberus-2','cerberus-3','cerberus-4')
        self.hydra = ('No hydra', 'hydra-1', 'hydra-2','hydra-3','hydra-4')
        self.bayard = ('No bayard', 'bayard-1', 'bayard-2','bayard-3','bayard-4')
        self.turtke = ('No turtke', 'turtke-1', 'turtke-2','turtke-3','turtke-4')
        self.pumpkin = ('No pumpkin', 'pumpkin-1', 'pumpkin-2','pumpkin-3','pumpkin-4')
        self.warlord = ('No warlord', 'warlord-1', 'warlord-2','warlord-3','warlord-4')
        self.witch = ('No witch', 'witch-1', 'witch-2','witch-3','witch-4')
        
        # Thông tin chọn boss
        self.levelymir=0
        self.levelbossnor= 0
        self.levelgolem= 0
        self.levelcerberus=0
        self.levelhydra= 0
        self.levelbayard= 0
        self.levelturtke= 0
        self.levelpumpkin= 0
        self.levelwarlord= 0
        self.levelwitch= 0
        
        self.joinRaliesGuild()

    def get_variables(self):
        return {
            'numberChamp': self.numberChamp.get(),
            'numberMeat': self.eatMeat.get(),
            'filterBossVar': self.filterBossVar.get(),
            'ymir_num': self.levelymir[0],
            'bossnor_num': self.levelbossnor[0],
            'golem_num': self.levelgolem[0],
            'cerberus_num': self.levelcerberus[0],
            'hydra_num': self.levelhydra[0],
            'bayard_num': self.levelbayard[0],
            'turtke_num': self.levelturtke[0],
            'pumpkin_num': self.levelpumpkin[0],
            'warlord_num': self.levelwarlord[0],
            'witch_num': self.levelwitch[0],
        }
        
    def joinRaliesGuild(self):
        self.tabJoinRalies = ttk.Frame(self.tabControl, style='My.TFrame')
        self.tabControl.add(self.tabJoinRalies, text='JoinRalies')

        self.framRallyChirld = tk.Frame(self.tabJoinRalies, bg="#CCFFFF")
        self.framRallyChirld.pack(pady=10)

        self.checkboxChampion = tk.Label(self.framRallyChirld, text="Join With Champion", bg="#CCFFFF")
        self.checkboxChampion.grid(row=0, column=0, pady=10,padx=10, sticky="w")

        self.numberChamp = tk.Entry(self.framRallyChirld, border=2, width=2)
        self.numberChamp.insert(0, "1")
        self.numberChamp.grid(row=0, column=1, pady=10, sticky="w")

        self.checkboxAutoMeat = tk.Label(self.framRallyChirld, text="Auto Meat", bg="#CCFFFF")
        self.checkboxAutoMeat.grid(row=0, column=3, pady=8, sticky="e")

        self.eatMeat = tk.Entry(self.framRallyChirld, border=2, width=2)
        self.eatMeat.insert(0, "5")
        self.eatMeat.grid(row=0, column=4, pady=10,padx=9, sticky="e")

        self.checkboxFilterBoss = tk.Checkbutton(self.framRallyChirld, text="Filter Boss",width=25, bg="#CCFFFF", variable=self.filterBossVar, command=self.on_checkbox_click)
        self.checkboxFilterBoss.grid(row=0, column=2, padx=20,pady=10, sticky="n")
        
        
        self.bossFillter = tk.Frame(self.tabJoinRalies, bg="#CCFFFF")
        
        select_ymir = ttk.Combobox(self.bossFillter, values=self.ymir)
        select_ymir.set('No ymir')
        select_ymir.grid(row=0, column=0, padx=10, pady=10)
        self.levelymir=self.onchange_box(select_ymir,self.ymir_num)
        
        select_bossnor = ttk.Combobox(self.bossFillter, values=self.bossnor)
        select_bossnor.set('No bossnor')
        select_bossnor.grid(row=0, column=1, padx=10, pady=10)
        self.levelbossnor=self.onchange_box(select_bossnor,self.bossnor_num)
        
        select_golem = ttk.Combobox(self.bossFillter, values=self.golem)
        select_golem.set('No golem')
        select_golem.grid(row=0, column=2, padx=10, pady=10)
        self.levelgolem=self.onchange_box(select_golem,self.golem_num)
        
        select_cerberus = ttk.Combobox(self.bossFillter, values=self.cerberus)
        select_cerberus.set('No cerberus')
        select_cerberus.grid(row=1, column=0, padx=10, pady=10)
        self.levelcerberus=self.onchange_box(select_cerberus,self.cerberus_num)
        
        select_hydra = ttk.Combobox(self.bossFillter, values=self.hydra)
        select_hydra.set('No hydra')
        select_hydra.grid(row=1, column=1, padx=10, pady=10)
        self.levelhydra=self.onchange_box(select_hydra,self.hydra_num)
        
        select_bayard = ttk.Combobox(self.bossFillter, values=self.bayard)
        select_bayard.set('No bayard')
        select_bayard.grid(row=1, column=2, padx=10, pady=10)
        self.levelbayard=self.onchange_box(select_bayard,self.bayard_num)
        
        select_turtke = ttk.Combobox(self.bossFillter, values=self.turtke)
        select_turtke.set('No turtke')
        select_turtke.grid(row=2, column=0, padx=10, pady=10)
        self.levelturtke=self.onchange_box(select_turtke,self.turtke_num)
        
        select_pumpkin = ttk.Combobox(self.bossFillter, values=self.pumpkin)
        select_pumpkin.set('No pumpkin')
        select_pumpkin.grid(row=2, column=1, padx=10, pady=10)
        self.levelpumpkin=self.onchange_box(select_pumpkin,self.pumpkin_num)
        
        select_warlord = ttk.Combobox(self.bossFillter, values=self.warlord)
        select_warlord.set('No warlord')
        select_warlord.grid(row=2, column=2, padx=10, pady=10)
        self.levelwarlord=self.onchange_box(select_warlord,self.warlord_num)
        
        select_witch = ttk.Combobox(self.bossFillter, values=self.witch)
        select_witch.set('No witch')
        select_witch.grid(row=3, column=0, padx=10, pady=10)
        self.levelwitch=self.onchange_box(select_witch,self.witch_num)
    
    # Cập nhật lại tab menu theo việc chọn acc
    def on_checkbox_click(self):
        if self.filterBossVar.get() == 0:
            self.bossFillter.pack_forget()
        else:
            self.bossFillter.pack(padx=0, pady=0)
    # Cập nhật thông chọn boss
    def onchange_box(self,box,bossNum):
        result = [0]  # Tạo một danh sách chứa giá trị trả về, sử dụng danh sách để truyền giá trị bằng tham chiếu
        def wrapper(event):
            result[0] = self.on_combobox_select(event, box, bossNum)
        box.bind("<<ComboboxSelected>>", wrapper)

        return result
    
    def on_combobox_select(self, event, boss, bossNum):
        selected_text = boss.get()
        return bossNum.get(selected_text)
        
        
