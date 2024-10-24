import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def get_git_config_value(key, global_scope=False):
    scope = "--global" if global_scope else "--local"
    try:
        result = subprocess.run(
            ["git", "config", scope, key],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Could not get {key}. Error: {e}")
        return None

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

def load_initial_config():
    # Load initial Git configuration with global scope
    email = get_git_config_value("user.email", global_scope=True)
    username = get_git_config_value("user.name", global_scope=True)

    print(f"Loaded email: {email}, username: {username}")  # Debug prints

    # Update entry fields if values are found
    if email:
        email_entry.delete(0, tk.END)
        email_entry.insert(0, email)
    if username:
        username_entry.delete(0, tk.END)
        username_entry.insert(0, username)

def load_from_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not filename:
        return
    try:
        with open(filename, 'r') as file:
            config = {}
            for line in file:
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()

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

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the file: {e}")

def on_submit():
    email = email_entry.get().strip()
    username = username_entry.get().strip()
    global_scope = global_var.get()

    if not email or not username:
        messagebox.showerror("Error", "Email and Username fields cannot be empty.")
        return

    set_git_email(email, global_scope)
    set_git_username(username, global_scope)

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

# Global scope checkbox
global_var = tk.BooleanVar(value=True)  # Default to global settings
global_check = tk.Checkbutton(frame, text="Set Globally", variable=global_var)
global_check.grid(row=3, columnspan=2, pady=5)

# Load from file button
load_button = tk.Button(frame, text="Load from File", command=load_from_file)
load_button.grid(row=4, columnspan=2, pady=5)

# Submit button
submit_button = tk.Button(frame, text="Submit", command=on_submit)
submit_button.grid(row=5, columnspan=2, pady=10)

# Load initial configuration
load_initial_config()

# Start the GUI event loop
root.mainloop()