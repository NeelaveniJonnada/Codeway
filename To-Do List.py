from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add():  
    task_name = task_field.get()  
    if len(task_name) == 0:  
        messagebox.showinfo('Error', 'Field is Empty, Please enter the task')  
    else:    
        tasks.append(task_name)   
        the_cursor.execute('insert into tasks values (?)', (task_name ,))    
        update()    
        task_field.delete(0, 'end')  
    
def delete():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())    
        if the_value in tasks:  
            tasks.remove(the_value)    
            update()   
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No task is selected , could not able to delete , select task.') 
   
def update():    
    clear()    
    for task in tasks:    
        task_listbox.insert('end', task)  
         
def clear():   
    task_listbox.delete(0, 'end')  
  
def close():    
    print(tasks)   
    guibox.destroy()  
    
def retrieve():    
    while(len(tasks) != 0):    
        tasks.pop()    
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  
if __name__ == "__main__":   
    guibox = Tk()   
    guibox.title("To-Do List ")  
    guibox.geometry("665x400+550+250")   
    guibox.resizable(False, False)  
    guibox.configure(bg = "pink")  
   
    the_connection = sql.connect('listOfTasks.db')   
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  
    tasks = []  
    functions_frame = Frame(guibox, bg = "violet") 
    functions_frame.pack(side = "top", expand = True, fill = "both")  
    task_label = Label( functions_frame,text = "Enter your task",  
        font = ("arial", "14", "normal"),  
        background = "lightblue", 
        foreground="black"
    )    
    task_label.place(x = 25, y = 40)  
        
    task_field = Entry(  
        functions_frame,  
        font = ("Arial", "14"),  
        width = 42,  
        foreground="black",
        background = "white",  
    )    
    task_field.place(x = 190, y = 40)  
    
    add_button =Button(  
        functions_frame,  
        text = "Add",  
        width = 15,
        bg='yellow',font=("arial", "14", "normal"),
        command = add,
    )  
    del_button = Button(  
        functions_frame,  
        text = "Remove",  
        width = 15,
        bg='yellow', font=("arial", "14", "normal"),
        command = delete,  
    )  

    exit_button = Button(  
        functions_frame,  
        text = "Exit / Close",  
        width = 52,
        bg='yellow',  font=("arial", "14", "normal"),
        command = close  
    )    
    add_button.place(x = 18, y = 80,)  
    del_button.place(x = 240, y = 80)  
    exit_button.place(x = 17, y = 330)  
    
    task_listbox = Listbox(  
        functions_frame,  
        width = 70,  
        height = 9,  
        font="normal",
        selectmode = 'SINGLE',  
        background = "white",
        foreground="blue",    
        selectbackground = "lightblue",  
        selectforeground="orange"
    )    
    task_listbox.place(x = 17, y = 140)  
    
    retrieve()  
    update()    
    guibox.mainloop()    
    the_connection.commit()  
    the_cursor.close()