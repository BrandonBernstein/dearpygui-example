import tkinter as tk
from tkinter import messagebox

class MyGui:

    def __init__(self):

        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff = 8)
        self.filemenu.add_command(label = "Close", command = self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Close Without Question", command = exit)
        self.menubar.add_cascade(menu = self.filemenu, label  = " File")
        self.root.config(menu = self.menubar)

        self.actionmenu = tk.Menu(self.menubar, tearoff = 8)
        self.actionmenu.add_command(label = "Show Message", command = self.show_message)
        self.menubar.add_cascade(menu = self.actionmenu, label  = "Action")


        self.label = tk.Label(self.root, text=  "Your Message", font = ('Arial',10))
        self.label.pack(padx = 10,pady = 10)

        self.textbox = tk.Text(self.root, font = ('Arial',10))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx = 10, pady = 10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text = "Show Messagebox", font = ('Arial',10), variable = self.check_state)
        self.check.pack(padx = 10, pady = 10)

        self.button = tk.Button(self.root, text= "Show Message", font = ('Arial',10), command = self.show_message)
        self.button.pack(padx = 10, pady = 10)

        self.clearnbtn = tk.Button(self.root, text = "Clear", font = ('Arial',10), command = self.clear)
        self.clearnbtn.pack(padx = 10, pady = 10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):

        if self.check_state.get() == 0:
            print(self.textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(title = "Message", message = self.textbox.get('1.0',tk.END))

    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_messsage()

    def on_closing(self):
        if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGui()