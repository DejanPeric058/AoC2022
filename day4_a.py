
my_sum = 0

with open("day4_input.txt", encoding='utf-8') as f:
    for i in range(1000):
        x = f.readline()
        x = x[:-1]
        sez1, sez2 = x.split(',')
        a, b = sez1.split('-') 
        c, d = sez2.split('-')
        a, b, c, d = int(a), int(b), int(c), int(d)
        if (a <= c and  b >= d) or (a >= c and  b <= d):
            my_sum += 1
print(my_sum)