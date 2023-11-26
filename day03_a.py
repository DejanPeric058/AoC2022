import string

def return_ordering(letter):
    if letter.isupper():
        return string.ascii_uppercase.index(letter) + 27
    else:
        return string.ascii_lowercase.index(letter) + 1
    
def find_common_letter(my_string):
    n = len(my_string)//2
    first, second = set([*my_string[:n]]), set([*my_string[n:]])
    return first.intersection(second).pop()

my_sum = 0

with open("day03_input.txt", encoding="utf-8") as f:
    for i in range(300):
        x = f.readline()
        x = x[:-1]
        common_letter = find_common_letter(x)
        my_sum += return_ordering(common_letter)

print(my_sum)