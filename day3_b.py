import string

def return_ordering(letter):
    if letter.isupper():
        return string.ascii_uppercase.index(letter) + 27
    else:
        return string.ascii_lowercase.index(letter) + 1
    
def find_common_letter(x, y, z):
    
    first, second, third = set([*x]), set([*y]), set([*z])
    return first.intersection(second,third).pop()

my_sum = 0

with open("day3_input.txt", encoding="utf-8") as f:
    for i in range(100):
        x = f.readline()
        x = x[:-1]
        y = f.readline()
        y = y[:-1]
        z = f.readline()
        z = z[:-1]
        common_letter = find_common_letter(x,y,z)
        my_sum += return_ordering(common_letter)

print(my_sum)