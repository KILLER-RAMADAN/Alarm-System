from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from pygame import mixer
import datetime
from datetime import *
from time import strftime
from tkinter import messagebox
from threading import *
from tkinter import filedialog
from Timer import Countdowntimer
from StopWatch import stopwatch

    



root=tk.Tk()
root.title("Alarm")
root.geometry("400x170+600+300")
root.configure(background="black")
root.iconbitmap("c:\\Program Files\\alarm\\images\\alarm.ico")
root.resizable(0,0)
root.attributes("-topmost",True)
img=tk.PhotoImage(file="c:\\Program Files\\alarm\\images\\clock.png")

lbl1=tk.Label(root,image=img,bg="black")
lbl1.place(x=0,y=10)

def load_music():
    global target
    filetypes = ( ('mp3 files', '*.mp3'), ('All files', '*.*') )
    target=filedialog.askopenfile(initialdir="C:\\Program Files\\alarm\\songs",filetypes=filetypes)# to select folder only...
    




Menubar=Menu(root)
root.config(menu=Menubar)
organise_menue=Menu(Menubar,tearoff=False)
def develober():
    messagebox.showinfo("Ahmed Ramadan Abd Elnaser","Contact Me On\nAhmed-Ramadan-Abd-Elnaser@protonmail.com")
    
Menubar.add_command(label="Devoleped By",command=develober,font=('SF Pro', 3, ' bold '))
Menubar.add_command(label="Edit Alarm Music ",command=load_music,font=('Technolog', 3, ' bold '))
Menubar.add_command(label="Stopwatch",command=stopwatch,font=('Technolog', 3, ' bold '))
Menubar.add_command(label="Timer",command=Countdowntimer,font=('Technolog', 3, ' bold '))
def clock():
    now=strftime("%H:%M:%S %p")
    lbl0.config(text=now)
    lbl0.after(200,clock)
    
lbl0=Label(root,font=('SF Pro', 22,"bold"),background="black",foreground="white")
lbl0.place(x=135,y=10)
clock()


framr_body=tk.Frame(root,width=1000,height=7,bg="#000000")

framr_body.place(x=0,y=0)

hour_time=Combobox(root,width=5,text="hour",font=("arial 12"))
hour_time['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
hour_time.current(0)
hour_time.place(x=110,y=68)
txt_lbl_hour=Label(root,text="hour         ",foreground="white",background="black",font=('SF Pro', 10, ' bold '))
txt_lbl_hour.place(x=110,y=50)


minute_time=Combobox(root,width=5,text="minute    ",font=("arial 12"))
minute_time['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
minute_time.current(0)
minute_time.place(x=190,y=68)
txt_lbl_minute=Label(root,text="minute         ",foreground="white",background="black",font=('SF Pro', 10, ' bold '))
txt_lbl_minute.place(x=190,y=50)

second_time=Combobox(root,width=5,text="Seconds",font=("arial 12"))
second_time['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
second_time.current(0)
second_time.place(x=270,y=68)
txt_lbl_second=Label(root,text="Seconds    ",foreground="white",background="black",font=('SF Pro', 10, ' bold '))
txt_lbl_second.place(x=270,y=50)

time_period=Combobox(root,width=5,font=("SF Pro",7,"bold"))
time_period['values']=("PM","AM")
time_period.current(0)
time_period.place(x=343,y=68)






def active_alarm():
  if hour_time.get()=="00" and minute_time.get()=="00" and second_time.get()=="00":
      messagebox.showerror("ERROR","Please Select Correct Time...")
  else:
   messagebox.showinfo("Set Successfully",f"alarm Set:{hour_time.get()}:{minute_time.get()}:{second_time.get()}")  
   Target=Thread(target=alarm)
   Target.start()

def stop_alarm():
   
    messagebox.showinfo("awake","YOU ARE AWAKE NOW!!!!")
    mixer.music.stop()

def exit():
    root.destroy()

active=tk.Button(root,fg="green",command=active_alarm,bg="white",bd=0,text="Active Alarm",activebackground="red",highlightcolor="green",highlightbackground="green")
active.place(x=110,y=120)
# avtive_lbl=Label(root,text="Active Alarm",background="black",foreground="white",font=("arial,10,bold")).place(x=140,y=115)




exit_button=tk.Button(root,text="EXIT",bg="black",fg="white",activebackground="red",command=exit,width=10,bd=0)
exit_button.place(x=12,y=123)

defulte_song="C:\\Program Files\\alarm\\songs\\iphone sound.mp3"
songs=[]
songs.append(defulte_song)
def sound_alarm():
    global unavtive_lbl
    # unavtive_lbl=Label(root,text="Stop Alarm",background="black",foreground="white",font=("arial,10,bold")).place(x=262,y=115)
    unactive=tk.Button(root,fg="red",bg="white",text="Stop Alarm",bd=0,command=stop_alarm,activebackground="black",highlightbackground="red")
    unactive.place(x=270,y=120)
    for song in songs: 
     mixer.music.load(song)
     mixer.music.play(-1)
    else:
     mixer.music.load(target)
     mixer.music.play(-1)


 

def alarm():
    while True:  
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
                         messagebox.showinfo("THANKS","WAKEUP MAN WAKEUP!!!!🚀🚀")  
                         break



















mixer.init()
root.mainloop()



 #   time_lbl=Label(background="black",foreground="white",font="Helvetica 7 bold",)
    #   m_time=f"last alarm:{hour_time.get()}:{minute_time.get()}:{second_time.get()}"
    #   time_lbl.config(text=m_time)
    #   time_lbl.place(x=110,y=100)
    # self.hour_time.delete(0,100) and self.minute_time.delete(0,100) and self.second_time.delete(0,100)
