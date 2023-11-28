
with open("day10_input.txt") as f:
    text = f.read()

ukazi = text.splitlines()
novi_ukazi = []
signal_checkers = [20 + i*40 for i in range(6)]
my_sum = 1
my_signal = 0
for ukaz in ukazi:
    if ukaz[0] == 'a':
        _, add = ukaz.split(' ')
        novi_ukazi.append(0)
        novi_ukazi.append(int(add))
    else:
        novi_ukazi.append(0)

for i, ukaz in enumerate(novi_ukazi,start=1):
    if i in signal_checkers:
        my_signal += i*my_sum
    
    my_sum += ukaz

print(my_signal)