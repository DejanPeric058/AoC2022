
maximal_values = [0, 0, 0]
new_value = 0

with open("day1.txt", encoding="utf-8") as f:
    for i in range(2231):
        line = f.readline()
        if line == "\n":
            maximal_values.append(new_value)
            maximal_values.sort(reverse=True)
            maximal_values.pop()
            new_value = 0
        else:
            new_value += int(line)
print(sum(maximal_values))