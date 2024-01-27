import datetime as dt
from datetime import datetime as dtdt, timedelta

"""
This function returns upcoming in 7 days birthdays for set of users (returns list of dicts)
"""

def get_upcoming_birthdays(users) -> list:

    today_date = dtdt.today().date()
    birthdays = []
    diffs = []
    for user in users:
        bdate = user["birthday"]

        #check if it's not end of the year to include early January bdays for upcoming year:
        last_day_of_this_year = dtdt.strptime(str(today_date.year) + '.12.31', "%Y.%m.%d").date()
        if ((last_day_of_this_year - today_date).days < 7) and bdate[5:7] == '01': 
            bdate = str((today_date + dt.timedelta(days = 365)).year) + bdate[4:] # check for January birthdays next year, not current
        else:    
            bdate = str(today_date.year) + bdate[4:] # check bday for current year

        bdate = dtdt.strptime(bdate, "%Y.%m.%d").date()
        diff = (bdate - today_date).days # delta in days btw bday date and today

        if 0 <= diff < 7: # add to the list only upcoming in 7 days bdays
            day_of_week = bdate.isoweekday() 
            if day_of_week < 6:
                birthdays.append({'name': user['name'], 'congratulation_date': bdate.strftime('%Y.%m.%d')})
            elif day_of_week == 6: # if it's Saturday, congratulate in 2 days, on Monday
                delta = dt.timedelta(days = 2) 
                birthdays.append({'name': user['name'], 'congratulation_date': (bdate + delta).strftime('%Y.%m.%d')}) 
            else:
                delta = dt.timedelta(days = 1) # if it's Sunday, congratulate in 1 day, on Monday
                birthdays.append({'name': user['name'], 'congratulation_date': (bdate + delta).strftime('%Y.%m.%d')}) 
    
    return birthdays