#!/usr/bin/python3

oceans = ["indian", "atlantic", "arctic", "southern", "pacific"]
elements = ["air", "earth", "air", "fire", "water", "air", "earth"]
air_list = ["air", "air", "air", "air", "air"]
num_list = [1, 1, 1, 5, 1]

def contains_item(items, target):
    if target not in items:
        return False
    else:
        return True
    
def count_occurrences(items, target):
    counter = 0
    
    for current_item in items:
        if current_item != target:
            pass
        else:
            counter += 1

    return counter

def find_index(items, target):
    for i in range(0, len(items)):
        if items[i] != target:
            pass
        else:
            return i

def is_empty(items):
    if not items:
        return True
    else:
        return False

def all_same(items):
    first_item = items[0]

    for current_item in items:
        if current_item != first_item:
            return False
        else:
            pass

    return True



## contains_item TEST    
# test1 = contains_item(oceans, "arctic")
# test2 = contains_item(oceans, "pacific")
# test3 = contains_item(oceans, "the red ocean")
    
## count_occurrences TEST    
# test1 = count_occurrences(elements, "air")
# test2 = count_occurrences(elements, "fire")
# test3 = count_occurrences(elements, "earth")

## find_index TEST    
# test1 = find_index(elements, "water")
# test2 = find_index(elements, "fire")
# test3 = find_index(elements, "earth")

## is_empty TEST    
# test1 = is_empty(elements)
# test2 = is_empty([])
# test3 = is_empty(oceans)
    
## all_same TEST    
# test1 = all_same(elements)
# test2 = all_same(air_list)
# test3 = all_same(num_list)
    

    
# print(test1)
# print(test2)
# print(test3)