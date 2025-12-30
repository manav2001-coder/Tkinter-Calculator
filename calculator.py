import tkinter as tk
from tkmacosx import Button 
root = tk.Tk()
root.title("Modern Calculator")

# 1. SET FIXED WINDOW SIZE
# Format: Width x Height
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#2c3e50")  # Dark background color

# Modern Font Styles
ENTRY_FONT = ("Helvetica", 24)
BTN_FONT = ("Helvetica", 14, "bold")

# Entry Widget (The Display)
entry = tk.Entry(
    root,
    font=ENTRY_FONT,
    bg="#ecf0f1",
    fg="#2c3e50",
    borderwidth=5,
    relief="flat",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=20, sticky="nsew")

# Functionality
def enterValue(num):
    entry.insert(tk.END, num)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

# 2. HELPER TO CREATE BUTTONS QUICKLY
def create_button(text, row, col, cmd, color="#34495e", fg="white"):
    btn = Button(root, text=text, font=BTN_FONT, bg=color, fg=fg,relief="flat", activebackground="#1abc9c",command=cmd, width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Row 1
create_button("1", 1, 0, lambda: enterValue("1"))
create_button("2", 1, 1, lambda: enterValue("2"))
create_button("3", 1, 2, lambda: enterValue("3"))
create_button("+", 1, 3, lambda: enterValue("+"), color="#e67e22")

# Row 2
create_button("4", 2, 0, lambda: enterValue("4"))
create_button("5", 2, 1, lambda: enterValue("5"))
create_button("6", 2, 2, lambda: enterValue("6"))
create_button("-", 2, 3, lambda: enterValue("-"), color="#e67e22")

# Row 3
create_button("7", 3, 0, lambda: enterValue("7"))
create_button("8", 3, 1, lambda: enterValue("8"))
create_button("9", 3, 2, lambda: enterValue("9"))
create_button("*", 3, 3, lambda: enterValue("*"), color="#e67e22")

# Row 4
create_button("C", 4, 0, clear, color="#e74c3c")
create_button("0", 4, 1, lambda: enterValue("0"))
create_button("=", 4, 2, calc, color="#2ecc71")
create_button("/", 4, 3, lambda: enterValue("/"), color="#e67e22")

# Ensure the grid stretches appropriately
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()