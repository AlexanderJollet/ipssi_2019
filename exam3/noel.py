#!/usr/bin/python3

import sys
import calendar
from datetime import datetime, date, timedelta
from tree import show_tree


def show_noel(arg):
    d1 = arg[1]
    d1 = datetime.strptime(d1, "%Y-%m-%d")

    c1 = calendar.TextCalendar(calendar.MONDAY)
    c1 = c1.formatmonth(d1.year, d1.month, 3, 1)
    c1 = c1.replace(str(d1.day), "("+str(d1.day)+")", 1)
    
    c2 = calendar.TextCalendar(calendar.MONDAY)
    c2 = c2.formatmonth(d1.year, 12, 3, 1)
    c2 = c2.replace(" 25 ", "[25]", 1)
    d2 = datetime(d1.year,12,25)
    diff = datetime.date(d2) - datetime.date(d1)

    if (d1.strftime('%Y-%m-%d') == str(d1.year)+"-12-25") :
            return(show_tree(10))
    else :
        print(diff.days, "days before christmas\n")
        return c1 + c2


if __name__ == "__main__":
    print(show_noel(sys.argv))

    