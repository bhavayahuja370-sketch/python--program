list_input = input("Enter list elements separated by spaces: ")
my_list = list_input.split()

search_element = input("Enter the element to search for: ")

if search_element in my_list:
    index = my_list.index(search_element)
    print(f"'{search_element}' found at index {index}.")
else:
    print(f"'{search_element}' not found in the list.")
