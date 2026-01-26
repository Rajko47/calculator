import tkinter as tk
from math import sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, log, log10, log2, sqrt, factorial, exp, pi, e
import math

ans = ""  # memorija poslednjeg rezultata

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    global ans
    expr = entry.get()
    try:
        expr = expr.replace("^", "**")
        expr = expr.replace("ans", ans)
        # math funkcije
        for func in ["factorial","sin","cos","tan","asin","acos","atan","sinh","cosh","tanh","log","log10","log2","sqrt","exp","pi","e"]:
            expr = expr.replace(func, f"math.{func}" if func not in ["pi","e"] else f"math.{func}")
        result = eval(expr)
        ans = str(result)
        entry.delete(0, tk.END)
        entry.insert(0, ans)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# GUI prozor
root = tk.Tk()
root.title("Napredni Kalkulator")

entry = tk.Entry(root, width=35, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

buttons = [
    '7','8','9','/','C','←',
    '4','5','6','*','(',')',
    '1','2','3','-','pi','e',
    '0','.','^','+','ans','=',
    'sin(','cos(','tan(','asin(','acos','atan',
    'sinh(','cosh(','tanh(','log(','log10(','log2(',
    'sqrt(','factorial(','exp('
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        b = tk.Button(root,text=button,width=5,height=2,font=('Arial',12),command=calculate)
    elif button == "C":
        b = tk.Button(root,text=button,width=5,height=2,font=('Arial',12),command=clear)
    elif button == "←":
        b = tk.Button(root,text=button,width=5,height=2,font=('Arial',12),command=backspace)
    else:
        b = tk.Button(root,text=button,width=5,height=2,font=('Arial',12),command=lambda key=button: press(key))
    
    b.grid(row=row_val,column=col_val,padx=2,pady=2)
    col_val += 1
    if col_val > 5:
        col_val = 0
        row_val += 1

root.mainloop()
