from tkinter import*
def button_click(number):
    global operator
    operator +=str(number)
    input_value.set(operator)
def button_clear():
    global operator
    operator=""
    input_value.set("")

def button_equal():
    global operator
    try:
        result=str(eval(operator))
        input_value.set(result)
        operator=result
    except:
        input_value.set("Error")
        opertor=""
main=Tk()
main.title("Calculator")
operator=""
input_value=StringVar()
display_text=Entry(main,font=("Arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,bg="orange",justify=RIGHT)
display_text.grid(columnspan=4)
btn_7=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="7",command=lambda:button_click(7))
btn_7.grid(row=1,column=0)
btn_8=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="8",command=lambda:button_click(8))
btn_8.grid(row=1,column=1)
btn_9=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="9",command=lambda:button_click(9))
btn_9.grid(row=1,column=2)
btn_div=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="/",command=lambda:button_click("/"))
btn_div.grid(row=1,column=3)
btn_4=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="4",command=lambda:button_click(4))
btn_4.grid(row=2,column=0)
btn_5=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="5",command=lambda:button_click(5))
btn_5.grid(row=2,column=1)
btn_6=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="6",command=lambda:button_click(6))
btn_6.grid(row=2,column=2)
btn_mul=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="*",command=lambda:button_click("*"))
btn_mul.grid(row=2,column=3)
btn_1=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="1",command=lambda:button_click(3))
btn_1.grid(row=3,column=0)
btn_2=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="2",command=lambda:button_click(2))
btn_2.grid(row=3,column=1)
btn_3=Button(main,padx=16,fg="black",font=("Arial",20,"bold"),text="3",command=lambda:button_click(3))
btn_3.grid(row=3,column=2)
btn_sub=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="-",command=lambda:button_click('-'))
btn_sub.grid(row=3,column=3)
btn_0=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="0",command=lambda:button_click(0))
btn_0.grid(row=4,column=0)
btn_clear=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="C",command=button_clear)
btn_clear.grid(row=4,column=1)
btn_eq=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="=",command=button_equal)
btn_eq.grid(row=4,column=2)
btn_add=Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text="+",command=lambda:button_click('+'))
btn_add.grid(row=4,column=3)
main.mainloop()

