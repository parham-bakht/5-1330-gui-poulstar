from tkinter import *
from tkinter import messagebox
app = Tk()
def get_user_choice():
    javab = user_choice.get()
    print(javab)
    if javab == "60":
        messagebox.showinfo(title="correct",message="جواب شما درست بود")
    else:
        messagebox.showerror(title="wrong",message="جواب شما اشتباه بود")
        
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

check_btn = Button(app,text="Check Answer",font=("arial",15),bg="green",command=get_user_choice)
check_btn.pack()

app.mainloop()