from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

#Gets text in entry
def new_web_address():
    web_address = web_entry.get()
    mail_address = mail_entry.get()
    password = pass_entry.get()

    web_entry.delete(0, 'end')
    mail_entry.delete(0, 'end')
    mail_entry.insert(0, "bruno.gupa@gmaill.com")
    pass_entry.delete(0, 'end')
    return web_address + "   |   " + mail_address + "   |   " + password + "\n"

def save_pass():
    f = open("passwords.txt", "a")
    string = new_web_address()
    f.write(string)
    f.close()

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
generate_password = Button(text="New Password", command=action, font=("Arial", 10, "bold"), width=10)
generate_password.grid(row=4, column=2)

add_button = Button(text="Add", command=save_pass, font=("Arial", 12, "bold"), width=30)
add_button.grid(row=5, column=1, columnspan=2)


#Entries
web_address = StringVar()
web_entry = Entry(textvariable=web_address, width=37)
web_entry.grid(row=2, column=1, columnspan=2)
web_entry.focus() #To focus the cursor in the entry


mail_address = StringVar()
mail_entry = Entry(textvariable=mail_address, width=37)
#Add some text to begin with
mail_entry.insert(0, string="bruno.gupa@gmail.com")
mail_entry.grid(row=3, column=1, columnspan=2)

password = StringVar()
pass_entry = Entry(textvariable=password, width=24)
pass_entry.grid(row=4, column=1)



window.mainloop()
