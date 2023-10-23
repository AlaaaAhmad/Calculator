from tkinter import *

# Specifying the window properties
window = Tk()
window.geometry("420x420")
window.title("Calculator")
window.configure(bg = "pink")

equation_text = ""
equation_label = StringVar()


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equality():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
    except SyntaxError:
        equation_label.set("Syntax Error")
    except ZeroDivisionError:
        equation_label.set("Can't Divide by Zero!")


def clear():
    equation_label.set("")


# Specifying the label properties
label = Label(window,
              textvariable= equation_label,
              width=36,
              height=3,
              bg="White",
              font=("Arial", 12)
              )
label.pack()

frame = Frame(window, bg="Pink")
frame.pack()

# Row 0 Creation
button1 = Button(frame, text='1', height=4, width=9, command= lambda: button_press(1), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button1.grid(row=0, column=0)
button2 = Button(frame, text='2', height=4, width=9, command= lambda: button_press(2), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button2.grid(row=0, column=1)
button3 = Button(frame, text='3', height=4, width=9, command= lambda: button_press(3) , bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button3.grid(row=0, column=2)
plus = Button(frame, text='+', height=4, width=9, command= lambda: button_press('+'), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
plus.grid(row=0, column=3)

# Row 1 Creation
button4 = Button(frame, text='4', height=4, width=9, command= lambda: button_press(4), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button4.grid(row=1, column=0)
button5 = Button(frame, text='5', height=4, width=9, command= lambda: button_press(5), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button5.grid(row=1, column=1)
button6 = Button(frame, text='6', height=4, width=9, command= lambda: button_press(6), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button6.grid(row=1, column=2)
minus = Button(frame, text='-', height=4, width=9, command= lambda: button_press('-'), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
minus.grid(row=1, column=3)

# Row 2 Creation

button7 = Button(frame, text='7', height=4, width=9, command= lambda: button_press(7), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button7.grid(row=2, column=0)
button8 = Button(frame, text='8', height=4, width=9, command= lambda: button_press(8), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button8.grid(row=2, column=1)
button9 = Button(frame, text='9', height=4, width=9, command= lambda: button_press(9), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button9.grid(row=2, column=2)
multiply = Button(frame, text='*', height=4, width=9, command= lambda: button_press('*'), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
multiply.grid(row=2, column=3)

# Row 3 Creation

button0 = Button(frame, text='0', height=4, width=9, command= lambda: button_press(0), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
button0.grid(row=3, column=0)
equal = Button(frame, text='=', height=4, width=9, command= equality, bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
equal.grid(row=3, column=1)
decimal = Button(frame, text='.', height=4, width=9, command= lambda: button_press('.'), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
decimal.grid(row=3, column=2)
divide = Button(frame, text='/', height=4, width=9, command= lambda: button_press('/'), bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
divide.grid(row=3, column=3)

clearB = Button(frame, text = "Clear", height=4, width=9, command=clear, bg="Black", fg="Pink", font=("Arial",9), activebackground="Black", activeforeground="Pink")
clearB.grid(row = 4, column = 0, columnspan= 4)
window.mainloop()
