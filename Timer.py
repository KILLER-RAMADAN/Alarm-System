import threading
import time
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
from pygame import mixer
from playsound import *


class Countdowntimer:
    def __init__(self):
        self.defulte_song="C:\\Program Files\\alarm\\songs\\Samsung alarm.mp3"
        self.root = tk.Toplevel()
        self.root.geometry("400x170+600+300")
        self.root.title("Countdowntimer")
        self.root.configure(bg="black")
        self.root.attributes("-topmost",True)
        self.root.iconbitmap("c:\\Program Files\\alarm\\images\\alarm.ico")
        self.root.resizable(0,0)

        imag00=tk.PhotoImage(file="c:\\Program Files\\alarm\\images\\deadline.png")

        lbl11000=tk.Label(self.root,image=imag00,bg="black")
        lbl11000.place(x=0,y=10)

        self.hour_time_text=Combobox(self.root,width=5,text="hour",font=("arial 12"))
        self.hour_time_text['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
        self.hour_time_text.current(0)
        self.hour_time_text.place(x=110,y=75)
        txt_lbl_hour_lbl=Label(self.root,text="hour         ",foreground="white",background="black",font=('digital-7', 10, ' bold '))
        txt_lbl_hour_lbl.place(x=110,y=57)
        
        
        self.minute_time_text=Combobox(self.root,width=5,text="minute    ",font=("arial 12"))
        self.minute_time_text['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
        self.minute_time_text.current(0)
        self.minute_time_text.place(x=190,y=75)
        self.txt_lbl_minute_lbl=Label(self.root,text="minute         ",foreground="white",background="black",font=('digital-7', 10, ' bold '))
        self.txt_lbl_minute_lbl.place(x=190,y=57)
        
        
        self.second_time_text=Combobox(self.root,width=5,text="Seconds",font=("arial 12"))
        self.second_time_text['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
        self.second_time_text.current(0)
        self.second_time_text.place(x=270,y=75)
        self.txt_lbl_second_lbl=Label(self.root,text="Seconds    ",foreground="white",background="black",font=('digital-7', 10, ' bold '))
        self.txt_lbl_second_lbl.place(x=270,y=57)

        self.active_button=tk.Radiobutton(self.root,fg="green",value=1,command=self.start_thread,bg="black",bd=0,activebackground="black",highlightcolor="green",highlightbackground="green")
        self.active_button.place(x=85,y=120)
        self.lbl_avtive_lbl=Label(self.root,text="Active Counter",background="black",foreground="white",font=("arial,10,bold")).place(x=105,y=115)
        
        
        self.unavtive_song_button=Label(self.root,text="Stop Sound",background="black",foreground="white",font=("arial,10,bold")).place(x=262,y=137)
        self.unactive_song_button=tk.Radiobutton(self.root,fg="red",value=1,bg="black",bd=0,command=self.stop_alarm,activebackground="black",highlightbackground="red")
        self.unactive_song_button.place(x=240,y=142)
        
        
        self.lbl_unavtive_lbl=Label(self.root,text="Stop Counter",background="black",foreground="white",font=("arial,10,bold")).place(x=262,y=115)
        self.unactive_button=tk.Radiobutton(self.root,fg="red",value=1,bg="black",bd=0,command=self.stop,activebackground="black",highlightbackground="red")
        self.unactive_button.place(x=240,y=120)
        

        self.label_time_label = tk.Label(self.root, font=("Helvetica", 30), text="Time: 00:00:00",background="black",foreground="red")
        self.label_time_label.place(x=105,y=10)
    

        self.root.mainloop()

    def start_thread(self):
      t = threading.Thread(target=self.start)
      t.start()
    
    def stop_alarm(self):
      mixer.music.stop()
     
    
    def start(self):
        self.stop_loop = False
        
        alarm_hour_time=int(self.hour_time_text.get())
        alarm_minute_time=int(self.minute_time_text.get())
        alarm_second_time=int(self.second_time_text.get())
     
        
        full_seconds = (alarm_hour_time*3600) + (alarm_minute_time* 60) + alarm_second_time

        while True and not self.stop_loop :
            if  full_seconds > 0:
             full_seconds -= 1
             minutes, seconds = divmod(full_seconds, 60)
             hours, minutes = divmod(minutes, 60)
             self.label_time_label.config(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
             self.root.update()
             time.sleep(1)
            else:
                messagebox.showinfo("countdown","wakeup wakeup!!! Enter Time Please...",parent=self.root)
                break
        if not self.stop_loop:
         mixer.music.load(self.defulte_song)
         mixer.music.play(-1)
     
    def stop(self):
        self.stop_loop = True
        self.hour_time_text.delete(0,100) and self.minute_time.delete(0,100) and self.second_time.delete(0,100)
        self.label_time_label.config(text="Time: 00:00:00")




