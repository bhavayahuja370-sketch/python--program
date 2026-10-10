def check_number(lst, number):
    if number in lst:
        return True
    else:
        return False

a = [1, 3, 5, 7, 9, 11]

num = int(input("Enter a number: "))

print(check_number(a, num))
