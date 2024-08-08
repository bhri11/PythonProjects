from tkinter import *
import bcrypt
import json

# Load stored passwords from a file
def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save passwords to a file
def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

# Add a new password
def add_password(email, new_password):
    if email in passwords:
        feedback_label.config(text="Email already exists", fg="red")
    else:
        hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        passwords[email] = hashed.decode('utf-8')
        save_passwords(passwords)
        feedback_label.config(text="Password added successfully", fg="green")

# Validate the password
def validate(email, password):
    hashed = passwords.get(email)
    if hashed and bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')):
        feedback_label.config(text="Login successful", fg="green")
    else:
        feedback_label.config(text="Invalid email or password", fg="red")

passwords = load_passwords()

root = Tk()
root.geometry("300x400")
root.title("Password Manager")

# Email Entry
email_label = Label(root, text="Enter your email:")
email_label.pack(pady=10)

email_entry = Entry(root)
email_entry.pack(pady=5)

# Password Entry
password_label = Label(root, text="Enter your password:")
password_label.pack(pady=10)

password_entry = Entry(root, show="*")
password_entry.pack(pady=5)

# Add Email and Password
new_email_label = Label(root, text="Add new email:")
new_email_label.pack(pady=10)

new_email_entry = Entry(root)
new_email_entry.pack(pady=5)

new_password_label = Label(root, text="Add new password:")
new_password_label.pack(pady=10)

new_password_entry = Entry(root, show="*")
new_password_entry.pack(pady=5)

# Buttons
validate_button = Button(root, text="Validate", command=lambda: validate(email_entry.get(), password_entry.get()))
validate_button.pack(pady=5)

add_button = Button(root, text="Add Password", command=lambda: add_password(new_email_entry.get(), new_password_entry.get()))
add_button.pack(pady=5)

# Feedback Label
feedback_label = Label(root, text="")
feedback_label.pack(pady=10)

root.mainloop()
