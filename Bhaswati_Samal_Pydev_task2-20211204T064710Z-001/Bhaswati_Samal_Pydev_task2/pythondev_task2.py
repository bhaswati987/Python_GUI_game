#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from random import randint

window= Tk()

window.geometry("350x300")
window.title("Rock,Paper,Scissor,Lizard,Spock")
window.configure(background="dark slate gray")

def window2():
    w2=Toplevel(window)
    w2.title("THE GAME")
    w2.configure(background="dark slate gray")
    
    #center images
    nmp=Image.open("middleplayer.jpeg")
    nmpr=nmp.resize((70,70),Image.ANTIALIAS)
    middle_player=ImageTk.PhotoImage(nmpr)
    nmc=Image.open("middlecomp.jpeg")
    nmcr=nmc.resize((70,70),Image.ANTIALIAS)
    middle_comp=ImageTk.PhotoImage(nmcr)
    
    #optionimages
    nr=Image.open("ro.jpeg")
    nrr=nr.resize((70,70),Image.ANTIALIAS)
    rockimg=ImageTk.PhotoImage(nrr)
    np=Image.open("paper.jpeg")
    npr=np.resize((70,70),Image.ANTIALIAS)
    paperimg=ImageTk.PhotoImage(npr)
    ns=Image.open("scissors.jpeg")
    nsr=ns.resize((70,70),Image.ANTIALIAS)
    scissorsimg=ImageTk.PhotoImage(nsr)
    nl=Image.open("lizard.jpeg")
    nlr=nl.resize((70,70),Image.ANTIALIAS)
    lizardimg=ImageTk.PhotoImage(nlr)
    nsp=Image.open("spock.jpeg")
    nspr=nsp.resize((70,70),Image.ANTIALIAS)
    spockimg=ImageTk.PhotoImage(nspr)
    


    middleplayer=Label(w2,image=middle_player)
    middlecomputer=Label(w2,image=middle_comp)
    middleplayer.grid(row=4,column=4 )
    middlecomputer.grid(row=4,column=11 )

    lost=Label(w2,text=0,font=20,bg= "pale green",fg="dim gray")
    win=Label(w2,text=0,font=20,bg= "pale green",fg="dim gray")
    lost.grid(row=7,column=12)
    win.grid(row=7,column=5)

    def score_of_comp():
        total=int(lost['text'])
        total+=1
        lost['text']=str(total)
        if total==3:
            window3()
            
    
    def score_of_player():
        total=int(win['text'])
        total+=1
        win['text']=str(total)
    
    def results(p,c):
        if p==c:
            pass
        elif p=="rock":
            if c=="paper":
                score_of_comp()
            elif c=="spock":
                 score_of_comp()
            else:
                score_of_player()
      
           
        elif p=="paper":
            if c=="scissors":
                score_of_comp()
            elif c=="lizard":
                 score_of_comp()
            else:
                score_of_player()
        
            
        elif p=="scissors":
            if c=="rock":
                score_of_comp()
            elif c=="spock":
                 score_of_comp()
            else:
                score_of_player()
       
             
        elif p=="lizard":
            if c=="rock":
                score_of_comp()
            elif c=="scissors":
                 score_of_comp()
            else:
                score_of_player()
        
            
        elif p=="spock":
            if c=="paper":
                score_of_comp()
            elif c=="lizard":
                 score_of_comp()
            else:
                score_of_player()
             
        else:
            pass
   

    options=["rock","paper","scissors","lizard","spock"]

    def selection(x):
        choice_of_computer=options[randint(0,4)]
        choice_of_player=x
        if choice_of_computer=="rock":
            middlecomputer.configure(image=rockimg)
        elif choice_of_computer=="paper":
            middlecomputer.configure(image=paperimg)
        elif choice_of_computer=="scissors":
            middlecomputer.configure(image=scissorsimg)
        elif choice_of_computer=="lizard":
            middlecomputer.configure(image=lizardimg)
        else:
            middlecomputer.configure(image=spockimg)
        
        if x=="rock":
            middleplayer.configure(image=rockimg)
        elif x=="paper":
             middleplayer.configure(image=paperimg)
        elif x=="scissors":
             middleplayer.configure(image=scissorsimg)
        elif x=="lizard":
             middleplayer.configure(image=lizardimg)
        else:
            middleplayer.configure(image=spockimg)
        results(choice_of_player,choice_of_computer)




    l21=Label(w2,text=e1.get(),font=20,bg= "misty rose",fg="gray29").grid(row="1",column="4")


    l22=Label(w2,text="Computer",font=20,bg= "misty rose",fg="gray29").grid(row="1",column="11")


    b21=Button(w2,image=rockimg,command=lambda:selection("rock")).grid(row="2",column="1")
    b22=Button(w2,image=paperimg,command=lambda:selection("paper")).grid(row="3",column="1")
    b23=Button(w2,image=scissorsimg,command=lambda:selection("scissors")).grid(row="4",column="1")
    b24=Button(w2,image=lizardimg,command=lambda:selection("lizard")).grid(row="5",column="1")
    b25=Button(w2,image=spockimg,command=lambda:selection("spock")).grid(row="6",column="1")
    l1=Label(w2,image=rockimg).grid(row="2",column="14")
    l2=Label(w2,image=paperimg).grid(row="3",column="14")
    l3=Label(w2,image=scissorsimg).grid(row="4",column="14")
    l4=Label(w2,image=lizardimg).grid(row="5",column="14")
    l5=Label(w2,image=spockimg).grid(row="6",column="14")



    l6=Label(w2,text="VS",font=30,bg= "misty rose",fg="gray29").grid(row="4",column="9")
    l7=Label(w2,text="POINTS",font=30,bg= "gray2",fg="snow").grid(row="7",column="1")
    l8=Label(w2,text=e1.get() +" 's score=>",font=20,bg= "pale green",fg="dim gray").grid(row="7",column="4")
    l9=Label(w2,text="Computer's score=>",font=20,bg= "pale green",fg="dim gray").grid(row="7",column="11")
    

  
    def window3():
        w3=Toplevel(w2)
        w3.title("RESULTS")
        w3.geometry("320x300")
        w3.configure(background="dark slate gray") 
        def exit():
            w3.destroy()
            w2.destroy()
            window.destroy()
    
        def new_game():
            w3.destroy()
            w2.destroy()
            e1.delete(0,END)
    
        l31=Label(w3,text=e1.get() + " 's score is:-",font=30,bg= "misty rose",fg="gray29").place(x=10,y=50)
        l32=Label(w3,text=win.cget("text"),font=30).place(x=190,y=50)
        b31=Button(w3,text="EXIT",command=exit,height=4,width=10,bg= "pale green",fg="dim gray").place(x=10,y=200)
        b32=Button(w3,text="START NEW GAME",command=new_game,height=4,width=20,bg= "pale green",fg="dim gray").place(x=150,y=200)

        w3.mainloop()

    w2.mainloop()



l11= Label(window, text= "THE GAME OF", font= ('arial',20),bd=5,bg= "misty rose",fg="gray29")
l11.place(x=80,y=40)

l12= Label(window, text="CHANCES", font= ('arial',29,'bold'),bg= "misty rose",fg="gray29")
l12.place(x=80,y=80)



l13= Label(window, text="Enter name:", font= ('arial'), bg= "ivory2",fg="IndianRed1")
l13.place(x=50,y=150)
e1=Entry(window)
e1.place(x=170,y=150)


b11= Button(window, text= "START!", font=('bold',12),height=3, width= 10,bg= "pale green",fg="dim gray",command=window2)
b11.place(x=130,y=220)


window.mainloop()


# In[ ]:




