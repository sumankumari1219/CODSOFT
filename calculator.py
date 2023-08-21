from tkinter import *
root=Tk()

root.geometry("260x400")
root.minsize(260,400)
root.maxsize(260,400)

root.title("Calculator")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 30")
screen.pack(padx=10,pady=10)
screen.focus()
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
       if scvalue.get().isdigit():
           value = int(scvalue.get())
       else:
           value=eval(screen.get())
       scvalue.set(value)
       screen.update()
    elif text == "AC":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

f2=Frame(root,height="400",width="260")
f2.pack(side="top",padx=20)

b=Button(f2,text="AC",height="3",width="4",relief=GROOVE)
b.grid(row=3,column=1,padx=5,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="%",height="3",width="4",relief=GROOVE)
b.grid(row=3,column=2,padx=5,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="/",height="3",width="4",relief=GROOVE)
b.grid(row=3,column=3,padx=5,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="*",height="3",width="4",relief=GROOVE)
b.grid(row=3,column=4,padx=5,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="7",height="3",width="6")
b.grid(row=4,column=1,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="8",height="3",width="6")
b.grid(row=4,column=2,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="9",height="3",width="6")
b.grid(row=4,column=3,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="-",height="3",width="4",relief=GROOVE)
b.grid(row=4,column=4,padx=5,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="4",height="3",width="6")
b.grid(row=5,column=1,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="5",height="3",width="6")
b.grid(row=5,column=2,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="6",height="3",width="6")
b.grid(row=5,column=3,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="+",height="3",width="4",relief=GROOVE)
b.grid(row=5,column=4,padx=5,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="1",height="3",width="6")
b.grid(row=6,column=1,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="2",height="3",width="6")
b.grid(row=6,column=2,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="3",height="3",width="6")
b.grid(row=6,column=3,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text=".",height="3",width="4",relief=GROOVE)
b.grid(row=6,column=4,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="00",height="3",width="6",relief=GROOVE)
b.grid(row=7,column=1,padx=5,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="0",height="3",width="6")
b.grid(row=7,column=2,padx=3,pady=4)
b.bind("<Button-1>",click)
b=Button(f2,text="=",height="3",width="12",relief=GROOVE,bg="pink")
b.grid(row=7,column=3,columnspan=2,padx=3,pady=4)
b.bind("<Button-1>",click)

root.mainloop()