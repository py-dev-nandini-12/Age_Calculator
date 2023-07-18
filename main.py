from tkinter import *

window = Tk()
window.title("Age Calculator")
window.minsize(width=600, height=300)
# window.config(padx=20,pady=10)
window.config(background="grey")

date_of_birth_label = Label(text= "Date Of Birth", font=("Ariel", 15, "normal"))
date_of_birth_label.grid(column= 3, row= 0)
date_of_birth_label.config(pady=10,padx=20)
#
Given_date_label = Label(text= "Given Date", font=("Ariel", 15, "normal"))
Given_date_label.grid(column= 6, row=0 )
Given_date_label.config(pady=10,padx=0)

day_label = Label(text="Day" ,font=("Ariel", 15, "normal"))
day_label.grid(column=0 ,row=1 )
# # day_label.config(padx=-5,pady=0)
month_label = Label(text="Month" ,font=("Ariel", 15, "normal"))
month_label.grid(column=0 ,row= 2)
year_label = Label(text="Year" ,font=("Ariel", 15, "normal"))
year_label.grid(column= 0 ,row=  3)

given_day_label = Label(text= "Given Day" , font=("Ariel", 15, "normal"))
given_day_label.grid(column= 5 ,row=1 )
# given_day_label.config(padx= 50 ,pady=10)
given_month_label = Label(text= "Given Month" ,font=("Ariel", 15, "normal"))
given_month_label.grid(column=5, row =2)
given_year_label = Label(text= " Given Year" ,font=("Ariel", 15, "normal"))
given_year_label.grid(column=5, row =3)


day_entry = Entry(width=10)
day_entry.grid(column=1 ,row=1)
day_entry.get()

month_entry = Entry(width=10)
month_entry.grid(column=1 ,row=2)
month_entry.get()

year_entry = Entry(width=10)
year_entry.grid(column=1 ,row=3)
year_entry.get()

given_day_entry = Entry(width=10)
given_day_entry.grid(column=6 ,row=1)
given_day_entry.get()

given_month_entry = Entry(width=10)
given_month_entry.grid(column=6 ,row=2)
given_month_entry.get()

given_year_entry = Entry(width=10)
given_year_entry.grid(column=6 ,row=3)
given_year_entry.get()


def age_calculator():
    gy = int(given_year_entry.get())
    yb = int(year_entry.get())
    gm =int(given_month_entry.get())
    mb = int(month_entry.get())
    gd = int(given_day_entry.get())
    bd = int(day_entry.get())

    # if birth month exceeds given month, then
    # donot count this year and add 12 to the
    # month so that we can subtract and find out
    # the difference
    if mb > gm:
        gy -= 1
        gm += 12

    # if birth date is greater then given birth_month
    # then donot count this month and add 30 to the date so
    # as to subtract the date and get the remaining days
    if bd > mb:
        gm -=1
        gd += 30

    Years = gy - yb
    Months = gm - mb
    Days = gd - bd
    Years_entry.insert(0,f"{Years}")
    Months_entry.insert(0,f"{Months}")
    Days_entry.insert(0,f"{Days}")


def clear():
    year_entry.delete(0, END)
    month_entry.delete(0,END)
    day_entry.delete(0,END)
    given_year_entry.delete(0,END)
    given_month_entry.delete(0,END)
    given_day_entry.delete(0,END)
    Years_entry.delete(0,END)
    Months_entry.delete(0, END)
    Days_entry.delete(0, END)



resultant_age_button = Button(text= "Resultant Age" ,command=age_calculator)
resultant_age_button.grid(column=3 ,row= 3)

clear_button = Button(text="clear" ,command=clear)
clear_button.grid(column=3 ,row=9)

Years_label = Label(text = "Years")
Years_label.grid(column=4 ,row= 5)

Years_entry = Entry(width =10)
Years_entry.grid(column=3 ,row= 5)

Months_label = Label(text ="Months")
Months_label.grid(column=4 ,row= 7)

Months_entry = Entry(width = 10)
Months_entry.grid(column=3 ,row= 7)

Days_label = Label(text = "Days")
Days_label.grid(column=4 ,row= 8)

Days_entry = Entry(width =10)
Days_entry.grid(column=3 ,row= 8)


window.mainloop()

# : resolve bug ,when the given day < birth day same for month
#: include entries in Y,M D when age calculator is clicked
#: also include entries for the YEARS,MONTHS DAYS ,inorder to delete them once done
#with calculation