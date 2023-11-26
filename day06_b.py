with open("day06_input.txt") as f:
    my_string = f.read()

n = 14
marker = [x for x in my_string[:n-1]]
for i, charachter in enumerate(my_string[n-1:]):
    marker.append(charachter)
    if len(set(marker)) == n:
        print(i+n)
        break
    marker.pop(0)