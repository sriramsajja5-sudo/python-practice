#add_numbers:
def add_numbers(a, b):
    result = a + b
    return result
print(add_numbers(3, 5))
print(add_numbers(10, 20))

#is_even:
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(8))
print(is_even(7))

#get_grade:
def get_grade(marks):
    if marks>=90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        return 'F'
print(get_grade(95))
print(get_grade(80))
print(get_grade(65))
print(get_grade(40))
    