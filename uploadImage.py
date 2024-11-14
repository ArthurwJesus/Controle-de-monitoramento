import tkinter
import  customtkinter
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import shutil
import random
import string
from tkinter import messagebox

def viewPic(filephat):
    global img 

    img = Image.open(filephat)
    img = img.resize((250,250),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    pic_show = tk.Label(frame,bg="#1F6AA5",image=img)
    pic_show.grid(row=1,column=0,columnspan=3,pady=5,ipady=0,sticky="nswe")
    entity_Path.insert(0,filephat)

def selectPic():
    global filename
    filename= filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Selecione a foto do usuário",
        filetypes=(("jpg images","*.jpg"),)
    )
    viewPic(filename)

def savePic():
    filenameSplit = filename.split('.')
    textRandom = ''.join((random.choice(string.ascii_lowercase) for x in range(12)))
    shutil.copy(filename,f"./bd-images/{textRandom}.{filenameSplit[1]}")
    viewPic('default-img/default.jpg')
    messagebox.showinfo("Sucess","Uploado completo")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("👤 Cadastro de usuário")
app.geometry("480x360")


frame = customtkinter.CTkLabel(app,text="")
frame.grid(row=0,column=0,sticky="w",padx=50,pady=20)

btn_Select = customtkinter.CTkButton(frame,text="Carregar imagem",width=50,command=selectPic)
entity_Path = customtkinter.CTkEntry(frame,width=200)
btn_Save = customtkinter.CTkButton(frame,text="Upload",width=50, command=savePic)
pic_show = tk.Label(frame,bg="#1F6AA5")


viewPic('default-img/default.jpg')

btn_Select.grid(row=0,column=0,padx=1,pady=5,ipady=0,sticky="e")
entity_Path.grid(row=0,column=1,padx=1,pady=5,ipady=0,sticky="e")
btn_Save.grid(row=0,column=2,padx=1,pady=5,ipady=0,sticky="e")
pic_show.grid(row=1,column=0, columnspan=3,padx=1,pady=5,ipady=0,sticky="nswe")

app.resizable(False,False)
app.mainloop()


