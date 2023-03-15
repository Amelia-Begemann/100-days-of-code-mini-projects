from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
# constants are from colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
count_timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global count_timer
    global reps
    window.after_cancel(count_timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #titel_label "Timer"
    timer.config(text="Timer", fg=fg)
    #reset checkmarks
    checkmarks_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    # If it's the 1st/3rd/5th/7th rep
    if reps % 2 != 0:
        timer.config(text ="Work",  fg = GREEN)
        count_down(work_sec)
    # If it is the 8th rep:
    elif reps == 8:
        timer.config(text ="Break", fg = RED)
        count_down(long_break_sec)
    #If it is the 2nd/4th/6th rep
    elif reps % 2 == 0:
        timer.config(text ="Break", fg = PINK)
        count_down(short_break_sec)
    else:
        print("Error")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    global count_timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        count_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += checkmark
            checkmarks_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# window.after(1000,)

fg = GREEN
checkmark="✔"

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# We want image in the middle so we give a width and height of half of the canvas size
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

# Create "Timer" label
timer = Label(text="Timer",fg=fg, bg=YELLOW, font=(FONT_NAME,40,"bold"))
timer.grid(row=0,column=1)

start_button = Button(width=5, text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(width=5, text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2,column=2)

checkmarks_label = Label(text="",fg=fg, bg=YELLOW, highlightthickness=0)
checkmarks_label.grid(row=3,column=1)


window.mainloop()