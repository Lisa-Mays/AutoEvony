import tkinter as tk


class saveFIle:
    def __init__(self,guilde) -> None:
        self.guilde=guilde
        
        self.start = []
        self.rally = []
        self.relic = []
        self.text_file_path = "Account.txt"
        self.directory_data = {
            'Acc': "0",
            'ip': '127.0.0.1',
            'port': '0',
            'doAuto': 1,
            'Champ': 1,
            'filter': 0,
            'meat': 5  
        }
        
    def addTab(self,start,rally,relic):
        self.start.append(start)
        self.rally.append(rally)
        self.relic.append(relic)
        
    def updateTab(self,start,rally,relic,index):
        try:
            self.start[index] = start
            self.rally[index] = rally
            self.relic[index] = relic
        except IndexError:
            return -1
        
    def upload(self):
        with open(self.text_file_path, 'w') as text_file:
            for key, value in self.directory_data.items():
                text_file.write("")
                
        for i in range(len(self.rally)):
            self.directory_data['Acc'] = i
            self.directory_data['ip'] = self.start[i].input_ip.get()
            if self.start[i].input_port.get() != "":
                self.directory_data['port'] = self.start[i].input_port.get()
            else:
                self.directory_data['port'] = 0
            self.directory_data['doAuto'] = self.start[i].doAuto
            self.directory_data['Champ'] = self.rally[i].numberChamp.get()
            self.directory_data['filter'] = self.rally[i].filterBossVar.get()
            self.directory_data['meat'] = self.rally[i].eatMeat.get()
            
            with open(self.text_file_path, 'a') as text_file:
                for key, value in self.directory_data.items():
                    text_file.write(f'{key}: {value}\n')
                text_file.write('\n')
                
    def loadfile(self):
        with open(self.text_file_path, 'r') as text_file:
            lines = text_file.readlines()
            
        for line in lines:
            line = line.strip()
            
            if line:
                key, value = line.split(': ', 1)
                
                self.directory_data[key] = value 

                if key == "Acc":
                    if self.directory_data["Acc"] != "0":
                        self.guilde.addAccount()
                        
            else:
                self.start[int(self.directory_data["Acc"])].input_ip.delete(0, tk.END)
                self.start[int(self.directory_data["Acc"])].input_ip.insert(0,self.directory_data["ip"])
                
                self.start[int(self.directory_data["Acc"])].input_port.delete(0, tk.END)
                self.start[int(self.directory_data["Acc"])].input_port.insert(0,self.directory_data["port"])
                    
                self.start[int(self.directory_data["Acc"])].selectWork(int(self.directory_data["doAuto"]))

                self.rally[int(self.directory_data["Acc"])].numberChamp.delete(0, tk.END)
                self.rally[int(self.directory_data["Acc"])].numberChamp.insert(0,self.directory_data["Champ"])

                self.rally[int(self.directory_data["Acc"])].filterBossVar.set(self.directory_data["filter"])
                self.rally[int(self.directory_data["Acc"])].on_checkbox_click()
            
                self.rally[int(self.directory_data["Acc"])].eatMeat.delete(0, tk.END)
                self.rally[int(self.directory_data["Acc"])].eatMeat.insert(0,self.directory_data["meat"])
                
    def RunAll(self):
        print("exit",self.guilde.existAccount)
        for i in range(self.guilde.existAccount+1):
            print(i)
            self.start[i].Start()