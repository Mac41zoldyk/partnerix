import csv, os, re, webbrowser
import tkinter as tk
from tkinter import Entry, Label, Button, messagebox

def validate_email(email):
    # Simple email validation using regular expression
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return pattern.match(email)

def save_to_csv(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)

def on_confirm_button_click(name_entry, email_entry):
    name = name_entry.get()
    email = email_entry.get()

    if not name or not email:
        messagebox.showerror("Error", "Please enter both name and email.")
        return

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format. Please enter a valid email.")
        return

    # Save information to CSV file
    csv_filename = os.path.join('C:/Users/Shruti/Downloads', 'user_data.csv')
    save_to_csv(csv_filename, [name, email])

    # Redirect to a certain site (replace 'https://example.com' with the desired website)
    website_url = 'https://www.wikipedia.org/'
    webbrowser.open(website_url)

def create_gui():
    window = tk.Tk()
    window.title("User Information Entry")

    # Labels
    Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    Label(window, text="Email:").grid(row=1, column=0, padx=10, pady=5)

    # Entry fields
    name_entry = Entry(window)
    name_entry.grid(row=0, column=1, padx=10, pady=5)
    
    email_entry = Entry(window)
    email_entry.grid(row=1, column=1, padx=10, pady=5)

    # Confirm button
    confirm_button = Button(window, text="Confirm", command=lambda: on_confirm_button_click(name_entry, email_entry))
    confirm_button.grid(row=2, column=0, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
