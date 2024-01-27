from datetime import datetime, timedelta

def get_days_from_today(date):
    # for valid start date, transform str into date object
    try:
        start_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return  -1 #print("Please, use valid format '%Y-%m-%d'")
    # get current date without time    
    current_date = datetime.today().date()
    # calculate difference (in days)
    diff = current_date.toordinal() - start_date.toordinal()
    return diff

#print(get_days_from_today('190-02-20'))