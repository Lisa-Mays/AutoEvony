import tkinter as tk
from tkinter import ttk


class killBossMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.killBossGuild()
        
    def killBossGuild(self):
        self.tab_bossKiller = ttk.Frame(self. tabControl ,style='My.TFrame')
        self.tabControl.add( self.tab_bossKiller , text='Kill Boss')
        
        