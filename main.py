import tkinter as tk


root = tk.Tk()

root.geometry("500x500")
root.title("GUI")

label = tk.Label(root, text = "Hello world!", font = ('Arial',18))
label.pack(padx = 20, pady = 20)

textbox = tk.Text(root,height = 3,font = ("Arial",14))
textbox.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight = 1)
buttonframe.columnconfigure(1,weight = 1)
buttonframe.columnconfigure(2,weight = 1)

btn6 = tk.Button(buttonframe, text = "1", font = ('Arial',18))
btn6.grid(row = 0, column = 0, sticky = tk.W + tk.E)

btn6 = tk.Button(buttonframe, text = "2", font = ('Arial',18))
btn6.grid(row = 0, column = 1, sticky = tk.W + tk.E)

btn6 = tk.Button(buttonframe, text = "3", font = ('Arial',18))
btn6.grid(row = 0, column = 2, sticky = tk.W + tk.E)

btn6 = tk.Button(buttonframe, text = "4", font = ('Arial',18))
btn6.grid(row = 1, column = 0, sticky = tk.W + tk.E)

btn6 = tk.Button(buttonframe, text = "5", font = ('Arial',18))
btn6.grid(row = 1, column = 1, sticky = tk.W + tk.E)

btn6 = tk.Button(buttonframe, text = "6", font = ('Arial',18))
btn6.grid(row = 1, column = 2, sticky = tk.W + tk.E)

buttonframe.pack(fill = "x")

anotherbtn = tk.Button(root, text = "TEST")
anotherbtn.place(x = 200, y = 200, height = 100, width = 100)


root.mainloop()

