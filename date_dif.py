from datetime import datetime, timedelta

"""
Fnc returns delta in days btw input date and today date. If error returns None
"""

def get_days_from_today(date):
    # for valid start date, transform str into date object
    try:
        start_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return None
    # get current date without time    
    current_date = datetime.today().date()
    # calculate difference (in days)
    diff = current_date.toordinal() - start_date.toordinal()
    return diff