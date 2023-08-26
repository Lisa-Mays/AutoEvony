import tkinter as tk
from tkinter import ttk


class relicsMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.relicsGuild()
        
    def relicsGuild(self):
        self.tabRelics = ttk.Frame(self. tabControl ,style='My.TFrame')
        self.tabControl.add( self.tabRelics , text='Relics')
        
        