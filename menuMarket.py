import tkinter as tk
from tkinter import ttk


class marketMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.marketGuild()
        
    def marketGuild(self):
        self.tab_blackMarket = ttk.Frame(self. tabControl ,style='My.TFrame')
        self.tabControl.add( self.tab_blackMarket , text='Market')
        
        