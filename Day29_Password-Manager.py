from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- CONSTANTS ---------------------------------- #
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list = [choice(letters) for _ in range(randint(8, 10))]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    # "".join(shuffle(password_list))
    shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # Variables
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops", message = "Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered: \n"
                                                      f"Email: {email}\n "
                                                      f"Password: {password}\n"
                                                      f"Is it ok to save?")

        if is_ok:
            # Write data to file
            f = open("password_data.text", "a")
            f.write(f"{website} | {email} | {password} \n")
            f.close()
            # Alternative (closes file automatically):
            # with open("password_data.text", "a") as data_file:
            #   data_file.write(f"...")

            # Clear entry widgets
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")



# ---------------------------- UI SETUP ------------------------------- #

# Create window using Tkinter
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Add logo image to window using Canvas widget
canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
logo_img = PhotoImage(file="Day29_logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

# Create text widgets
website_label = Label(text = "Website:")
website_label.grid(row = 1,column = 0)

username_label = Label(text = "Email/Username:")
username_label.grid(row = 2, column = 0)

password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)

# Create Entry widgets
website_entry = Entry(width = 35)
website_entry.grid(row = 1, column = 1, columnspan = 2, sticky = W+E, padx = 2)
    # Add cursor in website_entry widget
website_entry.focus()

email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, columnspan = 2, sticky = W+E, padx = 2)
    # Add email for user experience
email_entry.insert(0, "ameliabegemann@gmail.com")

password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1, sticky = W+E, padx = 2)

# Create Button widgets
generate_button = Button(text = "Generate Password", command=generate_password)
generate_button.grid(row = 3, column = 2, sticky = W, padx = 2)

add_button = Button(width = 36, text = "Add", command=save)
add_button.grid(row = 4, column = 1, columnspan = 2, sticky = W+E, padx= 2)

# Need to align widgets

window.mainloop()
