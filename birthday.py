import datetime as dt
from datetime import datetime as dtdt, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.02.01"},
    {"name": "Jane Smith", "birthday": "1990.01.02"},
    {"name": "Yuliia Smith2", "birthday": "1990.01.07"}
]

def get_upcoming_birthdays(users):
    today_date = dtdt.today().date()
    birthdays = []
    diffs = []
    for user in users:
        bdate = user["birthday"]
        last_day_of_this_year = dtdt.strptime(str(today_date.year) + '.12.31', "%Y.%m.%d").date()
        if ((last_day_of_this_year - today_date).days < 7) and bdate[5:7] == '01':
            bdate = str((today_date + dt.timedelta(days = 365)).year) + bdate[4:]
        else:    
            bdate = str(today_date.year) + bdate[4:]
        bdate = dtdt.strptime(bdate, "%Y.%m.%d").date() # get date object for bday in curr year
        diff = (bdate - today_date).days
        if 0 <= diff < 7:
            day_of_week = bdate.isoweekday()
            if day_of_week < 6:
                birthdays.append({'name': user['name'], 'congratulation_date': bdate.strftime('%Y.%m.%d')})
            elif day_of_week == 6:
                delta = dt.timedelta(days = 2) # it's Saturday
                birthdays.append({'name': user['name'], 'congratulation_date': (bdate + delta).strftime('%Y.%m.%d')}) 
            else:
                delta = dt.timedelta(days = 1) # it's Sunday
                birthdays.append({'name': user['name'], 'congratulation_date': (bdate + delta).strftime('%Y.%m.%d')}) 
    
    return birthdays


print(get_upcoming_birthdays(users))