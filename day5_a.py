
with open("day5_input.txt", encoding='utf-8') as f:
    sez = f.readlines()

my_dict = {}

for i in range(9):
    my_dict[i] = ''


for x in reversed(sez[:8]):
    for i in range(9):
        if x[1+ 4*i] != ' ':
            my_dict[i] += x[1+ 4*i]

def move_crates(n, a, b):
    my_dict[b] += my_dict[a][-n:][::-1]
    my_dict[a] = my_dict[a][:-n]


for x in sez[10:]:
    x[:-1]
    _, n, _, a, _, b = x.split(' ')
    move_crates(int(n), int(a)-1, int(b)-1)


solution = ''
for y in my_dict.values():
    solution += y[-1]

print(solution)