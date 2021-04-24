from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global rep
    rep = 0
    canvas.itemconfig(time_text, text="25:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def time_start():
    global rep
    rep += 1
    work = WORK_MIN * 1
    short_break = SHORT_BREAK_MIN * 1
    long_break = LONG_BREAK_MIN * 1

    if rep %8 == 0:
        count_down(long_break)
        title_label.config(text="break", bg=YELLOW, fg=RED, font=(FONT_NAME, 35, "bold"))
        rep = 0
    elif rep %2 == 0:
        count_down(short_break)
        title_label.config(text="break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 35, "bold"))
    else:
        count_down(work)
        title_label.config(text="work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    

    if count >= 0:
        mins, secs = divmod(count, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        canvas.itemconfig(time_text, text=timer)
        buttun_start.config(state="disabled")
    if count == 0:
        check_label.config(text="✔")
        buttun_start.config(state="active", bg=GREEN)
        time_start()
    if count != 0:
        window.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=YELLOW)

# --------------photo handaling-------------------- #
photo_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
canvas.create_image(150, 150, image=photo_img)
canvas.grid(row=1, column=1)
time_text = canvas.create_text(150, 150, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))

# -------------------- text handling --------------- #
title_label = Label(text="timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)

check_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
check_label.grid(row=2, column=1)

# ------------------- buttuns --------------------- #

buttun_start = Button(bg=GREEN, highlightthickness=0, width=15, height=5, text="start", command=time_start)
buttun_start.grid(padx=20, pady=20, row=2, column=0)

buttun_reset = Button(bg=RED, highlightthickness=0, width=15, height=5, text="reset", command=timer_reset)
buttun_reset.grid(padx=20, pady=20, row=2, column=2)

window.mainloop()
