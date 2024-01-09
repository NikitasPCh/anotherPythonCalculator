import tkinter as tk

calc = ""

def addToCalc(symbol):
    global calc
    calc += str(symbol)
    textBox.delete(1.0, "end")
    textBox.insert(1.0, calc)

def evalCalc():
    global calc
    try:
        # Security risk
        calc = str(eval(calc))
        textBox.delete(1.0, "end")
        textBox.insert(1.0, calc)
    except:
        clear()
        textBox.insert(1.0, "Error")

def clear():
    global calc
    calc = ""
    textBox.delete(1.0, "end")


root = tk.Tk()
# Some visual formatting for better presentation
root.title("Calculator")
root.geometry("350x300")
root.minsize(350, 300)
root.maxsize(350, 300)
frame = tk.Frame(root)
frame.place(relx = 0.5, rely = 0.5, anchor = "c")

textBox = tk.Text(frame, height = 2, width = 16, font=("Arial", 24))
textBox.grid(columnspan = 5)

# Number buttons
btn_1 = tk.Button(frame, text = "1", command = lambda: addToCalc(1), width = 5, font = ("Arial", 14))
btn_1.grid(row = 2, column = 1)
btn_2 = tk.Button(frame, text = "2", command = lambda: addToCalc(2), width = 5, font = ("Arial", 14))
btn_2.grid(row = 2, column = 2)
btn_3 = tk.Button(frame, text = "3", command = lambda: addToCalc(3), width = 5, font = ("Arial", 14))
btn_3.grid(row = 2, column = 3)
btn_4 = tk.Button(frame, text = "4", command = lambda: addToCalc(4), width = 5, font = ("Arial", 14))
btn_4.grid(row = 3, column = 1)
btn_5 = tk.Button(frame, text = "5", command = lambda: addToCalc(5), width = 5, font = ("Arial", 14))
btn_5.grid(row = 3, column = 2)
btn_6 = tk.Button(frame, text = "6", command = lambda: addToCalc(6), width = 5, font = ("Arial", 14))
btn_6.grid(row = 3, column = 3)
btn_7 = tk.Button(frame, text = "7", command = lambda: addToCalc(7), width = 5, font = ("Arial", 14))
btn_7.grid(row = 4, column = 1)
btn_8 = tk.Button(frame, text = "8", command = lambda: addToCalc(8), width = 5, font = ("Arial", 14))
btn_8.grid(row = 4, column = 2)
btn_9 = tk.Button(frame, text = "9", command = lambda: addToCalc(9), width = 5, font = ("Arial", 14))
btn_9.grid(row = 4, column = 3)
btn_0 = tk.Button(frame, text = "0", command = lambda: addToCalc(0), width = 5, font = ("Arial", 14))
btn_0.grid(row = 5, column = 2)

# Sign buttons
btn_plus = tk.Button(frame, text = "+", command = lambda: addToCalc("+"), width = 5, font = ("Arial", 14))
btn_plus.grid(row = 2, column = 4)
btn_minus = tk.Button(frame, text = "-", command = lambda: addToCalc("-"), width = 5, font = ("Arial", 14))
btn_minus.grid(row = 3, column = 4)
btn_mult = tk.Button(frame, text = "*", command = lambda: addToCalc("*"), width = 5, font = ("Arial", 14))
btn_mult.grid(row = 4, column = 4)
btn_div = tk.Button(frame, text = "/", command = lambda: addToCalc("/"), width = 5, font = ("Arial", 14))
btn_div.grid(row = 5, column = 4)
btn_open = tk.Button(frame, text = "(", command = lambda: addToCalc("("), width = 5, font = ("Arial", 14))
btn_open.grid(row = 5, column = 1)
btn_close = tk.Button(frame, text = ")", command = lambda: addToCalc(")"), width = 5, font = ("Arial", 14))
btn_close.grid(row = 5, column = 3)

# Other buttons
btn_clear = tk.Button(frame, text = "C", command = clear, width = 11, font = ("Arial", 14))
btn_clear.grid(row = 6, column = 1, columnspan = 2)
btn_calculate = tk.Button(frame, text = "=", command = evalCalc, width = 11, font = ("Arial", 14))
btn_calculate.grid(row = 6, column = 3, columnspan = 2)

root.mainloop()