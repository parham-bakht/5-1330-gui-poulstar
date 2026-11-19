from tkinter import *

app = Tk()
app.geometry("400x400")

q_lbl = Label(app,text="هر یک ساعت چند دقیقه است؟",font=("arial",15))
q_lbl.pack(pady=30)

user_choice = StringVar(app,"362")

option1 = Radiobutton(app,text="362 دقیقه",font=("arial",15),variable=user_choice,value="362")
option1.pack(pady=10)

option2 = Radiobutton(app,text="60 دقیقه",font=("arial",15),variable=user_choice,value="60")
option2.pack(pady=10)

option3 = Radiobutton(app,text="44 دقیقه",font=("arial",15),variable=user_choice,value="44")
option3.pack(pady=10)

check_btn = Button(app,text="Check Answer",font=("arial",15),bg="green")
check_btn.pack()

app.mainloop()