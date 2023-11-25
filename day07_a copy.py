import re

with open("day07_input.txt", encoding='utf-8') as f:
    commands = f.readlines()

my_sizes = {}
max_size = 100000
reversed_commands = commands[::-1]
number_starts_pattern = re.compile(r'^\d')
dir_pattern = re.compile(r'^\$ cd [a-zA-Z]+')
past_dir = []
gggg = []
 
def sum_small_dir(sizes):
    sum_all = 0
    for size in sizes.values():
        if size <= max_size:
            sum_all += size
    return sum_all

part_sum = 0
for command in reversed_commands:
    command = command[:-1]
    part_of_command = command.split(" ")
    first_command = part_of_command[0]
    if first_command == "dir":
        part_sum += my_sizes[part_of_command[1]]
    elif bool(number_starts_pattern.match(first_command)):
        part_sum += int(first_command)
    elif bool(dir_pattern.match(command)) or command == '$ cd /':
        z = part_of_command[2]
        if z not in past_dir:
            my_sizes[z] = part_sum
            past_dir.append(z)
        else:
            gggg.append(z)
        part_sum = 0

my_sum = sum_small_dir(my_sizes)
print(my_sum)
print(set(gggg))