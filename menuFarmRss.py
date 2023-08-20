import tkinter as tk
from tkinter import ttk


class farmRssMenu:
    def __init__(self,tabControl) -> None:
        self.tabControl = tabControl
        self.farmRssGuild()
        
    def farmRssGuild(self):
        self.tab_farmRss = ttk.Frame(self. tabControl ,style='My.TFrame')
        self.tabControl.add( self.tab_farmRss , text='Farm Rss')
        
        