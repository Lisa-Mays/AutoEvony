import tkinter as tk
from tkinter import ttk


class joinRaliesMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.joinRaliesGuild()
        
    def joinRaliesGuild(self):
        self.tabJoinRalies = ttk.Frame(self.tabControl, style='My.TFrame')
        self.tabControl.add(self.tabJoinRalies, text='JoinRalies')

        self.framRallyChirld = tk.Frame(self.tabJoinRalies, bg="white")
        self.framRallyChirld.pack(padx=10, pady=10)

        self.checkboxChampion = tk.Checkbutton(self.framRallyChirld, text="Join With Champion", bg="white")
        self.checkboxChampion.select()
        self.checkboxChampion.grid(row=0, column=0, pady=10, sticky="w")

        self.numChampion = tk.Entry(self.framRallyChirld, border=2, width=2)
        self.numChampion.insert(0, "1")
        self.numChampion.grid(row=0, column=1, pady=10, sticky="w")

        self.checkboxNoChampion = tk.Checkbutton(self.framRallyChirld, text="Join With No Champion", bg="white")
        self.checkboxNoChampion.grid(row=0, column=2, padx=20,pady=10, sticky="n")

        self.checkboxAutoMeat = tk.Checkbutton(self.framRallyChirld, text="Auto Meat", bg="white")
        self.checkboxAutoMeat.select()
        self.checkboxAutoMeat.grid(row=0, column=3, pady=10, sticky="e")

        self.eatMeat = tk.Entry(self.framRallyChirld, border=2, width=2)
        self.eatMeat.grid(row=0, column=4, pady=10, sticky="e")

        self.checkboxFilterBoss = tk.Checkbutton(self.framRallyChirld, text="Filter Boss", bg="white")
        self.checkboxFilterBoss.grid(row=2, column=2, pady=10, sticky="n")
        
        
        