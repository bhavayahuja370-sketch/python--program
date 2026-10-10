numbers = input("Enter numbers: ").split(",")

lst = [int(x) for x in numbers]
tup = tuple(lst)

print("List:", lst)
print("Tuple:", tup)
