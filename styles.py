from tkinter import ttk
import tkinter as tk

class AppStyle:
    # Main theme colors
    PRIMARY_COLOR = "#03363D"
    SECONDARY_COLOR = "#BDD9D7"
    ACCENT_COLOR = "#045C64"
    TEXT_COLOR = "#FFFFFF"
    
    @staticmethod
    def apply_style(root):
        style = ttk.Style()
        style.theme_use('clam')  # Use clam theme as base
        
        # Configure main window
        root.configure(bg=AppStyle.PRIMARY_COLOR)
        
        # Style for frames
        style.configure('Main.TFrame', background=AppStyle.PRIMARY_COLOR)
        style.configure('Secondary.TFrame', background=AppStyle.SECONDARY_COLOR)
        
        # Style for labels
        style.configure('Main.TLabel',
                       background=AppStyle.PRIMARY_COLOR,
                       foreground=AppStyle.TEXT_COLOR,
                       font=('Helvetica', 10))
        
        # Style for buttons
        style.configure('Custom.TButton',
                       background=AppStyle.ACCENT_COLOR,
                       foreground=AppStyle.TEXT_COLOR,
                       padding=10,
                       font=('Helvetica', 10, 'bold'))
        
        style.map('Custom.TButton',
                  background=[('active', AppStyle.SECONDARY_COLOR)],
                  foreground=[('active', AppStyle.PRIMARY_COLOR)])
        
        # Style for entry fields
        style.configure('Custom.TEntry',
                       fieldbackground=AppStyle.SECONDARY_COLOR,
                       padding=5)
        
        # Style for combobox
        style.configure('Custom.TCombobox',
                       fieldbackground=AppStyle.SECONDARY_COLOR,
                       padding=5)
        
        # Style for treeview (transaction list)
        style.configure('Custom.Treeview',
                       background=AppStyle.SECONDARY_COLOR,
                       fieldbackground=AppStyle.SECONDARY_COLOR,
                       foreground=AppStyle.PRIMARY_COLOR,
                       rowheight=25)
        
        style.configure('Custom.Treeview.Heading',
                       background=AppStyle.PRIMARY_COLOR,
                       foreground=AppStyle.TEXT_COLOR,
                       padding=5,
                       font=('Helvetica', 10, 'bold'))