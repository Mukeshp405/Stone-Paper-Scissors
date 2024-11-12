from tkinter import *
import random

def play():
    # Frame 1
    frame1 = Frame(root, bg="gray30", width=600, height=600)
    frame1.place(x=0, y=0)

    # Choose your Symbol
    text_choose = Label(frame1, text="Choose your symbol...", font="Arial 25 bold", bg="gray30", fg="burlywood1")
    text_choose.place(x=120, y=0)

    def rock_selected():
        selection("rock")

    def paper_selected():
        selection("paper")

    def scissor_selected():
        selection("scissor")

    def create_button_and_label(img_path, text, x, y, command):
        img = PhotoImage(file=img_path).subsample(2, 2)
        btn = Button(frame1, image=img, bg="gray30", activebackground="gray30", command=command)
        btn.image = img  # Store reference to avoid garbage collection
        btn.place(x=x, y=y)
        
        lbl = Label(frame1, text=text, font="Arial 15 bold", bg="gray30", fg="IndianRed2" if text == "Rock" else "yellow" if text == "Paper" else "skyblue")
        lbl.place(x=x+90, y=y-30)

    # Buttons for user selection
    create_button_and_label("img/rock.png", "Rock", 60, 90, rock_selected)
    create_button_and_label("img/paper.png", "Paper", 310, 90, paper_selected)
    create_button_and_label("img/scissors.png", "Scissor", 180, 360, scissor_selected)

# Exit game
def quit():
    root.quit()

# Selection of (Stone, Paper, Scissor)
def selection(user_choice):
    # Frame 2
    frame2 = Frame(root, width=600, height=600, bg="gray30")
    frame2.place(x=0, y=0)

    # You Select
    Label(frame2, text="You Select!", bg="gray30", font="Arial 20 bold", fg="burlywood1").place(x=70, y=160)
    # Computer Select
    Label(frame2, text="Computer Select!", bg="gray30", font="Arial 20 bold", fg="burlywood1").place(x=350, y=160)

    # Image path dictionary
    images = {
        "rock": "img/rock.png",
        "paper": "img/paper.png",
        "scissor": "img/scissors.png"
    }

    # User selection image
    user_img = PhotoImage(file=images[user_choice]).subsample(2, 2)
    user_label = Label(frame2, image=user_img, bg="gray30")
    user_label.image = user_img
    user_label.place(x=50, y=230)

    # Random computer selection
    computer_choice = random.choice(["rock", "paper", "scissor"])
    computer_img = PhotoImage(file=images[computer_choice]).subsample(2, 2)
    computer_label = Label(frame2, image=computer_img, bg="gray30")
    computer_label.image = computer_img
    computer_label.place(x=350, y=230)

    # Display result based on choices
    result = determine_winner(user_choice, computer_choice)
    Label(frame2, text=result, bg="gray30", font="Arial 33 bold", fg="pink").place(x=190, y=10)

    # Reset Button
    reset_btn = Button(frame2, text="Reset", font="Arial 15 bold", relief=RAISED, borderwidth=5, command=play)
    reset_btn.place(x=170, y=520)

    # Quit Button
    quit_btn = Button(frame2, text="Quit", font="Arial 15 bold", relief=RAISED, borderwidth=5, command=quit)
    quit_btn.place(x=380, y=520)

# Display the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "rock" and computer == "scissor") or (user == "paper" and computer == "rock") or (user == "scissor" and computer == "paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def rock_selected():
    selection("rock")

def paper_selected():
    selection("paper")

def scissor_selected():
    selection("scissor")


root = Tk()
root.minsize(600, 600)
root.maxsize(600, 600)
root.title("Rock Paper Scissor")

# Title logo
title_logo = PhotoImage(file="img/title_logo.png")
root.iconphoto(True, title_logo)

# background image
bg_img = PhotoImage(file="img/bg_img.png")
bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0)

# logo
logo_img = PhotoImage(file="img/logo.png")
logo_resize = logo_img.subsample(2, 2)
logo_label = Label(root, image=logo_resize, bg="white")
logo_label.place(x=180, y=150)

# Start Button
start_btn = Button(root, text="Start", font="Arial 20 bold", relief=RAISED, borderwidth=5, bg="gray30", fg="white", command=play)
start_btn.place(x=265, y=420)


root.mainloop()