from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def time_start():
    count_down(1500)


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    if count >= 0:
        mins, secs = divmod(count, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        window.after(1000, count_down, count - 1)
        canvas.itemconfig(time_text, text=timer)
        buttun_start.config(state="disabled")
    if count == 0:
        check_label.config(text="✔")
        buttun_start.config(state="active", bg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=YELLOW)

# --------------photo handaling-------------------- #
photo_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
canvas.create_image(150, 150, image=photo_img)
canvas.grid(row=1, column=1)
time_text = canvas.create_text(150, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# -------------------- text handling --------------- #
title_label = Label(text="timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)

check_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
check_label.grid(row=2, column=1)

# ------------------- buttuns --------------------- #

buttun_start = Button(bg=GREEN, highlightthickness=0, width=15, height=5, text="start", command=time_start)
buttun_start.grid(padx=20, pady=20, row=2, column=0)

buttun_reset = Button(bg=RED,highlightthickness=0, width=15, height=5, text="reset")
buttun_reset.grid(padx=20, pady=20, row=2, column=2)

window.mainloop()
