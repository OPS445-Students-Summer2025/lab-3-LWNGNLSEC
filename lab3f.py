#!/usr/bin/env python3

# Author ID: clee259

# Place my_list below this comment (before the function definitions)
my_list = [1, 2, 3, 4, 5 ]

def add_item_to_list(ordered_list):
        last_list = ordered_list[ -1]
        new_list = last_list + 1 #with the value (last item + 1)
        return ordered_list.append(new_list) #Appends new item to end of list
    

def remove_items_from_list(ordered_list, items_to_remove):
    for item in items_to_remove:
        ordered_list.remove(item) # Removes all values, found in items_to_remove list, from ordered_list

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)