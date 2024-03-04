import string
import random
from tkinter import *
from tkinter import messagebox
import re
import sqlite3

with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL);")
cursor.execute("SELECT * FROM users")
db.commit()
db.close()

class GENERATE():
    def __init__(val,num):
        val.master = num
        val.passwordlen = IntVar()
        val.generatedpassword = StringVar()
        val.n_generatedpassword = StringVar()
        val.n_passwordlen = IntVar()
        box.title('Password Generator')
        box.geometry('550x300')
        box.config(bg='lightblue')
        box.resizable(0, 0)
        val.label = Label(text="Password Generator", anchor=N, fg='black', bg='pink', font='arial 20 bold underline')
        val.label.grid(row=0, column=1)

        val.blank_label1 = Label(text="")
        val.length = Label(text="Enter Password Length: ", font='normal', bg='pink', fg='black')
        val.length.grid(row=6, column=0)

        val.length_textfield = Entry(textvariable=val.n_passwordlen, font='normal', bd=6, relief='ridge')
        val.length_textfield.grid(row=6, column=1)
        val.generated_password = Label(text="Generated Password: ", font='normal', bg='pink', fg='black')
        val.generated_password.grid(row=8, column=0)

        val.generated_password_textfield = Entry(textvariable=val.n_generatedpassword, font='normal', bd=6, relief='ridge', fg='RED')
        val.generated_password_textfield.grid(row=8, column=1)
        val.generate = Button(text="Generate Password", bd=0, padx=1, pady=1, font='normal' , fg='black', bg='#BCEE68', command=val.generate_pass)
        val.generate.grid(row=11, column=1)
        val.reset = Button(text="Reset", bd=0, padx=1, pady=1, font='normal', fg='black', bg='violet', command=val.reset_fields)
        val.reset.grid(row=15, column=1)

    def generate_pass(self):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        chars = "@#%&()\"?!"
        numbers = "1234567890"
        upper = list(upper)
        lower = list(lower)
        chars = list(chars)
        numbers = list(numbers)
        leng = self.length_textfield.get()

        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
        length = int(leng) 

        if length<6:
            messagebox.showerror("Error", "Password must be atleast 6 characters long")
            self.textfield.configure(text="")
            return
        else:
            self.blank_label1.configure(text="")

        self.generated_password_textfield.delete(0, length)
        u = random.randint(1, length-3)
        l = random.randint(1, length-2-u)
        c = random.randint(1, length-1-u-l)
        n = length-u-l-c

        password = random.sample(upper, u)+random.sample(lower, l)+random.sample(chars, c)+random.sample(numbers, n)
        random.shuffle(password)
        gen_passwd = "".join(password)
        n_generatedpassword = self.generated_password_textfield.insert(0, gen_passwd)

    def reset_fields(self):
        self.length_textfield.delete(0, 25)
        self.generated_password_textfield.delete(0, 25)

if __name__=='__main__':
    box = Tk()
    pass_gen = GENERATE(box)
    box.mainloop()