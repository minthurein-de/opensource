from tkinter import *
import math

# Constants
FONT = ('courier',30,'bold')
WORK_MIN = int(0.2 * 60)
SHORT_BREAK = int(0.1 * 60)
LONG_BREAK = int(0.15 * 60)
c = 0
shift = 0
timer = None
timer_running = False
current_timer = 0

def pomodoro():
    global c
    if shift % 2 == 1:
        c += 1
        pomodoro_count.config(text=f"TOTAL POMODORO({c}/4)\nPROTECT YOUR POMODORO!")
    elif shift % 8 == 0:
        c = 0

def start_timer():
    global shift
    shift += 1
    pomodoro()
    if shift % 8 == 0:
        count_down(LONG_BREAK)
        window.config(bg="palegreen")
        canvas.config(bg='palegreen')
        pomodoro_count.config(bg='palegreen')
        title_label.config(text="LONG BREAK",bg='palegreen')
    elif shift % 2 == 0:
        count_down(SHORT_BREAK)
        window.config(bg="paleturquoise")
        canvas.config(bg='paleturquoise')
        pomodoro_count.config(bg='paleturquoise')
        title_label.config(text="SHORT BREAK",bg='paleturquoise')
    else:
        count_down(WORK_MIN)
        window.config(bg="khaki")
        canvas.config(bg='khaki')
        pomodoro_count.config(bg='khaki')
        title_label.config(text="HUSTLE TIME",bg='khaki')

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()

def start_or_pause():
    global pause, timer_running, current_timer
    if not timer_running:
        if current_timer > 0:
            count_down(current_timer)
        else:
            start_timer()
        timer_running = True
        start_button.config(text='PAUSE')
    else:
        pause_timer()
        timer_running = False
        start_button.config(text='START')
        
def get_current_time():
    time_str = canvas.itemcget(timer_text,'text')
    m, s = map(int, time_str.split(":"))
    return m*60 + s

def pause_timer():
    global current_timer, timer
    if timer:
        window.after_cancel(timer)
    current_timer = get_current_time()

def reset_timer():
    global shift, c, current_timer, timer_running
    if timer:
        window.after_cancel(timer)
    window.config(bg="khaki")
    canvas.config(bg='khaki')
    pomodoro_count.config(bg='khaki')
    canvas.itemconfig(timer_text,text='00:00')
    title_label.config(text='TOMATO TIMER',bg='khaki')
    shift = 0
    c = 0
    current_timer = 0
    timer_running = False
    start_button.config(text='START')
    pomodoro_count.config(text=f"TOTAL POMODORO({c}/4)\nPROTECT YOUR POMODORO!")

window = Tk()
window.title("Pomodoro Timer")
window.geometry('846x680')
window.resizable(0,0)
window.config(padx=20,pady=20,bg='khaki')

canvas = Canvas(width=512,height=512,bg='khaki',highlightthickness=0)
img = PhotoImage(file='pomodoro2.png')
canvas.create_image(256,256,image=img)
timer_text = canvas.create_text(256,256,text='00:00',font=('courier',50,'bold'),fill='khaki')
canvas.moveto(timer_text,150,250)
canvas.grid(row=1,column=1)

title_label = Label(text='TOMATO TIMER',font=('courier',50,'bold'),bg='khaki',fg='tomato')
title_label.grid(row=0,column=1)

start_button = Button(text='Start',font=FONT,fg='khaki',bg='tomato',command=start_or_pause,highlightthickness=0)
start_button.grid(row=2,column=0)

reset_button = Button(text='Reset',font=FONT,fg='khaki',bg='tomato',highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

pomodoro_count = Label(text='TOTAL POMODORO(0/4)\nPROTECT YOUR POMODORO!',font=('courier',15,'bold'),bg='khaki',fg='tomato')
pomodoro_count.grid(row=2,column=1)












window.mainloop()
