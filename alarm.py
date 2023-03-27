from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from pygame import mixer
import datetime
from datetime import *
from time import strftime
from tkinter import messagebox
from threading import *

root=tk.Tk()
root.title("ALARM")
root.geometry("400x170+600+300")
root.configure(background="black")
root.iconbitmap("images/alarm.ico")
root.resizable(0,0)




Menubar=Menu(root)
root.config(menu=Menubar)
organise_menue=Menu(Menubar,tearoff=False)
def develober():
    messagebox.showinfo("Ahmed Ramadan Abd Elnaser","Contact Me On\nAhmed-Ramadan-Abd-Elnaser@protonmail.com")
    
Menubar.add_command(label="devoleped by",command=develober,font=('Technolog', 3, ' bold '))

def clock():
    now=strftime("%H:%M:%S %p")
    lbl0.config(text=now)
    lbl0.after(200,clock)
    
lbl0=Label(root,font=('Technolog', 22, ' bold '),background="black",foreground="red")
lbl0.place(x=135,y=10)
clock()





framr_body=tk.Frame(root,width=1000,height=7,bg="#000000")

framr_body.place(x=0,y=0)





img=tk.PhotoImage(file="images/clock.png")

lbl1=tk.Label(root,image=img,bg="black")
lbl1.place(x=0,y=10)



hour_time=Combobox(root,width=5,text="hour",font=("arial 12"))
hour_time['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
hour_time.current(0)
hour_time.place(x=110,y=68)
txt_lbl_hour=Label(root,text="hour         ",foreground="white",background="black",font=('digital-7', 10, ' bold '))
txt_lbl_hour.place(x=110,y=50)


minute_time=Combobox(root,width=5,text="minute    ",font=("arial 12"))
minute_time['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
minute_time.current(0)
minute_time.place(x=190,y=68)
txt_lbl_minute=Label(root,text="minute         ",foreground="white",background="black",font=('digital-7', 10, ' bold '))
txt_lbl_minute.place(x=190,y=50)

second_time=Combobox(root,width=5,text="Seconds",font=("arial 12"))
second_time['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
second_time.current(0)
second_time.place(x=270,y=68)
txt_lbl_second=Label(root,text="Seconds    ",foreground="white",background="black",font=('digital-7', 10, ' bold '))
txt_lbl_second.place(x=270,y=50)

time_period=Combobox(root,width=5,font=("digital-7 7"))
time_period['values']=("PM","AM")
time_period.current(0)
time_period.place(x=343,y=68)





def active_alarm():
  t1=Thread(target=alarm)
  t1.start()

def stop_alarm():
    print("stop alarm now")
    mixer.music.stop()

def exit():
    root.destroy()

active=tk.Radiobutton(root,fg="green",value=1,command=active_alarm,bg="black",bd=0,activebackground="black",highlightcolor="green",highlightbackground="green")
active.place(x=100,y=120)
avtive_lbl=Label(root,text="Active Alarm",background="black",foreground="white",font=("arial,10,bold")).place(x=115,y=115)


unavtive_lbl=Label(root,text="Stop Alarm",background="black",foreground="white",font=("arial,10,bold")).place(x=262,y=115)
unactive=tk.Radiobutton(root,fg="red",value=1,bg="black",bd=0,command=stop_alarm,activebackground="black",highlightbackground="red")
unactive.place(x=240,y=120)

exit_button=tk.Button(root,text="EXIT",bg="black",fg="white",activebackground="black",command=exit,width=10,bd=0)
exit_button.place(x=5,y=123)


def sound_alarm():
    mixer.music.load("images/mixkit-city-alert-siren-loop-1008.mp3")
    mixer.music.play(-1)
   

 

def alarm():
    while True:
     if hour_time.get()=="00" and minute_time.get()=="00" and second_time.get()=="00":
      messagebox.showerror("ERROR","Please Select Correct Time...")
      break
     else:
      alarm_hour=hour_time.get()
      alarm_minute=minute_time.get()
      alarm_second=second_time.get()
      alarm_period=time_period.get()
      now=datetime.now()
      hour=now.strftime("%I")
      minute=now.strftime("%M")
      seconds=now.strftime("%S") 
      period=now.strftime("%p")
      if period==alarm_period:
            if hour==alarm_hour:
                if minute==alarm_minute:
                    if seconds==alarm_second:
                         sound_alarm()
                         break
mixer.init()
root.mainloop()
