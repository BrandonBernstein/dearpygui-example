import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Multiple Tabs Tutorial")

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Tab 1')
tab_control.add(tab2, text='Tab 2')

label1 = tk.Label(tab1, text="This is Tab 1")
label1.pack(padx=20, pady=20)

label2 = tk.Label(tab2, text="This is Tab 2")
label2.pack(padx=20, pady=20)

tab_control.pack(expand=1, fill="both")

root.mainloop()
