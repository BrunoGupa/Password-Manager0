from tkinter import *
from tkinter import messagebox
import random
#import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pasword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, string=password)
    #pyperclip.copy(password) #to copy the password but doesn't works in Ubuntu


# ---------------------------- SAVE PASSWORD ------------------------------- #

#Gets text in entry
def new_input():
    web_address = web_entry.get()
    mail_address = mail_entry.get()
    password = pass_entry.get()
    new_data = {
        web_address: {
            "email": mail_address,
            "password": password,
        }
    }

    if len(web_address) == 0 or len(password) == 0 or len(mail_address) == 0:
        messagebox.showerror(title="Epmty Field", message="Please fill all fields")
        empty_field = True
        return "", False

    save = messagebox.askokcancel(title="Password Manager", message=f"Are you sure to save the folowiong input?"
                                                          f" \n web: {web_address} \n user: {mail_address}"
                                                          f"\n password: {password} ")
    if save:
        web_entry.delete(0, 'end')
        mail_entry.delete(0, 'end')
        mail_entry.insert(0, "bruno.gupa@gmaill.com")
        pass_entry.delete(0, 'end')
    return new_data, save


def save_pass():
    new_data, save = new_input()
    if save:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating the new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving the updated data
                json.dump(data, data_file, indent=4)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50) #, bg=BLUE)  # bg is background

canvas = Canvas(width=200, height=200)#, bg=BLUE, highlightthickness=0)  # highlightthickness deletes the border
padlock = PhotoImage(file="logo.png")  # To read my file in tkinter package
canvas.create_image(100, 100, image=padlock)
#timer_text = canvas.create_text(103, 150, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)


#Labels
web_label = Label(text="Website:", font=("Arial", 12, "bold"))
web_label.grid(row=2, column=0)

mail_label = Label(text="Email/Username:", font=("Arial", 12, "bold"))
mail_label.grid(row=3, column=0)

pass_label = Label(text="Password:", font=("Arial", 12, "bold"))
pass_label.grid(row=4, column=0)


#Buttons
def action():
    pass

#calls action() when pressed
generate_password = Button(text="New Password", command=generate_pasword, font=("Arial", 10, "bold"), width=10)
generate_password.grid(row=4, column=2)

add_button = Button(text="Add", command=save_pass, font=("Arial", 12, "bold"), width=30)
add_button.grid(row=5, column=1, columnspan=2)


#Entries
web_entry = Entry(width=37)
web_entry.grid(row=2, column=1, columnspan=2)
web_entry.focus() #To focus the cursor in the entry


mail_entry = Entry(width=37)
#Add some text to begin with
mail_entry.insert(0, string="bruno.gupa@gmail.com")
mail_entry.grid(row=3, column=1, columnspan=2)

pass_entry = Entry(width=24)
pass_entry.grid(row=4, column=1)


window.mainloop()
