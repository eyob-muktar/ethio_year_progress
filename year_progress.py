import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter.constants import *
import sys
from datetime import date

DAYDIFFERENCE=2810 #manually calculated day difference b/n eth & gregorian calender
DAYSINAYEAR=365
MONTHS=[31,28,31,30,31,30,31,31,30,31,30,31] #no of days in gregorian calender months

#gets the current date from datetime module
today = date.today()
day = int(today.strftime("%d"))
month = int(today.strftime("%m"))
year = int(today.strftime("%y"))

#uncomment to enter the date manualy
##day = int(input("enter day"))
##month = int(input("enter month"))
##year = int(input("enter year"))

def leapyears(): 
    if (month>1):#add current year if february has passed
        leapyears=year//4
    else: #leave the current year if february hasnt passed
        leapyears=(year-1)//4
    return leapyears

        
def daysInLastYear():
    daysInLastYear=0
    for i in range(month-1):
        daysInLastYear+=MONTHS[i]
    return (daysInLastYear+day)


totalDays = ((year-1)*365)+leapyears()+daysInLastYear()
ethTotalDays = totalDays-DAYDIFFERENCE
ethLeapYears = ethTotalDays//(4*365)
ethTotalDays -= ethLeapYears
ethYear = (ethTotalDays//365)+1    
ethDaysOfYear = ethTotalDays%365
flag = True#to use for the leap year


if(ethYear%4==0):#in case of leap years
    if(ethDaysOfYear==0):
        ethYear-=1
        ethDay=6
        ethMonth=13
        flag=False
   ## else:
        ##ethDaysOfYear-=1
if(flag):
    if(ethDaysOfYear%30==0):
        if(ethDaysOfYear==0):
            ethDay=5
            ethMonth=13
            ethYear-=1
        else:
            ethMonth=(ethDaysOfYear//30)
            ethDay=30       
    else:
        ethMonth=(ethDaysOfYear//30)+1
        ethDay=ethDaysOfYear%30

currentYearDays = ((ethMonth-1)*30)+ethDay
yearProgress = int((currentYearDays*100)/365)


canvas = tk.Tk()
canvas.title("Ethiopian Year Progress")
canvas.geometry('400x200')
frame = tk.Frame(canvas, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='blue')
bar = Progressbar(frame, length=180, style='black.Horizontal.TProgressbar')
bar['value'] = yearProgress
bar.grid(column=0, row=0)
bar.pack(expand=1)
label = tk.Label(frame, text=str(bar['value'])+"%", fg="blue")
label.pack(fill=X, expand=1)
label2 = tk.Label(frame, text= (ethDay,"/",ethMonth,"/",ethYear,"EC"), fg="blue")
label2.pack(fill=X, expand=1)
canvas.mainloop()
