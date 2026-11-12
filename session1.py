from tkinter import *
# T Bozorg K koochik
app = Tk()
# تغییر سایز صفحه
app.geometry("500x700")

# تغییر رنگ پس زمینه
app.config(bg="#212121")

first_label = Label(app,text="Hello World",bg="red",fg="white",font=("times",30))

# first_label.place(x=180,y=400)
first_label.pack(pady=50)

first_button = Button(app,text="Click me",bg="green",fg="white",font=("times",30))
first_button.pack()

first_entry = Entry(app,font=("times",30),fg="red")
first_entry.pack(pady=30)



app.mainloop()
