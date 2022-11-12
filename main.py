from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#------------------------------ CONSTANTS -----------------------------------#
DARK_GREEN = "#66BFBF"
GREEN = "#EAFFF6"
FONT = ("Helvetica", 10, "bold")
left = "w"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generate():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    char_list = [random.choice(letters) for _ in range(nr_letters)]
    num_list = [random.choice(numbers) for _ in range(nr_numbers)]
    sym_list = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = char_list + num_list + sym_list
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    psswd_entry.delete(0, END)
    psswd_entry.insert(0, password)
    messagebox.showinfo(title="COPIED", message="Password automatically copied to clipboard")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_to_file():

    website = website_entry.get()
    email = email_entry.get()
    password = psswd_entry.get()
    new_data = {website:
                    {
                        "email":email,
                        "password": password
                    }
                }

    if len(website) == 0 or len(password) == 0 :
        messagebox.showerror(title="Oops", message="Please fill out all the fields")

    else:

        try:

            with open("passwords.json", mode="r") as file:
                #reading old data
                data = json.load(file)

        except KeyError:

            with open("passwords.json", mode="w") as file:
                # making new file as it doesn't exist
                json.dump(new_data, file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)
            with open("passwords.json", mode="w") as file:
                # saving new data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "yeshavyas27@gmail.com")
            psswd_entry.delete(0, END)

# ---------------------------- SEARCH THROUGH FILE ------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(500, 500)
window.config(bg=GREEN)

canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
#below are x and y coordinates
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1,padx=20, pady=20)


website_label = Label(text="Website:", fg=DARK_GREEN, font=FONT, bg=GREEN)
website_label.grid(row=1, column=0, padx=5, pady=5)

email_label = Label(text="Email/Username:", fg=DARK_GREEN, font=FONT, bg=GREEN)
email_label.grid(row=2, column=0, padx=5, pady=5)

psswd_label = Label(text="Password:", fg=DARK_GREEN, font=FONT, bg=GREEN)
psswd_label.grid(row=3, column=0, padx=5, pady=5)


website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky=left)

email_entry = Entry(width=59)
email_entry.insert(0, "yeshavyas27@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky=left)

psswd_entry = Entry(width=40)
psswd_entry.grid(row=3, column=1, sticky=left)

generate_psswd = Button(text="Generate Password", width =14, command=password_generate)
generate_psswd.grid(row=3, column=2)

add_button = Button(text="Add", width=49, command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky=left, pady=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)


window.mainloop()



