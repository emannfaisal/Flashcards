BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

data=pandas.read_csv("C:\\Users\\Hp\\Downloads\\New folder\\New folder\data\\french_words.csv")
to_learn=data.to_dict(orient="records")
current_card={}
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_img)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("New folder/data/new_words.png",index=False)
    next_card()

window=Tk()
window.title("The flash card game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)
canvas=Canvas(width=800, height=526)
front_img=PhotoImage(file="C:\\Users\\Hp\\Downloads\\New folder\\New folder\\images\\card_front.png")
back_img=PhotoImage(file="C:\\Users\\Hp\\Downloads\\New folder\\New folder\\images\\card_back.png")
card_background=canvas.create_image(400,263,image=front_img)
card_title=canvas.create_text(400,150,text="Label",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="Word",font=("Arial",40,"italic"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="C:\\Users\\Hp\\Downloads\\New folder\\New folder\\images\\wrong.png")
no_button=Button(image=cross_image,highlightthickness=0,command=next_card)
no_button.grid(row=1,column=0)
tick_image=PhotoImage(file="C:\\Users\\Hp\\Downloads\\New folder\\New folder\\images\\right.png")
yes_button=Button(image=tick_image,highlightthickness=0,command=is_known)
yes_button.grid(row=1,column=1)

next_card()
window.mainloop()
