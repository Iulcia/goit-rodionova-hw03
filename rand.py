import random

"""
Fnc returns  list with lenght of {quantity} of unique RANDOM integers from {min} to {max} values inclusively
"""

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
   
    if (isinstance(min, int)) and (isinstance(max, int)) and (isinstance(quantity, int)):  # check if inputs are integers
        if min <= 0 or max > 1000 or max < min or quantity <=0 or quantity > max:  # check requirements for min, max, qty values
            return [] # reqs not met for min, max or qty
        else:
            result = []
            while len(result) < quantity:
                item = random.randint(min, max)
                if item not in result: # add only unique values
                    result.append(item)
            result.sort()    
            return result
    else:
        return [] # return empty list for not int params 