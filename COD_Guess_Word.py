from tkinter import *
import random
from PIL import Image, ImageTk
attempts= 5
answer_number = random.randint(0,10)
list_of_words = ['Warzone', 'Battlefield', 'Strategy', 'Survival',
                 'Combat', 'War', 'Ammo', 'Soldier', 'Hostilities',
                 'Rivalry']
answer = random.randint(0,10)
def check_answer():
    global attempts
    global text
    attempts -= 1


    try:
        guess = int(entry_of_guess.get())-1
    except:
        text.set("Invalid Entry Amigo! Type A Number!!!")
        entry_of_guess.delete(0, 'end')
    else:
        if guess == answer:
            text.set("Well Done Soldier, You Won! Mission Accomplished")
            btn_entry.pack_forget()
        elif attempts == 0:
            text.set("You Lose Maggot!! ")
            btn_entry.pack_forget()
        elif guess != answer:
            text.set("Try Again Soldier " + str(attempts) + " remaining")
            entry_of_guess.delete(0, 'end')




root = Tk()
root.title("WORD GAME")
root.geometry("1200x700")
im = Image.open('COD.png')
tkimage = ImageTk.PhotoImage(im)
myvar=Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)
root.minsize(width=750, height=350)
word_label = Label(root, text= "List of Words", font=("arial bold", 15), bg="gray72",
                   relief="groove", borderwidth=5)
word_label.pack(pady = 7) #grid(row=0, column=3, columnspan=1)#pack()

words = Label(root, text="1. Warzone, 2. Battlefield, "
                         "3. Strategy, 4. Survival, 5. Combat, 6. War, 7. Ammo, "
                         "8. Soldier, 9. Hostilities, 10. Rivalry", font=("comic sans",10,'bold')
              , bg="gray72",
              relief="raised", borderwidth=3)
words.pack(pady=7)

text = StringVar()
text.set("you have 5 attempts remaining! Good luck")

guess_entry = Label(root, text="Enter your Guess in 'Number' in below box Rookie: ", font=("comic sans", 15), bg="gray72",
                    relief="raised", borderwidth=3)
guess_entry.pack(pady=7)#side="left")#grid(row=4, column=0, columnspan=2)

entry_of_guess = Entry(root, width=20, borderwidth=4, bg="gray72",
                       relief="sunken")
entry_of_guess.pack(pady=40)#side="right")#grid(row=4, column=2, columnspan=2)

#Relief	This displays different types of borders like SUNKEN, RAISED, GROOVE, and RIDGE.
btn_entry = Button(root, text="Enter", command= check_answer, borderwidth=10,
                   relief="groove", bg="gray72")
btn_entry.pack(pady=7)#grid(row=5, column=0, columnspan=1)

btn_quit = Button(root, text="Quit", command=root.destroy, borderwidth=10,
                  relief="groove", bg="gray72")
btn_quit.pack(pady=7)#grid(row=5, column=2, columnspan=1)

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack(pady=7)

root.mainloop()