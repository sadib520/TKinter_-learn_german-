from tkinter import *
from customtkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

current_card = {}
to_learn = {}

try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("german_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    Window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    a = current_card["German"]
    canvas.itemconfig(canvs_title, text="German")
    canvas.itemconfig(canvs_text, text=a)
    canvas.itemconfig(canvs_text2, text="")
    flip_timer =  Window.after(3000, func=flip_card)


def flip_card():
    global current_card
    b = current_card["English"]
    c = current_card["Bengali"]
    canvas.itemconfig(canvs_title, text="English")
    canvas.itemconfig(canvs_text, text=b)
    canvas.itemconfig(canvs_text2, text=c)

def is_known():
    global current_card
    to_learn.remove(current_card)
    d = pd.DataFrame(to_learn)
    d.to_csv("words_to_learn.csv", index=FALSE)
    next_card()



Window = CTk()
Window.title("Flash Card Application ! ")
Window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
flip_timer = Window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=front_card)
canvs_title = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
canvs_text = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvs_text2 = canvas.create_text(400, 370, font=(FONT_NAME, 30))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)



wrong_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=wrong_image, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)


next_card()

Window.mainloop()