def remove_duplicates(my_list):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

numbers = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(numbers))
