from __future__ import with_statement
from imp import new_module
from tkinter import *
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import *
from tkinter import ttk
from tokenize import Name
import os
from tkinter import messagebox
import pyttsx3
listdir = []
def Check1():
    file = open("list.dir", "r")
    lines = file.readlines()
    for l in lines:
        listdir.append(l)
        

background = '#000000'
root = Tk()
root.geometry("562x296")
root.config(bg=background)

def Check():
    file = open("Games.list", "r")
    text = file.readlines()
    for l in text:
        listbox.insert(0, l)

def add():
    try:
        NameGame = askopenfile()
        NameGame = NameGame.name
        if NameGame in listdir:
            pass
        else:
            listdir.append(NameGame)
            file = open("list.dir", "w")
            for l in listdir:
                file.write(l+"\n")
            file.close()
            
        Namenew = NameGame.split("/")[-1]
        file = open("Games.list", 'r')
        text = file.read()
        if Namenew in text:
            pass
        else:
            listbox.insert(0, Namenew)
            
            file = open("Games.list", "r")
            data = file.read()+Namenew+"\n"
            file.close()
            #print (data)
            f = open("Games.list", "w")
            f.write(data)
            f.close()
        
    except:
        pass
def rem():
    try:
        global listbox
        NameGame = listbox.get(ACTIVE)
        index = listbox.get(ACTIVE)
        file = open("list.dir", "r")
        lines = file.readlines()
        for l in lines:
            if index in l:
                index = lines.index(l)
                
                lines.pop(index)
        
        data = ""
        for l in lines:
            data += l
            
        file = open("list.dir" , 'w')
        file.write(data)
        file.close()
        
        
        listbox.delete(ACTIVE)
        
        listdir.pop(index)
        file = open("Games.list", "r")
        lines = file.readlines()
        for l in lines:
            if NameGame in l:
                lines.remove(l)
            
        file = open("Games.list", "w")    
        for l in lines:
            
            file.write(l)
        file.close()
                
        
    except:
        pass
def run():
    try:
        NameGame = listbox.get(ACTIVE)
        file = open("list.dir", "r")
        lines = file.readlines()
        for l in lines:
            if NameGame in l:
                index = lines.index(l)
                
        a = lines[index]
        a = a.replace('\n', '')
        
        os.startfile(a)
    except:
        pass

def openf():
    try:
        NameGame = listbox.get(ACTIVE)
        file = open("list.dir", "r")
        lines = file.readlines()
        for l in lines:
            if NameGame in l:
                index = lines.index(l)
                
        a = lines[index]
        a = a.replace('\n', '')
        a = a.replace(NameGame, '')
        os.startfile(a)
    except:
        pass
    
    
            
    
def cleen():
    try:
        listbox.delete(0, END)
        file = open("Games.list", 'w')
        file.write('')
        file.close()
        file = open("list.dir", 'w')
        file.write('')
        file.close()
    except:
        pass
    
def py3():
    try:
        NameGame = listbox.get(ACTIVE)
        engine = pyttsx3.init()
        engine.setProperty("rate", 173)
        engine.say(NameGame)
        engine.runAndWait()
    except:
        pass

# objects

listbox = Listbox(root , width=45, height=18)

listbox.place(relx=0.75 , rely =0.5 , anchor='c', )

#btn add
btn_add = Button(root, width=37, text='Add Game list', height=1, bg=background, fg='white', borderwidth=3, command=add)
btn_add.place(relx=0.25 , rely =0.05 , anchor='c')

#btn remove
btn_rem = Button(root, width=37, text='Remove Game as list', height=1, bg=background, fg='white', borderwidth=3, command=rem)
btn_rem.place(relx=0.25 , rely =0.16 , anchor='c')

#btn run
btn_run = Button(root, width=37, text='Run Game', height=1, bg=background, fg='white', borderwidth=3, command=run)
btn_run.place(relx=0.25 , rely =0.263 , anchor='c')

#btn open
btn_open = Button(root, width=37, text='Open Game Directory', height=1, bg=background, fg='white', borderwidth=3, command=openf)
btn_open.place(relx=0.25 , rely =0.37 , anchor='c')

#btn copy
btn_c = Button(root, width=37, text='Clear All list', height=1, bg=background, fg='white', borderwidth=3, command=cleen)
btn_c.place(relx=0.25 , rely =0.48 , anchor='c')

#btn search
btn_s = Button(root, width=37, text='Read Name Game', height=1, bg=background, fg='white', borderwidth=3, command=py3)
btn_s.place(relx=0.25 , rely =0.59 , anchor='c')

#label made
lblm = Label(root, text='Made by : Amir mohamad arefinia', height=1, bg=background, fg='white', font=('Calibri', 12))
lblm.place(relx=0.20 , rely =0.69 , anchor='c')

#label ap
lblap = Label(root, text='aparat : https://aparat.com/228961354', height=1, bg=background, fg='white', font=('Calibri', 12))
lblap.place(relx=0.23 , rely =0.79 , anchor='c')

#label g
lblg = Label(root, text='Github : https://github.com/Air-pal/', height=1, bg=background, fg='white', font=('Calibri', 12))
lblg.place(relx=0.21 , rely =0.89 , anchor='c')




Check()
root.mainloop()