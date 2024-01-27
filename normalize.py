import re

"""
This function is formatting entered phone numbers to common Ukrainian standart '+38**********'
"""

def normalize_phone(num: str) -> str:

    num_digits_plus = re.sub("[^0123456789+]","", num) # get only digits and + sign
    if len(num_digits_plus) < 10 or len(num_digits_plus) > 13: # check if number is 2 short or 2 long       
        return ""
    result = '+38' + num_digits_plus[-10:]
    return result