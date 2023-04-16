import customtkinter
from tkinter import *
import time
from plyer import notification
from tkinter import messagebox

root=customtkinter.CTk()
root.title("Notifier")
root.geometry("500x150")
root.resizable(0,0)
root.config(bg="#202630")
FONT=('Arial',15,'bold')

def notify_me():
    if(entry1.get()=='' or entry2.get()==''):
        messagebox.showerror(title='Error',message='Enter a notification and a time')
    else:
        time.sleep(int(entry2.get()))#delay time
        notification.notify(title='Alert',message=entry1.get(),timeout=60)

        
label1=customtkinter.CTkLabel(root,text="Notification",font=FONT,text_color="#FFFFFF")
label1.place(x=20,y=20)
entry1=customtkinter.CTkEntry(root,font=FONT,width=200,text_color="#000000",fg_color="#FFFFFF")
entry1.place(x=20,y=50)

label2=customtkinter.CTkLabel(root,text="After(Sec)",font=FONT,text_color="#FFFFFF")
label2.place(x=310,y=20)
entry2=customtkinter.CTkEntry(root,font=FONT,width=100,text_color="#000000",fg_color="#FFFFFF")
entry2.place(x=310,y=50)

button=customtkinter.CTkButton(root,text="Notify Me",font=FONT,text_color="#FFFFFF",fg_color="#127a16",hover_color="#127a16",width=50,command=notify_me)
button.place(x=190,y=110)

root.mainloop()
