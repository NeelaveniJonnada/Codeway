from tkinter import *

box = Tk() # This is to create a basic window box
box.geometry("310x326")  # this is for the size of the window box
box.resizable(False,False)  # this is to prevent from resizing the window box
box.title("Simple Calculator")
# This Function continuously updates the input value whenever you give an input
def enter(number):
    global value
    value = value + str(number)
    input_value.set(value)
# 'remove' function :This is used to clear or remove the input field
def remove(): 
    global value 
    value = "" 
    input_value.set("")
# 'calculate' function calculates the value present in input field
def calculate():
    global value
    result = str(eval(value)) # 'eval' function is used to evaluates the string value directly
    input_value.set(result)
    value = ""
value = ""
# 'StringVar()' :It is used to get the instance of input value
input_value = StringVar()
# Let us creating a frame for the input value
input_frame = Frame(box, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=BOTTOM)
#creating an input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 12, 'bold'), textvariable=input_value, width=50, bg="pink", bd=0, justify=LEFT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
#creating another 'Frame' for the button
btns_frame = Frame(box, width=312, height=272.5, bg="orange")
btns_frame.pack()

# first row of the calculator
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: remove()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# second row of the calculator
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: enter(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#87CEFA", cursor = "arrow", command = lambda: calculate()).grid(row = 4, column = 3, padx = 1, pady = 1)

box.mainloop()
