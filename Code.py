import tkinter as tk
import re

def check_strength(password):
    strength = 0
    remarks = ""

    # Check conditions and update strength
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[\W_]", password):  # Special characters
        strength += 1

    # Remarks based on strength score
    if strength <= 2:
        remarks = "Weak "
    elif strength == 3 or strength == 4:
        remarks = "Moderate "
    else:
        remarks = "Strong "

    return f"Strength: {remarks}"

def on_check():
    password = entry.get()
    result = check_strength(password)
    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=('Arial', 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=25, font=('Arial', 12))
entry.pack()

tk.Button(root, text="Check Strength", command=on_check, font=('Arial', 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12, 'bold'))
result_label.pack(pady=5)

root.mainloop()
