from tkinter import *
app = Tk()
app.geometry("600x600")

lbl1 = Label(app,text="LABEL 1",font=("arial",15),bg="red")
lbl1.grid(row=1,column=1)

lbl2 = Label(app,text="Label 2",font=("arial",15),bg="green")
lbl2.grid(row=1,column=2)

lbl3 = Label(app,text="Label 3",font=("arial",15),bg="blue")
lbl3.grid(row=1,column=3)


btn_1 = Button(app,text="Button",font=("arial",15),bg="purple")
# EW = East West
# NS = Norht South
btn_1.grid(row=2,column=1,columnspan=3,sticky="ew")

lbl5 = Label(app,text="Label 5",font=("arial",16),bg="yellow")
lbl5.grid(row=3,column=1,columnspan=3,sticky="ew")

lbl6 = Label(app,text="Label 6",font=("arial",15),bg="light green")
lbl6.grid(row=1,column=4,rowspan=3,sticky="ns")


app.mainloop() 