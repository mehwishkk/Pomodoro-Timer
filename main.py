from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer =None

window = Tk()
window.title("Pomodoro")
window.config(padx = 100,pady =50, bg = YELLOW)
# ---------------------------- TIMER RESET ------------------------------- # 
timer_label = Label(text = "Timer", fg = GREEN,bg = YELLOW, font=(FONT_NAME,25,'bold'))
timer_label.grid(column = 1, row =0)

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = '00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count>0:
       global timer
       timer= window.after(1000,count_down,count-1)
# ---------------------------- UI SETUP ------------------------------- #


canvas = Canvas(width=200,height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = 'tomato.png')
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text = '00:00',fill='white', font = (FONT_NAME,35,'bold'))
canvas.grid(column = 1, row =1)



def reset():
    print('reset button')
button_start = Button(text="Start", command = start_timer)

button_start.grid(column=0,row=3)

button_end = Button(text="Reset", command = reset_timer)
button_end.grid(column=2,row=3)
window.mainloop()
