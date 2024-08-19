import random
from tkinter import*
from tkinter.ttk import*


def low():
    entry.delete(0,END)

    length = Var1.get()

    lower = "abcdefghijklmnopqsrtuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if Var.get() == 1:
        for i in range(0,length):
            password = password+ random.choice(lower)
        return password
    elif Var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
    elif Var.get() == 3:
        for i in range(0,length):
            password = password + random.choice(digits)
        return password
    else:
        print("please choose an option")
    return password


def generate():
    password1 = low()
    entry.delete(0,END)
    entry.insert(0,password1)

def copy1():
    random_password=entry.get()
    root.clipboard_clear()
    root.clipboard_append(random_password)
    root.update()

def update_length(event):
    length=combo.get()
    if length.isdigit():
        Var1.set(int(length))
root = Tk()
Var = IntVar()
Var1 = IntVar()

root.title("Random Password Generator")

Random_password = Label(root,text="password")
Random_password.grid(row=0,column=0)
entry = Entry(root)
entry.grid(row=0,column=1)

c_label = Label(root,text="Length")
c_label.grid(row=1,column=0)

copy_button = Button(root,text="copy",command=copy1)
copy_button.grid(row=0,column=2)
generate_button = Button(root,text="Genetare",command=generate)
generate_button.grid(row=0,column=3)


radio_low = Radiobutton(root,text="Low",variable = Var,value=1)
radio_low.grid(row=1,column=2,sticky='E')
radio_middle = Radiobutton(root,text="Medium",variable=Var,value=0)
radio_middle.grid(row=1,column=3,sticky='E')
radio_strong = Radiobutton(root,text="strong",variable=Var,value=3)
radio_strong.grid(row=1,column=4,sticky='E')


combo = Combobox(root, textvariable=Var1)
combo['values'] = (8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,"Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>',update_length)
combo.grid(column=1,row=1)

root.mainloop()