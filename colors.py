
from tkinter import *
app = Tk()
def purple():
    app.config(bg="purple")

def pink():
    app.config(bg="pink")

app.geometry("700x700")

purple_btn = Button(
    app,
    text="purple screen",
    bg="purple",
    font=("Times",20),
    fg="white",
    command=purple
)
purple_btn.pack(pady=10)



pink_btn = Button(
    app,
    text="pink screen",
    bg="pink",
    font=("Times",20),
    fg="black",
    command=pink
)
pink_btn.pack(pady=10)

# یک عدد دکمه دیگه بسازید 
# کاری کنید که هرموقع روی اون دکمه کلیک میکنیم رنگ صفحه عوض بشه
app.mainloop()