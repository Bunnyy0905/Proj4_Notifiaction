import customtkinter
from tkinter import *
from plyer import notification
root=customtkinter.CTk()
root.title("Notifiaction")
root.geometry("600x500")
root.config(bg="#202630")
FONT=('Arial',15,'bold')
label=customtkinter.CTkLabel(root,text="Notification",font=FONT)
label.place(x=13,y=20)
root.mainloop()