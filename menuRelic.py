import tkinter as tk
from tkinter import ttk


class relicMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.relicGuild()
        
    def relicGuild(self):
        self.tab_blackMarket = ttk.Frame(self. tabControl ,style='My.TFrame')
        self.tabControl.add( self.tab_blackMarket , text='Relic')
        
        