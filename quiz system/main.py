from tkinter import *
from time import time
#import feedbackmodule as f1
import string
import sqlite3
import random


#----------------------registration page code----------------------

 
 
def login():
        global root2
        
        root2 = Tk()
        root2.title("Login Form")
        root2.geometry('650x600')
        root2.resizable(0,0)
          
        label_0 = Label(root2, text="LogIn",width=20,font=("Gabriola",24,"bold"))
        label_0.place(x=170,y=53)
  
      
        label_1 = Label(root2, text="Email Id",width=20,font=("bold", 10))
        label_1.place(x=130,y=140)
        fname=StringVar()
        entry_1 = Entry(root2,textvar=fname)
        entry_1.place(x=290,y=140)
        label_11 = Label(root2, text="Password",width=20,font=("bold", 10))
        label_11.place(x=130,y=190)
        pwd=StringVar()
        entry_11 = Entry(root2,textvar=pwd)
        entry_11.place(x=290,y=190)
   
        b2=Button(root2, text='Login',width=20,bg='palegreen',fg='black',command=startmsg,activebackground = "lightgreen")
        b2.place(x=240,y=250)
        b3=Button(root2, text='Forget password',width=20,bg='palegreen',fg='black',activebackground = "lightgreen")
        b3.place(x=240,y=300)
        #img3=PhotoImage(file="person2.png")
        
        #labelimage1=Label(root,
           #         image=img3)
        #labelimage1.place(x=150,y=400)
        root2.mainloop()
def reg():
   
   root = Tk()
   root.title("Registration Form")
   root.geometry('650x600')
   root.resizable(0,0)
   Fullname=StringVar()
   Email=StringVar()
   var = IntVar()
   c=StringVar()
   var1= IntVar()
   #-------now i dont use this part----
   def subclick():
        root.title("Login Form")
        label_0.destroy()
        label_1.destroy()
        entry_1.destroy()
        label_2.destroy()
        entry_2.destroy()
        label_3.destroy()
        label_4.destroy()
        label_5.destroy()
        label_11.destroy()
        entry_11.destroy()
        label_12.destroy()
        entry_12.destroy()
        b1.destroy()
        c1.destroy()
        c2.destroy()
        r1.destroy()
        r2.destroy()
        droplist.destroy()
        login()
        #--------------
        
        
    
   def database():
      name=Fullname.get()
      email=Email.get()
      password=Password.get()
      gender=var.get()
      country=c.get()
      programming=var1.get()
      print(name)
      print(email)
      print(password)
      print(gender)
      print(country)
      print(programming)
     
      
      #with conn:
      cr=db.cursor()
      cr.execute('CREATE TABLE IF NOT EXISTS registration (name text,email text,password text,gender integer,country text,programming integer)')
      cr.execute('INSERT INTO registration (name,email,password,gender,country,programming) VALUES(?,?,?,?,?,?)',(name,email,password,gender,country,programming,))
      db.commit()
   
   
             
   label_0 = Label(root, text="Registration form",width=20,font=("Gabriola",24,"bold"),fg='darkslategray')
   label_0.place(x=150,y=53)
  

   label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
   label_1.place(x=110,y=130)

   entry_1 = Entry(root,textvar=Fullname)
   entry_1.place(x=270,y=130)

   label_2 = Label(root, text="Email",width=20,font=("bold", 10))
   label_2.place(x=98,y=160)

   entry_2 = Entry(root,textvar=Email)
   entry_2.place(x=270,y=160)
   global Password
   Password=StringVar()
   label_11 = Label(root, text="Password",width=20,font=("bold", 10))
   label_11.place(x=110,y=190)

   entry_11 = Entry(root,textvariable=Password,show='*')
   entry_11.place(x=270,y=190)
   z=Password.get()
   print(z)
   label_12 = Label(root, text="Conforim pass",width=20,font=("bold", 10))
   label_12.place(x=120,y=220)
   Cpwd=StringVar()
   entry_12 = Entry(root,textvar=Cpwd,show='*')
   entry_12.place(x=270,y=220)

   label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
   label_3.place(x=100,y=250)
   var = IntVar()
   r1=Radiobutton(root, text="Male",padx = 5, variable=var, value=1)
   r1.place(x=265,y=250)
   r2=Radiobutton(root, text="Female",padx = 20, variable=var, value=2)
   r2.place(x=320,y=250)

   label_4 = Label(root, text="country",width=20,font=("bold", 10))
   label_4.place(x=100,y=280)

   list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

   droplist=OptionMenu(root,c, *list1)
   droplist.config(width=15)
   c.set('select your country') 
   droplist.place(x=270,y=280)

   label_5 = Label(root, text="Programming",width=20,font=("bold", 10))
   label_5.place(x=115,y=330)
   var2= IntVar()
   c1=Checkbutton(root, text="java", variable=var1)
   c1.place(x=265,y=330)
  
   c2=Checkbutton(root, text="python", variable=var2)
   c2.place(x=320,y=330)
   

   b1=Button(root, text='Submit',width=15,bg='skyblue',fg='black',
             command=login,activebackground = "khaki")
   b1.place(x=230,y=400)
   #print(entry_11)
   x=Password.get()
   print(x)
   print()
   
   # ----------------validation------------
   
   

   root.mainloop()

#----------------------------main code---------------------------------

y=1
questions = [
    "How many Keywords are there in C Programming language ?",
    "Which of the following functions takes A console Input in Python ?",
    "Which of The Following is must to Execute a Python Code ?",
    "The append Method adds value to the list at the  ?",
    "Which of The following is executed in browser(client side) ?",
    "Which of the following keyword is used to create a function in Python ?",
    "To Declare a Global variable in python we use the keyword ?",
    "Which is the correct operator for power(xy)?",
    "Which one of these is floor division?",
    "What is the answer to this expression, 22 % 3 is?",
    "What is the return type of function id?",
    "What is the return value of trunc()?",
    "What does 3 ^ 4 evaluate to?",
    "Which of the following operators has its associativity from right to left?",
    "print(0xA + 0xB + 0xC)=?",
    "What is the output when we execute list(“hello”)?",
    "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
    "Suppose list1 is [2, 33, 222, 14, 25], What is list1[:-1]?",
    "Suppose t = (1, 2, 4, 3), which of the following is incorrect?",
    "Which of these about a set is not true?",
    
    ]

answers_choice = [
    ["a) 23","b) 32","c) 33","d) 43",],
    ["a) get()","b) input()","c) gets()","d) scan()",],
    ["a) TURBO C","b) Py Interpreter","c) Notepad","d) IDE",],
    ["a) custom location","b) end","c) center","d) beginning",],
    ["a) perl","b) css","c)  python","d) java",], 
    ["a) function","b) void","c) fun","d) def",],
    ["a) all","b) var","c) let","d) global",],
    ["a) X^y","b) X**y","c) X^^y","d) None of the mentioned",],
    ["a) /"," b) // ","c) % ","d) None of the mentioned",],
    ["a) 7"," b) 0" ,"c) 1 ","d) 5",],
    ["a) int"," b) float", "c) bool ","d) dict",],
    ["a) int ","b) bool", "c) float" ,"d) None",],
    ["a) 81", "b) 12"," c) 0.75"," d) 7",],
    ["a) + ","b) //"," c) % ","d) **",],
    ["a) 0xA0xB0xC", "b) Error"," c) 0x22"," d) 33",],
    ["a) [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]", "b) [‘hello’]"," c) [‘llo’] ","d) [‘olleh’]",],
    ["a) Error","b) None ","c) 25 ","d) 2",],
    ["a)[2, 33, 222, 14]", "b) Error"," c) 25"," d) [25, 14, 222, 33, 2]",],
    ["a) print(t[3])", "b) t[3] = 45"," c) print(max(t))"," d) print(len(t))",],
    ["a) Mutable data type", "b) Allows duplicate values ","c) Data type with unordered values ","d) Immutable data type",]]

    
answers = [1,1,1,1,1,3,3,1,1,2,0,0,3,3,3,0,2,0,1,1] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 15):
        x = random.randint(0,14)
        if x in indexes:
            continue
        else:
             indexes.append(x)
    #print(indexes)
z=[]

#-----------------feedback code-----------



    
#-----------------------------------------
def showresult(score):
    global skip
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r5.destroy()
    r6.destroy()
    r7.destroy()
    lab.destroy()
    l1.destroy()

    def persentage(score):
        a=(score/30)*100
        a=round(a,2)
        b=str(a)+"%"
        per=Label(text=b,
                    font = ("Gabriola",16),
                    background = "#ffffff",)
        per.place(x=280,y=370)

    resulttext=Label(text="* Result Analysis *",
                    font = ("Gabriola",26,'bold'),
                     background = "#ffffff",
                     fg="lawngreen",
                     bg="lightcyan"
                     )
    resulttext.place(x=230,y=40)
    mtx=Label(text="/30",
              font = ("Gabriola",16),
              background = "#ffffff",)
    mtx.place(x=310,y=400)




         
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.place(x=280,y=130)
    labelresulttext = Label(
        root,
        font = ("Gabriola",20,"bold"),
        background = "#ffffff",
        justify="center"
    )
    labelresulttext.place(x=210,y=250)

    questext=Label(text="Total Question= 15",
                    font = ("Gabriola",16),
                    background = "#ffffff",)
    questext.place(x=200,y=310)

    tmtext=Label(text="Total Marks= 30",
                    font = ("Gabriola",16),
                    background = "#ffffff",)
    tmtext.place(x=200,y=340)


    pertext=Label(text="Persentage=",
                    font = ("Gabriola",16),
                    background = "#ffffff",)
    pertext.place(x=200,y=370)
    
    markstext=Label(text="Your Marks=",
                    font = ("Gabriola",16),
                    background = "#ffffff",)
    markstext.place(x=200,y=400)


    timetext=Label(text="Duration=15 minutes",
                    font = ("Gabriola",16),
                    background = "#ffffff",)
    timetext.place(x=200,y=430)

    skiptx=Label(text="No of skip question=",
                 font = ("Gabriola",16),
                 background = "#ffffff",)
    skiptx.place(x=200,y=460)
    skip=Label(text=skip,
               font = ("Gabriola",17),
               background = "#ffffff",)
    skip.place(x=330,y=460)
                 

    
    persentage(score)   
    if score >= 30:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="wow !You Are Excellent !!",fg='darkgreen',)
        marks=Label(text=score,
                    font = ("Gabriola",16),
                    background = "#ffffff",)
        marks.place(x=290,y=400)
    elif (score >=20 and score<30):
        img = PhotoImage(file="prize1.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text=" Good Job !!",fg='limegreen',)
        marks=Label(text=score,
                    font = ("Gabriola",16),
                    background = "#ffffff",)
        marks.place(x=290,y=400)    
    elif (score >=10 and score <20):
        img = PhotoImage(file="star1.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!",fg='deepskyblue',)
        marks=Label(text=score,
                    font = ("Gabriola",16),
                    background = "#ffffff",)
        marks.place(x=290,y=400)
    elif (score>=1 and score<10):
        img = PhotoImage(file="star0.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You should work hard !",fg='orange',)
        marks=Label(text=score,
                    font = ("Gabriola",16),
                    background = "#ffffff",)
        marks.place(x=290,y=400)    
    else:
        img = PhotoImage(file="poor.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="very bad!you should work hard!",fg='red',)
        marks=Label(text=score,
                    font = ("Gabriola",16),
        background = "#ffffff",)
        marks.place(x=290,y=400)   
        

    
    show_ans=Button(root, text='Show Answers',bg='palegreen',fg='black',activebackground = "lightgreen",bd=0)
    #show_ans.place(x=250,y=520)
    #-----for showing feedback popup------
    start=time()
    #def feed0():
      #  import feedbackmodule
    #root.after(5000,feed0)
    
    #g1.graph(score)
    root.mainloop()
    #end=time()

    
    
    
    
    ''' plt.figure(figsize=(6,6))
    z=score
    p=30-z
    labels=['right ans','wrong ans']
    values=[z,p]
    explode=[0,0.05]
    colors=['greenyellow','gold']
    plt.pie(values,labels=labels,autopct="%.1f%%",explode=explode,colors=colors)
    plt.xlabel('Result Analysis')
    plt.show()'''





def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score+2
        x += 1
    print(score)
    showresult(score)            

ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4,r5,r6,r7
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques==15:
        r5.destroy()
        r7=Button(root,
              text=" Finish ",
              font=("Gabriola",12,"bold"),
              background="skyblue",activebackground = "mediumspringgreen",
              command=calc,    
              bd=0,
              )
        r7.place(x=500,y=400)
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        #calc()
        print(indexes)
        print(user_answer)
        
        
         
    elif ques < 15:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
        print(user_answer)
    else:
         print(indexes)
         print(user_answer)
         
         

skip=0       
def nextb():
    global ques,y
    print(ques)
    
    ques += 0
    y +=1
    selected()
    
     
def preb():
     global ques
     ques -= 3
     selected()

def sartQuiz():
    global lblQuestion,r1,r2,r3,r4,r5,r6,l1
    lblQuestion=Label( 
        root,
        text=questions[indexes[0]],
        font=("Gabriola",16),
        width=500,
        #justify="c",
        wraplength=400,
        background="#ffffff"
        )
    lblQuestion.pack(pady=(100,0 ))
    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)
    global ques

    l1=Label(root,text="                                                                                            Left Time:",font=("cambria",12),background="mediumspringgreen",width=75)
    l1.place(x=0,y=50)
    #quesno=indexes[-1]
    #l2=Label(root,text=quesno,font=("cambria",12),background="mediumspringgreen")
    #l2.place(x=0,y=50)
    r1=Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Gabriola",14),
        value=0,
        variable=radiovar,
        #command=selected,
        background="#ffffff"
        )
    r1.place(x=250,y=190)
    r2=Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Gabriola",14),
        value=1,
        variable=radiovar,
        # command=selected,
        background="#ffffff"
        )
    r2.place(x=250,y=230)

    r3=Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Gabriola",14),
        value=2,
        variable=radiovar,
         #command=selected,
        background="#ffffff"
        )
    r3.place(x=250,y=270)

    r4=Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Gabriola",14),
        value=3,
        variable=radiovar,
         #command=selected,
        background="#ffffff"
        )
    r4.place(x=250,y=310)


    r5=Button(root,
              text=" NEXT>> ",
              font=("Gabriola",12,"bold"),
              background="skyblue",activebackground = "mediumspringgreen",
              command=nextb,
              bd=0,
              )
    r5.place(x=500,y=400)
    r6=Button(root,
              text=" <<Previous ",
              font=("Gabriola",12,"bold"),
              background="skyblue",activebackground = "mediumspringgreen",
              command=preb,
              bd=0
              )
    r6.place(x=410,y=400)
     

    #-----------clock code-------------
    from time import time
    global i,j,lab
    i=60
    j=14
    lab=Label(text=i,font=("cambria",12),background="mediumspringgreen",width=6)
    lab.place(x=560,y=50)
    start=time()
    def f1():
        global i,j
        i-=1
        ab=str(j)+":"+str(i)
        lab.configure(text=ab)
        if i%60==0:
            i=60
            j-=1
        if j>=0:ff1()
        else:
            ques=15
            selected()
    
    def ff1():root.after(1000,f1)
    ff1()
    end=time()


            





def startmsg():
    root2.destroy()
    labelimage.destroy()
    labeltext.destroy()
    lblinstruction.destroy()
    b1.destroy()
    #b2.destroy()
    b3.destroy()
    lblRule.destroy()
    gen()
    sartQuiz()


 
root=Tk()
root.title("Online Quiz")
root.geometry("650x600")
root.config(background="#ffffff")
root.resizable(0,0)   


img1=PhotoImage(file="hat1.png")
labelimage=Label(
    root,
    image=img1,
    background="#ffffff",bd=0
    )
labelimage.pack(pady=(50,0))

labeltext=Label(
   root,
   text="Online Quiz",
   font=("Gabriola",26,"bold"),
   background="#ffffff"
   )
labeltext.pack()

b1 = Button(text = " SIGNUP  ",activeforeground = "white",
            activebackground = "lightgreen", background="springgreen",width=10,
            font=("Gabriola",12,"bold"),border=(0),
            command=reg)
b1.pack(pady=(30,0))

b3 = Button(text = " LOGIN ",activeforeground = "white",width=10,
            activebackground = "lightgreen", background="springgreen",
            font=("Gabriola",12,"bold"),border=(0),
            command=login,
            )
b3.place(x=370,y=300)

lblinstruction=Label(root,text="Read The Instruction And \n Click Start Once You Are Read",
   font=("Gabriola",15,"bold"),
   background="#ffffff",
   justify="center",
   fg='darkslategrey'                  
                     
    )
lblinstruction.pack(pady=(30,0))

lblRule=Label(root,
              text="This Quiz Contains 15 Questions\n You will get 1 minutes to solve a question Once you select \nfinal choice hence think before you select\n you have olny 15 minutes to complete quiz",
              font=("Cambria",12),
              width=100,
              background="black",
              foreground="yellow"
              )
lblRule.pack(side="bottom")


root.mainloop()
