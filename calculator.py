from tkinter import *
app = Tk()
app.config(bg="#212121")


input = StringVar(app)
ent_number = Entry(app,font=("arial",15),borderwidth=5,textvariable=input)
ent_number.grid(row=0,column=0,pady=10,padx=10,columnspan=4,sticky=EW)

btn_7 = Button(app,text="7",font=("arial",15),bg="#1F50FF",width=7)
btn_7.grid(row=1,column=0)

btn_8 = Button(app,text="8",font=('arial',15),bg="#1F50FF",width=7)
btn_8.grid(row=1,column=1)

btn_9 = Button(app,text="9",font=('arial',15),bg="#1F50FF",width=7)
btn_9.grid(row=1,column=2)

app.mainloop()