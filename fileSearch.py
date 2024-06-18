from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.title("Main Window")
toplevel = tk.Toplevel()
toplevel.title("Secondary Window")
filename = filedialog.askopenfilename(
    parent=toplevel,
    title="Browse File"
)
root.mainloop()