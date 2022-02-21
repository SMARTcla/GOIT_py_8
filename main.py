import time
import datetime
from datetime import datetime, timedelta
from datetime import date
import calendar

users = {"25.02.2003": "Mikhailo", "1.03.2013": "Mary", "22.02.2002": "Nick", "18.02.2000": "Krish", "24.02.2000": "Nansy", "08.11.2000": "Key","27.02.1976": "Down","28.02.1976": "Elena","1.02.1982": "Mick","21.02.1976": "Polina"}


def date_formed(i):
    p_day = 1
    p_month = 1
    p_year = 1971
    count_dot = 0
    tmp = ''
    for p, k in enumerate(i):
        if k != '.':
            l = tmp + k
            tmp = l
        elif k == ".":
            if count_dot == 0:
                p_day = int(tmp)
            else:
                p_month = int(tmp)
            tmp = ''
            count_dot = 1
        if p == len(i) - 1:
            p_year = int(tmp)
    return p_day,p_month,p_year


def add_in_list(happy_people):
    for i,j in users.items():
        p_day = 1
        p_month = 1
        p_year = 1971
        count_dot = 0
        p_day,p_month,p_year = date_formed(i)
        current_date = datetime.now()
        custom_date = datetime(year=current_date.year, month=p_month, day=p_day)
        tp = timedelta(days=1)
        custom_date += tp
        res = custom_date - current_date
        if res.days < 8 and res.days > -1:
            temp_date = datetime.now()
            delta = timedelta(res.days)
            temp_date += delta
            temp = calendar.day_name[temp_date.weekday()]
            if temp == "Sunday" or temp == "Saturday":
                temp = "Monday"
            current_date += tp
            if custom_date.day == current_date.day:
                temp = "Today"
            if temp in happy_people:
                happy_people[temp] = happy_people[temp] + "," + j
            else:
                happy_people[temp] = j


def printd(happy_people):
    print("This is the list of people to congratulate ")
    for i,j in happy_people.items():
        print(i + ": " + j)

def get_birthdays_per_week(users):
    happy_people = {}
    add_in_list(happy_people)
    printd(happy_people)


get_birthdays_per_week(users)
