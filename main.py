from tkinter import *
import string
import random
import pyperclip

#the main window
root = Tk()
root.title('Password Generator')
root.geometry('580x700+500+60')
root.resizable(False,False)
root.configure(bg='grey')

Font = ('arial',12)
extra1 = Label(root, text='                                                                                                                                                                                                ', font=('Times New Roman',10), bg='gray20', fg='White')
extra1.grid()


def generator():
    passwordField.delete(0, END) # This clears the existing text in the field

    passwordField.place(x=100, y=480)
    password_lenght = int(lenght_Box.get())

    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_char = string.punctuation

    all = small_alphabets+capital_alphabets+numbers+special_char

    if choice.get() == 1:
        password = ''.join(random.sample(small_alphabets, password_lenght))

    elif choice.get() == 2:
        password = ''.join(random.sample(small_alphabets + capital_alphabets, password_lenght))

    elif choice.get() == 3:
        password = ''.join(random.sample(all, password_lenght))

    passwordField.insert(0, password)

    result = Label(root, text='Here’s your secure password:', font=('arial',18),bg='gray20', fg='White')
    result.place(x=120, y=425)

    copyButton = Button(root, text='Copy', font=('arial',11,'bold'), bg='gray20', fg='white', command=copy())
    copyButton.place(x=425, y=477)

    safe = Label(root, text='Stay Safe!💪🛡️', font=('arial',38),bg='gray20', fg='White')
    safe.place(x=100, y=560)


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)



passwordLabel = Label(root, text='  Welcome to the Ultimate Password Generator! 🔐  ', font=('Times New Roman',21), bg='gray20', fg='White')
passwordLabel.grid()
extra2 = Label(root, text='                                                                                                                                                                                                ', font=('Times New Roman',10), bg='gray20', fg='White')
extra2.grid()

intro1 = Label(root, text='Let’s create the perfect password! What level of security do you need?', font=Font,bg='grey', fg='White')
intro1.place(x=20, y= 100)

choice = IntVar()



weakradiobutton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font, bg='grey', fg='White', selectcolor='#636363')
weakradiobutton.place(x=25, y=140)
weak = Label(root, text=': Quick and easy, but not very secure. (Perfect for temporary use)', font=Font,bg='grey', fg='White')
weak.place(x=97, y= 142)

mediumradiobutton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font, bg='grey', fg='White',selectcolor='#636363')
mediumradiobutton.place(x=25, y=170)
medium = Label(root, text=': A good balance of strength and convenience.', font=Font,bg='grey', fg='White')
medium.place(x=111, y=172)

strongradiobutton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font, bg='grey', fg='White', selectcolor='#636363')
strongradiobutton.place(x=25, y=200)
strong = Label(root, text=': Highly secure! No one will be cracking this anytime soon.', font=('arial',12),bg='grey', fg='White')
strong.place(x=111, y= 202)

lengthLabel = Label(root, text='Set password length (8-20)   :', font=Font, bg='grey',fg='white')
lengthLabel.place(x=30,y=235)
lenght_Box = Spinbox(root, from_=5, to=20, width=5, font=Font, bg='white', fg='gray20')
lenght_Box.place(x=250,y=237)

generateButton = Button(root, text='\n',font=('arial,14,bold'),bg='gray20',fg='white', width=20, command=generator)
generateButton.place(x=150,y=300)
generateLabel = Label(root, text='GENERATE', font=('Times New Roman',20,'bold'), bg='gray20',fg='white')
generateLabel.place(x=187,y=312)

backgroung_image = PhotoImage(file="D:/backgroung.png")
myimage = Label(image=backgroung_image, bg='grey')
myimage.place(x=50, y=400)

passwordField = Entry(root, width=35, bd=2, font=Font)







root.mainloop()
