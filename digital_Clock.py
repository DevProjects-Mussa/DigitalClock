from tkinter import *
import time
clk = Tk()
clk.title("Clock")
clk.geometry("1350x700+0+0")  # width, height, x_axis, y_axis
clk.config(bg="#1E1E3F")   # This is the background color of the whole GUI(You can choose any you want)


def clock():
    hr = str(time.strftime('%H'))
    minutes = str(time.strftime('%M'))
    sec = str(time.strftime('%S'))
    print(hr, minutes, sec)
    if int(hr) > 12 and int(minutes) > 0:
        Ib_dt.config(text="PM")
    if int(hr) > 12:
        hr = str(int(int(hr)-12))

    Ib_hr.config(text=hr)
    Ib_minutes.config(text=minutes)
    Ib_sec.config(text=sec)

    Ib_hr.after(200, clock)

# Hours(GUI tag or block showing the hours)


Ib_hr = Label(clk, text="12", font=("Times 20 bold", 75, "bold"), bg="black", fg="#00FF00")
Ib_hr.place(x=350, y=200, width=150, height=150)

Ib_hr_txt = Label(clk, text="HOUR", font=("Times  20 bold", 20, "bold"), bg="black", fg="#00FF00")
Ib_hr_txt.place(x=350, y=360, width=150, height=50)

# Minutes(GUI tag or block showing the minutes)

Ib_minutes = Label(clk, text="12", font=("Times 20 bold", 75, "bold"), bg="black", fg="#00FF00")
Ib_minutes.place(x=520, y=200, width=150, height=150)

Ib_minutes_txt = Label(clk, text="MINUTES", font=("Times  20 bold", 20, "bold"), bg="black", fg="#00FF00")
Ib_minutes_txt.place(x=520, y=360, width=150, height=50)

# Seconds(GUI tag or block showing the seconds)
Ib_sec = Label(clk, text="12", font=("Times 20 bold", 75, "bold"), bg="black", fg="yellow")
Ib_sec.place(x=690, y=200, width=150, height=150)

Ib_sec_txt = Label(clk, text="SECONDS", font=("Times  20 bold", 20, "bold"), bg="black", fg="yellow")
Ib_sec_txt.place(x=690, y=360, width=150, height=50)

# Day time(GUI tag or block showing what time of the day is, noon(pm) or am(morning))
Ib_dt = Label(clk, text="AM", font=("Times 20 bold", 75, "bold"), bg="black", fg="#D3D3D3")
Ib_dt.place(x=860, y=200, width=150, height=150)

Ib_dt_txt = Label(clk, text="NOON", font=("Times  20 bold", 20, "bold"), bg="black", fg="#D3D3D3")
Ib_dt_txt.place(x=860, y=360, width=150, height=50)

clock()

clk.mainloop()
