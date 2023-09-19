import random
from tkinter import *

EMAIL_TEXT = "symolyson@gmail.com"
from tkinter import messagebox
import json


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    text = text_box.get()
    password_text = text_box_password.get()
    email_text = text_box_email.get()
    new_data = {
        text: {
            "email": email_text,
            "password": password_text,
        }
    }

    if len(text) == 0:
        messagebox.showerror(title="WARNING", message="please input a valid website name")
    elif len(email_text) == 0:
        messagebox.showerror(title="WARNING", message="please input a valid email")
    elif len(password_text) == 0:
        messagebox.showerror(title="WARNING", message="please input a valid password")
    else:
        is_ok = messagebox.askokcancel(title=text,
                                       message=f"you entered:{email_text}, {password_text}.Do you want to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                text_box.delete(0, END)
                text_box_password.delete(0, END)
                messagebox.showinfo(message="DONE")


# ---------------------------- UI SETUP ------------------------------- #


def generate_password():
    text_box_password.delete(0, END)
    """generate an 8 characters password"""
    letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I'
        , 'i', 'J', 'j', 'K', 'k', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
               'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['#', '!', '@', '&', '(', ')', '*']
    data = [
        ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I'
            , 'i', 'J', 'j', 'K', 'k', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
         'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['#', '!', '@', '&', '(', ')', '*'],

    ]
    password_length = random.randint(6, 12)
    password = []
    while len(password) < password_length:
        data_list = random.choice(data)
        data_list_choice = data_list[random.randint(0, len(data_list) - 1)]
        password.append(data_list_choice)

    random.shuffle(password)
    password = (''.join(password))
    text_box_password.insert(0, password)


# ----------------------------- SEARCH PASSWORD-------------------------#
def search_password():
    webpage_name = text_box.get().lower()
    try:
        with open("data.json", mode="r") as data_file:
            # load the json dictionary
            data = json.load(data_file)
            # access the password using keyvalues
            password = data[webpage_name]["password"].lower()
            email= data[webpage_name]["email"].lower()
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="Oops, looks like the file does not exist! ")
    except KeyError:
        messagebox.showerror(title="ERROR", message="Oops, please input a valid website name! ")
    else:
        # show password to user
        messagebox.askokcancel(title="PASSWORD", message=f"your password for {webpage_name} is: {password} :email:{email}")


window = Tk()
window.config(pady=50, padx=50)
window.title("PASSWORD MANAGER")
canvas = Canvas(width=200, height=200)
pad_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pad_image)
canvas.grid(column=1, row=0)
website_label = Label()
website_label["text"] = "Website: "
website_label.grid(row=1, column=0)
text_box = Entry()
text_box.config(width=35)
text_box.focus()
text_box.grid(row=1, column=1, columnspan=1)

email_label = Label()
email_label["text"] = "Email/Username: "
email_label.grid(row=2, column=0)
text_box_email = Entry()
text_box_email.config(width=35)
text_box_email.insert(0, EMAIL_TEXT)

text_box_email.grid(row=2, column=1, columnspan=1)

password_label = Label()
password_label["text"] = "password: "
password_label.grid(row=3, column=0)

text_box_password = Entry()
text_box_password.config(width=34)

text_box_password.grid(row=3, column=1)

generate_button = Button()
generate_button.config(text="Generate password", command=generate_password, width=14)
generate_button.grid(row=3, column=2)

add_button = Button()
add_button.config(text="Add", command=add_data, width=45, padx=0, pady=0)
add_button.grid(row=4, column=1, columnspan=3)

add_search_button = Button()
add_search_button.config(text="Search", width=14, command=search_password)
add_search_button.grid(row=1, column=2)

window.mainloop()
