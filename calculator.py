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

btn_plus = Button(app,text="+",font=("arial",15),bg="orange",width=7)
btn_plus.grid(row=1,column=3)

btn_4 = Button(app,text="4",font=("arial",15),bg="#1F50FF",width=7)
btn_4.grid(row=2,column=0)

btn_5 = Button(app,text="5",font=('arial',15),bg="#1F50FF",width=7,)
btn_5.grid(row=2,column=1)

btn_6 = Button(app,text="6",font=('arial',15),bg="#1F50FF",width=7)
btn_6.grid(row=2,column=2)

btn_min = Button(app,text="-",font=("arial",15),bg="orange",width=7)
btn_min.grid(row=2,column=3)




btn_1 = Button(app,text="1",font=("arial",15),bg="#1F50FF",width=7)
btn_1.grid(row=3,column=0)

btn_2 = Button(app,text="2",font=('arial',15),bg="#1F50FF",width=7,)
btn_2.grid(row=3,column=1)


btn_3 = Button(app,text="3",font=('arial',15),bg="#1F50FF",width=7)
btn_3.grid(row=3,column=2)

btn_multi = Button(app,text="*",font=("arial",15),bg="orange",width=7)
btn_multi.grid(row=3,column=3)

app.mainloop()