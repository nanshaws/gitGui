import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def set_git_email(email, global_scope=False):
    try:
        scope = "--global" if global_scope else "--local"
        subprocess.run(["git", "config", scope, "user.email", email], check=True)
        messagebox.showinfo("Success", f"Git user email has been set to: {email}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while setting the Git user email: {e}")

def set_git_username(username, global_scope=False):
    try:
        scope = "--global" if global_scope else "--local"
        subprocess.run(["git", "config", scope, "user.name", username], check=True)
        messagebox.showinfo("Success", f"Git user name has been set to: {username}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while setting the Git user name: {e}")


def set_git_userpassword(userpassword, global_scope=False):
    try:
        scope = "--global" if global_scope else "--local"
        subprocess.run(["git", "config", scope, "user.password", userpassword], check=True)
        messagebox.showinfo("Success", f"Git user name has been set to: {userpassword}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while setting the Git user password: {e}")

def load_from_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not filename:
        return
    try:
        with open(filename, 'r') as file:
            config = {}
            for line in file:
                # Strip whitespace and split by '='
                if '=' in line:
                    key, value = line.split('=', 1)  # Split on first '='
                    config[key.strip()] = value.strip()

            # Update entries with the loaded configurations
            if 'email' in config:
                email_entry.delete(0, tk.END)
                email_entry.insert(0, config['email'])
            else:
                messagebox.showerror("Error", "Email entry is missing in the file.")

            if 'name' in config:
                username_entry.delete(0, tk.END)
                username_entry.insert(0, config['name'])
            else:
                messagebox.showerror("Error", "Username entry is missing in the file.")

            if 'password' in config:
                password_entry.delete(0, tk.END)
                password_entry.insert(0, config['password'])
            else:
                messagebox.showerror("Error", "Password entry is missing in the file.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the file: {e}")

def on_submit():
    email = email_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    global_scope = global_var.get()

    if not email or not username or not password:
        messagebox.showerror("Error", "Email, Username, and Password fields cannot be empty.")
        return

    set_git_email(email, global_scope)
    set_git_username(username, global_scope)
    set_git_userpassword(password,global_scope)
    # Here we show the password just for demonstration purposes
    # Note: You typically wouldn't show or store passwords in this manner.
    messagebox.showinfo("Password", f"The password is: {password}")

# GUI setup
root = tk.Tk()
root.title("Git Configurator")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# Email entry
tk.Label(frame, text="Email:").grid(row=0, column=0, sticky='e')
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=0, column=1)

# Username entry
tk.Label(frame, text="Username:").grid(row=1, column=0, sticky='e')
username_entry = tk.Entry(frame, width=30)
username_entry.grid(row=1, column=1)

# Password entry
tk.Label(frame, text="Password:").grid(row=2, column=0, sticky='e')
password_entry = tk.Entry(frame, width=30, show="*")
password_entry.grid(row=2, column=1)

# Global scope checkbox
global_var = tk.BooleanVar(value=False)
global_check = tk.Checkbutton(frame, text="Set Globally", variable=global_var)
global_check.grid(row=3, columnspan=2, pady=5)

# Load from file button
load_button = tk.Button(frame, text="Load from File", command=load_from_file)
load_button.grid(row=4, columnspan=2, pady=5)

# Submit button
submit_button = tk.Button(frame, text="Submit", command=on_submit)
submit_button.grid(row=5, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()