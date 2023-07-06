from tkinter import *
import random

root= Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("GAME")
root.config(bg="white")

Label(root,text="TAŞ,KAĞIT,MAKAS", font="arial 18 bold", bg="white").pack()

user_take=StringVar()
Label(root,text="Birini seçiniz: taş,kağıt,makas", font="arial 16 bold",bg="white").place(x=20,y=70)
Entry(root,font="arial 15", textvariable=user_take, bg="red").place(x=90,y=130)

comp_pick=random.randint(1,3)
if comp_pick ==1:
    comp_pick="taş"
elif comp_pick ==2:
    comp_pick="kağıt"
else:
    comp_pick="makas"

Result=StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set("berabere, aynı seçimi yaptınız")
    elif user_pick =="taş" and comp_pick == "kağıt":
        Result.set("kaybettiniz, bilgisayar kağıt seçti.")
    elif user_pick =="taş" and comp_pick == "makas":
        Result.set("kazandınız, bilgisayar makas seçti.")
    elif user_pick =="kağıt" and comp_pick == "taş":
        Result.set("kazandınız, bilgisayar taş seçti.")
    elif user_pick == "kağıt" and comp_pick == "makas":
        Result.set("kaybettiniz, bilgisayar makas seçti.")
    elif user_pick == "makas" and comp_pick == "kağıt":
        Result.set("kazandınız, bilgisayar kağıt seçti.")
    elif user_pick == "makas" and comp_pick == "taş":
        Result.set("kaybettiniz, bilgisayar taş seçti.")
    else:
        Result.set("gecersiz seçim .Lütfen birini seçiniz")



def Reset():
    Result.set("")
    user_take.set("")


def Exit():
    root.destroy()

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='red',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='red' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='red' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='red' ,command = Exit).place(x=230,y=310)

root.mainloop()
