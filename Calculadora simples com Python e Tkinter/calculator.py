from tkinter import *
from tkinter import ttk



'''

Colors

white = '#FFFFFF'
black = '#000000'
gray = '808080'
red = '#FF0000'
green = '#08000'
blue = '#0000FF'
yellow = '#FFFF00'
orange = '#FF6000'
purple = '#6600FF'
dark_blue = '#1E2E5C'

'''

dark_blue = '#1E2E5C'
black = '#000000'
gray = '#808080'
orange = '#FF6000'
white = '#FFFFFF'

window = Tk()
window.title('Calculator_App')
window.geometry('235x310')
window.config(bg=black)

# Frames

screen_frame = Frame(window, width=235, height=50, bg=dark_blue)
screen_frame.grid(row=0, column=0)

body_frame = Frame(window, width=235, height=268)
body_frame.grid(row=1, column=0)


# Variable

values = ""

# Functions

def get_values(event):
    global values
    values = values + str(event)
    str_result.set(values)


def calc():
    global values
    result = eval(values)
    str_result.set(result)
    values = str(result)


def cls_screen():
    global  values
    values = ""
    str_result.set('')

# Labels

str_result = StringVar()

label = Label(screen_frame, textvariable=str_result, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=dark_blue, fg=white)
label.place(x=0, y=0)


# Buttons

b_1 = Button(body_frame, command=cls_screen, text='C', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(body_frame, command=lambda: get_values('%'), text='%', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(body_frame, command=lambda: get_values('/'), text='/', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(body_frame, command=lambda: get_values('7'), text='7', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(body_frame, command=lambda: get_values('8'), text='8', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(body_frame, command=lambda: get_values('9'), text='9', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(body_frame, command=lambda: get_values('*'), text='*', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(body_frame, command=lambda: get_values('4'), text='4', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(body_frame, command=lambda: get_values('5'), text='5', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(body_frame, command=lambda: get_values('6'), text='6', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(body_frame, command=lambda: get_values('-'), text='-', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(body_frame, command=lambda: get_values('1'), text='1', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(body_frame, command=lambda: get_values('2'), text='2', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(body_frame, command=lambda: get_values('3'), text='3', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(body_frame, command=lambda: get_values('+'), text='+', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(body_frame, command=lambda: get_values('0'), text='0', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(body_frame, command=lambda: get_values('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(body_frame, command=calc, text='=', width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


window.mainloop()
