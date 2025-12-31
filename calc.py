import tkinter as tk

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def cal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Segoe UI", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

operators = {"+", "-", "*", "/", "="}

row = 1
col = 0

for b in buttons:
    if b in operators:
        bg_color = "#f2c94c"     
        fg_color = "black"
    else:
        bg_color = "#3a3a3a"
        fg_color = "white"

    if b == "=":
        cmd = cal
    else:
        cmd = lambda x=b: press(x)

    tk.Button(
        root,
        text=b,
        width=5,
        height=2,
        font=("Segoe UI", 14),
        bg=bg_color,
        fg=fg_color,
        bd=0,
        command=cmd
    ).grid(row=row, column=col, padx=6, pady=6)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    root,
    text="C",
    width=22,
    height=2,
    font=("Segoe UI", 14),
    bg="#ff4444",
    fg="white",
    bd=0,
    command=clear
).grid(row=row, column=0, columnspan=4, padx=6, pady=6)

root.mainloop()
