import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from styles import AppStyle

class FinanceGUI:
    def __init__(self, finance_tracker):
        self.tracker = finance_tracker
        self.root = tk.Tk()
        self.root.title("Finance Tracker")
        self.root.geometry("900x700")
        self.root.configure(bg=AppStyle.PRIMARY_COLOR)
        
        AppStyle.apply_style(self.root)
        self.setup_title()
        self.setup_gui()

    def setup_title(self):
        title_frame = ttk.Frame(self.root, style='Main.TFrame')
        title_frame.pack(fill='x', pady=20)
        
        self.title_label = ttk.Label(title_frame, 
                                   text="Finance Tracker", 
                                   style='Main.TLabel',
                                   font=('Helvetica', 24, 'bold'))
        self.title_label.pack()
        self.animate_title()

    def animate_title(self):
        colors = [AppStyle.SECONDARY_COLOR, AppStyle.TEXT_COLOR]
        self.current_color_index = 0
        
        def change_color():
            self.current_color_index = (self.current_color_index + 1) % len(colors)
            self.title_label.configure(foreground=colors[self.current_color_index])
            self.root.after(1500, change_color)
        
        change_color()

    def setup_gui(self):
        style = ttk.Style()
        style.configure('Custom.TNotebook', background=AppStyle.PRIMARY_COLOR)
        style.configure('Custom.TNotebook.Tab', 
                       background=AppStyle.SECONDARY_COLOR,
                       foreground=AppStyle.PRIMARY_COLOR,
                       padding=[20, 10],
                       font=('Helvetica', 10, 'bold'))
        
        notebook = ttk.Notebook(self.root, style='Custom.TNotebook')
        notebook.pack(pady=10, expand=True, fill='both', padx=20)

        transactions_frame = ttk.Frame(notebook, style='Secondary.TFrame')
        categories_frame = ttk.Frame(notebook, style='Secondary.TFrame')
        analysis_frame = ttk.Frame(notebook, style='Secondary.TFrame')

        notebook.add(transactions_frame, text="Transactions")
        notebook.add(categories_frame, text="Categories")
        notebook.add(analysis_frame, text="Analysis")

        self.setup_transactions_tab(transactions_frame)
        self.setup_categories_tab(categories_frame)
        self.setup_analysis_tab(analysis_frame)

    def setup_transactions_tab(self, parent):
        input_frame = ttk.LabelFrame(parent, text="Add Transaction", style='Secondary.TFrame')
        input_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(input_frame, text="Type:", style='Main.TLabel').grid(row=0, column=0, pady=5, padx=5)
        self.trans_type = ttk.Combobox(input_frame, values=["Income", "Expense"], style='Custom.TCombobox')
        self.trans_type.grid(row=0, column=1, pady=5, padx=5)
        self.trans_type.bind("<<ComboboxSelected>>", self.update_categories)

        ttk.Label(input_frame, text="Category:", style='Main.TLabel').grid(row=1, column=0, pady=5, padx=5)
        self.category = ttk.Combobox(input_frame, style='Custom.TCombobox')
        self.category.grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(input_frame, text="Amount:", style='Main.TLabel').grid(row=2, column=0, pady=5, padx=5)
        self.amount = ttk.Entry(input_frame, style='Custom.TEntry')
        self.amount.grid(row=2, column=1, pady=5, padx=5)

        ttk.Label(input_frame, text="Description:", style='Main.TLabel').grid(row=3, column=0, pady=5, padx=5)
        self.description = ttk.Entry(input_frame, style='Custom.TEntry')
        self.description.grid(row=3, column=1, pady=5, padx=5)

        ttk.Button(input_frame, text="Add Transaction", style='Custom.TButton', 
                  command=self.add_transaction).grid(row=4, column=0, columnspan=2, pady=10)

        # Transactions list
        list_frame = ttk.LabelFrame(parent, text="Transaction History", style='Secondary.TFrame')
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.trans_tree = ttk.Treeview(list_frame, columns=("Date", "Type", "Category", "Amount", "Description"), 
                                     show="headings", style='Custom.Treeview')
        for col in ("Date", "Type", "Category", "Amount", "Description"):
            self.trans_tree.heading(col, text=col)
            self.trans_tree.column(col, width=100)
        self.trans_tree.pack(fill="both", expand=True, padx=5, pady=5)

    def setup_categories_tab(self, parent):
        input_frame = ttk.LabelFrame(parent, text="Add Category", style='Secondary.TFrame')
        input_frame.pack(pady=10, padx=20, fill="x")

        ttk.Label(input_frame, text="Type:", style='Main.TLabel').grid(row=0, column=0, pady=5, padx=5)
        self.cat_type = ttk.Combobox(input_frame, values=["Income", "Expense"], style='Custom.TCombobox')
        self.cat_type.grid(row=0, column=1, pady=5, padx=5)

        ttk.Label(input_frame, text="Name:", style='Main.TLabel').grid(row=1, column=0, pady=5, padx=5)
        self.cat_name = ttk.Entry(input_frame, style='Custom.TEntry')
        self.cat_name.grid(row=1, column=1, pady=5, padx=5)

        ttk.Button(input_frame, text="Add Category", style='Custom.TButton', 
                  command=self.add_category).grid(row=2, column=0, columnspan=2, pady=10)

    def setup_analysis_tab(self, parent):
        ttk.Button(parent, text="Show Expense Analysis", style='Custom.TButton', 
                  command=self.show_analysis).pack(pady=20)

    def add_transaction(self):
        try:
            amount = float(self.amount.get())
            type_ = self.trans_type.get().lower()
            category = self.category.get()
            description = self.description.get()

            if not all([type_, category, description]):
                messagebox.showerror("Error", "Please fill all fields!")
                return

            self.tracker.transaction_manager.add_transaction(category, description, amount, type_)
            messagebox.showinfo("Success", "Transaction added successfully!")
            self.refresh_transactions()
            
            self.amount.delete(0, tk.END)
            self.description.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount!")

    def add_category(self):
        type_ = self.cat_type.get().lower()
        name = self.cat_name.get()
        
        if not all([type_, name]):
            messagebox.showerror("Error", "Please fill all fields!")
            return

        if self.tracker.category_manager.add_category(name, type_):
            messagebox.showinfo("Success", "Category added successfully!")
            self.cat_name.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Category already exists!")

    def show_analysis(self):
        self.tracker.visualizer.visualize_expenses()

    def update_categories(self, event=None):
        type_ = self.trans_type.get().lower()
        categories = self.tracker.category_manager.get_categories(type_)
        self.category['values'] = categories

    def refresh_transactions(self):
        for item in self.trans_tree.get_children():
            self.trans_tree.delete(item)
        
        transactions = self.tracker.transaction_manager.get_transactions()
        for t in transactions:
            self.trans_tree.insert('', 'end', values=(t[1], t[5], t[2], f"${t[4]:.2f}", t[3]))

    def run(self):
        self.refresh_transactions()
        self.root.mainloop()