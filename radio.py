from tkinter import *

app = Tk()
app.geometry("400x400")

q_lbl = Label(app,text="هر یک ساعت چند دقیقه است؟",font=("arial",15))
q_lbl.pack(pady=30)

option1 = Radiobutton(app,text="362 دقیقه",font=("arial",15))
option1.pack(pady=10)

option2 = Radiobutton(app,text="60 دقیقه",font=("arial",15))
option2.pack(pady=10)

option3 = Radiobutton(app,text="44 دقیقه",font=("arial",15))
option3.pack(pady=10)

app.mainloop()