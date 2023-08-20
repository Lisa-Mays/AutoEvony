import tkinter as tk
from tkinter import ttk


class findBossMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.findBossGuild()
        
    def findBossGuild(self):
        self.tab_bossFinder = ttk.Frame(self. tabControl ,style='My.TFrame')
        self.tabControl.add( self.tab_bossFinder , text='Find Boss')
        
        