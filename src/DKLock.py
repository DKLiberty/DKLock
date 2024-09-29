import tkinter
from tkinter import * 
from tkinter import messagebox
from tkinter import font
import sys
import os
import os.path
import random
import pyautogui
import wmi
import webbrowser
import keyboard

myList = ['1', '2', '3', '4', '5', '6', '7']
random.shuffle(myList, random.random)
lst1 = ''.join(myList)
lst2 = lst1[::-1]

def btn_click():
        password_1 = ent.get()
        c = wmi.WMI()

        for disk in c.Win32_LogicalDisk():
                d = disk
                d = str(d)
                b = "{''}"
        for char in b:
                d = d.replace(char, "")
        if 'VolumeName = "DK";' in d:
                root.destroy()
        elif 'VolumeName = "DK";' not in d:
                if password_1==lst2:
                        root.destroy()
                else:
                        messagebox.showwarning(title = 'Error', message = 'I couldn\'t find the key')


def back():
        d3.place_forget()
        ent.place_forget()
        button3.place_forget()
        button4.place_forget()
        v1.place_forget()
        d1.place(relx=0.5, rely=0.44, anchor=CENTER)
        button1.place(relx=0.48, rely=0.5, anchor=CENTER)
        button2.place(relx=0.51, rely=0.5, anchor=CENTER)
        
  
def yes():
        c = wmi.WMI()

        for disk in c.Win32_LogicalDisk():
                d = disk
                d = str(d)
                b = "{''}"
        for char in b:
                d = d.replace(char, "")
        if 'VolumeName = "DK";' in d:
                root.destroy()
        elif 'VolumeName = "DK";' not in d:
                messagebox.showwarning(title = 'Error', message = 'I couldn\'t find the key')

def no():
        print(lst2)
        d1.place_forget()
        button1.place_forget()
        button2.place_forget()
        d3.place(relx=0.5, rely=0.45, anchor=CENTER)
        ent.place(relx=0.5, rely=0.5, anchor=CENTER, width=150, height=30)
        button3.place(relx=0.5, rely=0.56, anchor=CENTER)
        button4.place(relx=0.0, rely=0.0, anchor=NW)
        v1.place(relx=1.0, rely=1.0, anchor=SE)

def feedback():
        webbrowser.open_new(r"https://t.me/Akmal1309")

root = Tk()
root.title('DKLock')
root.geometry('400x600')
root['bg'] = 'black'

v1 = tkinter.Label(root, text = lst1, font = 'Candara', bg = 'black', fg = 'white')
d1 = tkinter.Label(root, text = 'Do You Have The Key?', font = 'Candara', bg = 'black', fg = 'white')
d1.place(relx=0.5, rely=0.44, anchor=CENTER)
button1= tkinter.Button(root, text='Yes', font = 'Candara', bg = 'black', fg = 'white', command=yes)
button2 = tkinter.Button(root, text = 'No', font = 'Candara', bg = 'black', fg = 'white', command = no)
button1.place(relx=0.48, rely=0.5, anchor=CENTER)
button2.place(relx=0.51, rely=0.5, anchor=CENTER)
d3 = tkinter.Label(root, text = 'Input the password', font = 'Candara', bg = 'black', fg = 'white')
ent = Entry(root, show="x", justify='center', font="Calibri 20")
button3 = tkinter.Button(root, text = 'Unlock', font = 'Candara', bg = 'black', fg = 'white', height=1, command = btn_click)
button4 = tkinter.Button(root, text = '<- Back', font = 'Candara', bg = 'black', fg = 'white', command = back)
d4 = tkinter.Label(root, text = 'DKLock', font = 'Candara', bg = 'black', fg = 'white')
d4.place(relx=0.5, rely=0.01, anchor=CENTER)

# Feedback
b5 = Button(root, text='Feedback', font = 'Candara', bg = 'black', fg = 'white', command=feedback)
b5.place(relx=1.0, rely=0, anchor='ne')

def block():
    pyautogui.moveTo(x=680,y=800)
    root.protocol("WM_DELETE_WINDOW",block)
    root.update()
    
def fullscreen():
    root.attributes('-fullscreen', True, '-topmost', True)

keyboard.send('win+d')

fullscreen()

block()

root.mainloop()