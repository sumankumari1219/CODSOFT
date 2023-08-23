import random
from tkinter import *
root=Tk()
root.geometry("580x600")
root.title("Quiz")
root.minsize(600,600)
root.maxsize(600,600)

radiovar = IntVar()
radiovar.set(-1)

ques=["What is the output of the following code snippet?\nprint(2**3+(5+6)**(1+1))",
      "How is a code block indicated in Python?",
      "What will be the output of the following code snippet?\na=[1,2,3]\na=tuple(a)\na[0]=2\nprint(a)",
      "Which of the following is not the part of Python?",
      "Which of the following statements are used in Exception Handeling in Python?",
      "Which of the following types of loops are not supported in Python?",
      "Which of the following is the proper syntax to check if a particular element is present in a list?",
      "What will be the output of the following code snippet?\na=[1,2]\nprint(a*3)",
      "Which of the following functions converts date to corresponding time in Python?",
      "Which of the following blocks will always be executed whether an exception is encountered or not in the program?"]
ans_choice=[["A. 129","B. 8","C. 121","D. None of the above"],
            ["A. Brackets","B. Indentation","C. Key","D. None of the above"],
            ["A. [2,2,3]","B. (2,2,3)","C. (1,2,3)","D. Error"],
            ["A. Pointers","B. Loops","C. Dynamic Typing","D. All of the above"],
            ["A. try","B. catch","C. finally","D. All of the above"],
            ["A. for","B. while","C. do-while","D. None of the above"],
            ["A. if ele in list","B. if not ele not in list","C. Both A and B","D. None of the above"],
            ["A. Error","B. [1,2]","C. [1,2,1,2]","D. [1,2,1,2,1,2]"],
            ["A. strptime()","B. strftime()","C. Both A and B","D. None of the above"],
            ["A. try","B. catch","C. finally","D. None of the above"]]
indexes=[]
ans=[0,1,3,0,3,2,2,3,0,2]
user_ans=[]

def showresult(score):
    global lbl,button
    button.destroy()
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    if (score==25):
        lbl=Label(root,text="Fabulous✔.....\nYou scored 25/25🎁",font="LucidaBright 15",fg="green",width=100)
        lbl.pack(pady=200)
    elif (score == 20):
        lbl=Label(root, text="Excellent.....\nYou scored 20/25👏",font="LucidaBright 15",fg="green",width=100)
        lbl.pack(pady=200)
    elif (score == 15):
        lbl=Label(root, text="Very Good.....\nYou scored 15/25",font="LucidaBright 15",fg="green",width=100)
        lbl.pack(pady=200)
    elif (score == 10):
        lbl=Label(root, text="Good.....\nYou scored 10/25",font="LucidaBright 15",fg="green",width=100)
        lbl.pack(pady=200)
    elif(score==5):
        lbl=Label(root, text="Bad.....\nWork Hard!\nYou scored 5/25",font="LucidaBright 15",fg="green",width=100)
        lbl.pack(pady=200)
    else:
        lbl=Label(root, text="Worst.....\nYou performed worst😒\nYou scored 0/25\n",font="LucidaBright 15",fg="green",width=100)
        lbl.pack(pady=200)


def startQuiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion=Label(root,text=ques[indexes[0]],font="Leelawadee 20",width=400,justify="center",wraplength=300)
    lblQuestion.pack(pady=(100,8))
    global radiovar
    r1 = Radiobutton(root, text=ans_choice[indexes[0]][0], font="Times 15", variable=radiovar, justify="left" ,value=0,command=selected)
    r1.pack(pady=2)
    r2 = Radiobutton(root, text=ans_choice[indexes[0]][1], font="Times 15", variable=radiovar, justify="left", value=1,command=selected)
    r2.pack(pady=2)
    r3 = Radiobutton(root, text=ans_choice[indexes[0]][2], font="Times 15", variable=radiovar, justify="left", value=2,command=selected)
    r3.pack(pady=2)
    r4 = Radiobutton(root, text=ans_choice[indexes[0]][3], font="Times 15", variable=radiovar, justify="left", value=3,command=selected)
    r4.pack(pady=2)

def calc():
    global indexes,user_ans,ans,button
    global score
    x=0
    score=0
    for i in indexes:
        if user_ans[x] == ans[i]:
            score=score+5
        x=x+1
    button=Button(root,text="Show Result",fg="white",bg="green",font="Leelawadee 30",border=3,relief=FLAT,command=lambda: showresult(score))
    button.place(x=190,y=450)


question=1
def selected():
    global question
    global radiovar,user_ans
    global lblQuestion,r1,r2,r3,r4
    x=radiovar.get()
    user_ans.append(x)
    radiovar.set(-1)
    if (question<5):
        lblQuestion.config(text=ques[indexes[question]])
        r1['text']= ans_choice[indexes[question]][0]
        r2['text'] = ans_choice[indexes[question]][1]
        r3['text'] = ans_choice[indexes[question]][2]
        r4['text'] = ans_choice[indexes[question]][3]
        question=question+1
    else:
        calc()


def generate_question():
    global indexes
    while (len(indexes)<5):
        x=random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def press_start():
    quiz.destroy()
    start_button.destroy()
    ins_label.destroy()
    quiz_ins.destroy()
    generate_question()
    startQuiz()

quiz=Label(root,text="QUIZ",font="Ravie 60 bold",fg="green")
quiz.place(x=150,y=100)
start_button=Button(root,text="START QUIZ ➨",height=1,width=15,font="System 20 bold",bg="green",fg="white",border=3,relief=FLAT,command=press_start)
start_button.place(x=150,y=220)

ins_label=Label(root,text="Read the Rules and Regulations given below.\nClick start only when you are ready.",font="MalgunGothic 10 bold")
ins_label.place(x=135,y=290)
quiz_ins=Label(root,font="LucidaBright 13",bg="black",fg="white",width=100,text="This quiz contains 5 questions.\nEach question contains 5 marks.\nOnce you select the answer for the question then you can't\nbe able to go on previous question.\nSo,click on the answer only when you are confident.")
quiz_ins.pack(side="bottom")

root.mainloop()