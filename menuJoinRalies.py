import tkinter as tk
from tkinter import ttk


class joinRaliesMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.joinRaliesGuild()
        
    def joinRaliesGuild(self):
        self.tab_joinRalies = (ttk.Frame(self.tabControl ,style='My.TFrame'))
        self.tabControl.add( self.tab_joinRalies , text='JoinRalies')
        
        