from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

USER_EMAIL = 'vitisman@gmail.com'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title='Ups', message='Please make sure that all the fields are filled!')

    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}'
    #                                                           f'\nPassword: {password} \nIs it ok to save?')
    #     if is_ok:
    # else:
    #     with open('data.txt', 'a') as data:
    #         data.write(f'{website}/{email}/{password}\n')
    #         password_entry.delete(0, END)
    #         web_entry.delete(0, END)
    else:
        try:
            with open('data.json', 'r') as data_file:
                # read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- search ------------------------------- #
def search():
    website = web_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='File not found')

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']

            pyperclip.copy(password)  # this will copy the password to the clipboard

            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword:{password}'
                                                       f'\nPassword has been copied to the clipboard ready to use')

        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} found')
# ---------------------------- Open wanted programs ------------------------------- #
# TODO: open programs and access to pages with this program

# ---------------------------- ENCRYPT ------------------------------- #
# TODO: caesar cypher
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('My Password Manager')
window.configure(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

# labels
web_label = Label(text='Website:')
web_label.grid(column=1, row=2)
email_label = Label(text='Email/Username:')
email_label.grid(column=1, row=3)
password_label = Label(text='Password:')
password_label.grid(column=1, row=4)

web_entry = Entry(width=33)
web_entry.grid(column=2, row=2)
web_entry.focus()  # makes cursor start here
email_entry = Entry(width=47)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, USER_EMAIL)
password_entry = Entry(width=33)
password_entry.grid(column=2, row=4, )
search_button = Button(text='Search website', command=search)
search_button.grid(column=3, row=2, sticky='w')
generate_button = Button(text='Gen Password ', command=password_generator)
generate_button.grid(column=3, row=4, sticky='w')
add_password_button = Button(text='Add', width=40, command=save_pass)
add_password_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
