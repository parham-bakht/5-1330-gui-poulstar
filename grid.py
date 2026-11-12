from tkinter import *
app = Tk()
app.geometry("600x600")

lbl1 = Label(app,text="LABEL 1",font=("arial",15),bg="red")
lbl1.grid(row=1,column=1)

lbl2 = Label(app,text="Label 2",font=("arial",15),bg="green")
lbl2.grid(row=1,column=2)
app.mainloop()