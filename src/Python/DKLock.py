# Библиотеки
#----------------------------------------------------------------------------------------------------

import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import hashlib
import webbrowser

#----------------------------------------------------------------------------------------------------



# DB
#----------------------------------------------------------------------------------------------------

db_folder = 'db'
db_file = os.path.join(db_folder, 'pin_code.db')

def create_db():
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pin_codes (id INTEGER PRIMARY KEY, pin TEXT)''')
    conn.commit()
    conn.close()

#----------------------------------------------------------------------------------------------------



# PassWord
#----------------------------------------------------------------------------------------------------

def save_pin(pin):
    hashed_pin = hash_pin(pin)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pin_codes (pin) VALUES (?)", (hashed_pin,))
    conn.commit()
    conn.close()

#----------------------------------------------------------------------------------------------------



# Pin Hashing
#----------------------------------------------------------------------------------------------------

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

#----------------------------------------------------------------------------------------------------



# Checking PassWord
#----------------------------------------------------------------------------------------------------

def check_pin(entered_pin):
    hashed_entered_pin = hash_pin(entered_pin)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT pin FROM pin_codes WHERE pin=?", (hashed_entered_pin,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def unlockFunction(event=None):
    userInput = ent.get()

    if check_pin(userInput):
        root.destroy()
    else:
        messagebox.showwarning(title='Fail', message='Wrong PassWord')

#----------------------------------------------------------------------------------------------------


if not os.path.exists(db_file):
     create_db()
     
     def set_new_pin():
        user_pin = ent.get()
        if len(user_pin) < 4:
            messagebox.showwarning(title='Error', message='PIN must be at least 4 digits long')
        else:
            save_pin(user_pin)
            messagebox.showinfo(title='Success', message='PIN code saved')
            root.destroy()
            root = Tk()



# Параметры Окна
#----------------------------------------------------------------------------------------------------

     root = Tk()
     root.title('Set PIN Code')
     root.geometry('400x600')
     root['bg'] = 'black'
     
#----------------------------------------------------------------------------------------------------



# Интерфейс программы
#----------------------------------------------------------------------------------------------------

     input = tkinter.Label(root, text='Set a new PIN code', font='Candara', bg='black', fg='white')
     ent = Entry(root, show="*", justify='center', font="Calibri 20")
     saveButton = tkinter.Button(root, text='Save PIN', font='Candara', bg='black', fg='white', height=1, command=set_new_pin)
     
     input.place(relx=0.5, rely=0.45, anchor=CENTER)
     ent.place(relx=0.5, rely=0.5, anchor=CENTER, width=150, height=30)
     saveButton.place(relx=0.5, rely=0.56, anchor=CENTER)

     ent.bind('<Return>', set_new_pin)
     root.mainloop()

#----------------------------------------------------------------------------------------------------



else:
    # Окно для ввода пин-кода
    root = Tk()
    root.title('DKLock')
    root.geometry('400x600')
    root['bg'] = 'black'

    input = tkinter.Label(root, text='Input the PassWord', font='Candara', bg='black', fg='white')
    ent = Entry(root, show="*", justify='center', font="Calibri 20")
    unlockButton = tkinter.Button(root, text='Unlock', font='Candara', bg='black', fg='white', height=1, command=unlockFunction)

    input.place(relx=0.5, rely=0.45, anchor=CENTER)
    ent.place(relx=0.5, rely=0.5, anchor=CENTER, width=150, height=30)
    unlockButton.place(relx=0.5, rely=0.56, anchor=CENTER)

    ent.bind('<Return>', unlockFunction)

    

# Feedback
#----------------------------------------------------------------------------------------------------

def feedback():
        webbrowser.open_new(r"https://t.me/DKLiberty")

feedbackButton = Button(root, text='Feedback', font = 'Candara', bg = 'black', fg = 'white', command=feedback)

feedbackButton.place(relx=1.0, rely=0, anchor='ne')

#----------------------------------------------------------------------------------------------------



# Безопасность
#----------------------------------------------------------------------------------------------------

def blockscreen():
    root.protocol("WM_DELETE_WINDOW", blockscreen)
    root.update()
    
def fullscreen():
    root.attributes('-fullscreen', True, '-topmost', True)

fullscreen()

blockscreen()

#----------------------------------------------------------------------------------------------------



# Окно
#----------------------------------------------------------------------------------------------------

root.mainloop()

#----------------------------------------------------------------------------------------------------
