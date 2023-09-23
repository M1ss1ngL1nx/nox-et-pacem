import random
import tkinter as tk
from tkinter import messagebox as msg

def gen_pass():
    low = "abcdefghijklmnopqrstuvxyz"
    upp = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    num = "0123456789"
    sym = "!@#$%^&*"



    all_chars = low + upp + num + sym
    password = random.choice(low) + random.choice(upp) + random.choice(num) + random.choice(sym)
    length = 12
    rem_chars = random.sample(all_chars, length - 6)
    password += "".join(rem_chars)

    pass_entry.delete(0, tk.END)
    pass_entry.insert(tk.END, password)


def copy_pass():
    password = pass_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        msg.showinfo("Password Copied", "Password has been copied to clipboard.")
    else:
        msg.showwarning("No Password", "No password generated.")


def save_pass():
    passes = []
    password = pass_entry.get()
    passes.append(password)
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        passes.append(password)
        msg.showinfo("Password saved", "Password has been saved to system.")
    else:
        msg.showwarning("No Password", "No password saved.")

def prin_pass():
    passes = []
    password = pass_entry.get()
    passes.append(password)
    for i in passes:
        print(i)
        xom = i
       # msg.showinfo("Saved passwords",f"Here are the saved passwords:\n{xom}" )



root = tk.Tk()
root.title("----Password Generator---".center(200))

# Password label and entry
password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()

pass_entry = tk.Entry(root, width=30)
pass_entry.pack()

# Buttons
generate_button = tk.Button(root, text="Generate Password", command=gen_pass)
generate_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_pass)
copy_button.pack(pady=10)

save_button = tk.Button(root, text="Save Password?", command=save_pass)
save_button.pack(pady=10)

print_button = tk.Button(root, text="Print Passwords", command=prin_pass)
print_button.pack(pady=10)


root.mainloop()
