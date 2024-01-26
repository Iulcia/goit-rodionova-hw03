import random

def get_numbers_ticket(min, max, quantity) -> list:
    # check if inputs are integers:
    if (isinstance(min, int)) and (isinstance(max, int)) and (isinstance(quantity, int)):
        if min <= 0 or max > 1000 or quantity > max:  # check requirements for min, max, qty values
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
        return [] # return empty list on not int params

#print(get_numbers_ticket(1, 560, 78))

