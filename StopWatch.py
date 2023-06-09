import threading
import time
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
from pygame import mixer
from playsound import *


class stopwatch:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("400x170+600+300")
        self.root.title("Stopwatch")
        self.root.configure(bg="black")
        self.root.attributes("-topmost",True)
        self.root.iconbitmap("images\\alarm.ico")
        self.root.resizable(0,0)

        imag00=tk.PhotoImage(file="images\\deadline.png")

        lbl11000=tk.Label(self.root,image=imag00,bg="black")
        lbl11000.place(x=0,y=10)

        self.hour_time_text=Combobox(self.root,width=5,font=("arial 12"))
        self.hour_time_text['values']=("00")
        self.hour_time_text.current(0)
        self.hour_time_text.place(x=110,y=75)
       
        
        
        self.minute_time_text=Combobox(self.root,width=5,font=("arial 12"))
        self.minute_time_text['values']=("00")
        self.minute_time_text.current(0)
        self.minute_time_text.place(x=190,y=75)
     
        
        
        self.second_time_text=Combobox(self.root,width=5,font=("arial 12"))
        self.second_time_text['values']=("00")
        self.second_time_text.current(0)
        self.second_time_text.place(x=270,y=75)
      
        self.active_button=tk.Button(self.root,fg="green",text="Start",width=10,command=self.start_thread,bg="white",bd=0,activebackground="green",highlightcolor="green",highlightbackground="green")
        self.active_button.place(x=100,y=120)
        # self.lbl_avtive_lbl=Label(self.root,text="start",background="black",foreground="white",font=("arial,10,bold")).place(x=130,y=115)
        
        
        # self.unavtive_song_button=Label(self.root,text="reset",background="black",foreground="white",font=("arial,10,bold")).place(x=280,y=137)
        self.unactive_song_button=tk.Button(self.root,fg="red",text="Reset",width=10,bg="white",bd=0,command=self.reset,activebackground="red",highlightbackground="red")
        self.unactive_song_button.place(x=280,y=120)
        
        
        # self.lbl_unavtive_lbl=Label(self.root,text="stop",background="black",foreground="white",font=("arial,10,bold")).place(x=280,y=115)
        self.unactive_button=tk.Button(self.root,fg="red",bg="white",width=10,text="Stop",bd=0,command=self.stop,activebackground="red",highlightbackground="red")
        self.unactive_button.place(x=190,y=120)
        
        
        # self.lbl_unavtive_lbl=Label(self.root,text="countinue",background="black",foreground="white",font=("arial,10,bold")).place(x=262,y=130)
        # self.unactive_button=tk.Radiobutton(self.root,fg="red",value=1,bg="black",bd=0,command=self.countinue,activebackground="black",highlightbackground="red")
        # self.unactive_button.place(x=180,y=142)
        

        self.label_time_label = tk.Label(self.root, font=("Helvetica", 30), text="00:00.00",background="black",foreground="white")
        self.label_time_label.place(x=135,y=10)
        self.stop_loop = False

        self.root.mainloop()

    def start_thread(self):
      self.stop_loop =False
      self.active_button["state"]="disabled"
      self.unactive_song_button["state"]="disabled"  
      t = threading.Thread(target=self.start)
      t.start()
    #   self.unactive_button["state"]="normal"
    #   self.unactive_song_button["state"]="normal"

      
      
    
    

     
    
    def start(self):
        
        
        alarm_hour_time=int(self.hour_time_text.get())
        alarm_minute_time=int(self.minute_time_text.get())
        alarm_second_time=int(self.second_time_text.get())
     
        
        full_seconds = (alarm_hour_time//3600) + (alarm_minute_time//60) + alarm_second_time

        while  full_seconds >= 0 and not self.stop_loop: 
         
         full_seconds += 1
         minutes, seconds = divmod(full_seconds,4500)
         hours, minutes = divmod(minutes,60)
         
         self.label_time_label.config(text=f"{hours:02d}:{minutes:02d}.{seconds:02d}")
        #  if alarm_minute_time=="60":
        #      self.minute_time_text.set("00")
        #      continue
         
   
        
             
            

     
    def stop(self):
        self.stop_loop = True
        self.active_button["state"]="normal"
        self.unactive_song_button["state"]="normal"
        self.root.update()
        
        
        
    def reset(self):
        self.hour_time_text.set("00") and self.minute_time_text.set(0) and self.second_time_text.set(0)
        self.label_time_label.config(text="00:00.00")

