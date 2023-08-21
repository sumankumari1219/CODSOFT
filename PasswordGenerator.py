import random
import string
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("500x600")
root.maxsize(500,600)
root.minsize(500,600)

uname=StringVar()
passw=IntVar()
genpass=StringVar()

def generate():
    # print(uname.get())
    s1=string.ascii_letters
    s2=string.punctuation
    s3=string.digits
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    random.shuffle(s)
    genpass.set("".join(s[0:passw.get()]))

def accept():
    a=tmsg.askquestion("Confirmation",f" Your user name is {uname.get()} of length {passw.get()} and The Generated Password is {genpass.get()}\nIf you like the password then press OK otherwise press NO")
    if (a=='yes'):
        msg="Great....\nThanks for accepting the password"
    else:
        msg="Then again press the GENERATE PASSWORD button"
    tmsg.showinfo("Password Generated",msg)

def reset():
    uname.set("")
    passw.set("")
    genpass.set("")
    name_enter.focus()

root.title("Password Generator")

l1=Label(root,text="Password Generator",fg="blue",font="Impact 20 bold underline")
l1.place(x=120,y=20)

name=Label(root,text="Enter user name:",font="PalatinoLinotype 13")
name.place(x=20,y=100)

name_enter=Entry(root,width=30,textvariable=uname,borderwidth=3,font="DubaiMedium 10",relief=GROOVE)
name_enter.place(x=240,y=103)
name_enter.focus()

password=Label(root,text="Enter password length:",font="PalatinoLinotype 13")
password.place(x=20,y=140)

pass_enter=Entry(root,width=30,borderwidth=3,font="DubaiMedium 10",textvariable=passw,relief=GROOVE)
pass_enter.place(x=240,y=140)
passw.set("")

gpass=Label(root,text="Generated password:",font="PalatinoLinotype 13")
gpass.place(x=20,y=180)

gen_pass=Entry(root,width=30,borderwidth=3,font="DubaiMedium 10",textvariable=genpass,relief=GROOVE)
gen_pass.place(x=240,y=180)

Button(root,text="GENERATE PASSWORD",bg="blue",fg="white",font="Georgia 15",width=20,borderwidth=3,command=generate).place(x=130,y=230)
Button(root,text="ACCEPT",fg="blue",font="Georgia 15",width=7,command=accept).place(x=200,y=290)
Button(root,text="RESET",fg="blue",font="Georgia 15",width=5,command=reset).place(x=210,y=350)

root.mainloop()