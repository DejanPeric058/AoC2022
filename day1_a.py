
maximal_value = 0
new_value = 0

with open("day1.txt", encoding="utf-8") as f:
    for i in range(2233):
        line = f.readline()
        print(line)
        if line == "\n":
            maximal_value = max(maximal_value, new_value)
            new_value = 0
        else:
            new_value += int(line)
print(maximal_value)