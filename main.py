from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

language_data = pandas.read_csv("./data/japanese_words.csv")
data_dict = {row.Japanese: row.English for (index, row) in language_data.iterrows()}
words_list = language_data["Japanese"].tolist()

random_word = random.choice(words_list)
missed_words = {each_word: data_dict[each_word] for each_word in words_list}


def checked_word():
    global missed_words
    words_list.remove(random_word)
    card_flip_word()
    window.after(3000, card_flip_eng)

    # words_to_learn = pandas.DataFrame.from_dict(missed_words, orient="index")
    # words_to_learn.to_csv("./data/words_to_learn.csv", index=False)


def crossed_word():
    card_flip_word()
    window.after(3000, card_flip_eng)


def card_flip_eng():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(japanese_title, text="English", fill="white")
    canvas.itemconfig(japanese_word, text=data_dict[random_word], fill="white")


def card_flip_word():
    global random_word
    random_word = random.choice(words_list)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(japanese_title, text="Japanese", fill="black")
    canvas.itemconfig(japanese_word, text=random_word, fill="black")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=1, column=1, columnspan=2)

window.after(3000, card_flip_eng)

japanese_title = canvas.create_text(400, 150, text="Japanese", font=("Arial", 40, "italic"))
japanese_word = canvas.create_text(400, 263, text=random_word, font=("Arial", 60, "bold"))

checkmark = PhotoImage(file="./images/right.png")
checkmark_button = Button(image=checkmark, highlightthickness=0, command=checked_word)
checkmark_button.grid(row=2, column=2)

crossmark = PhotoImage(file="./images/wrong.png")
crossmark_button = Button(image=crossmark, highlightthickness=0, command=crossed_word)
crossmark_button.grid(row=2, column=1)

window.mainloop()
