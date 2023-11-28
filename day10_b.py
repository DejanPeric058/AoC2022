
with open("day10_input.txt") as f:
    text = f.read()

ukazi = text.splitlines()
novi_ukazi = []
signal_checkers = [i*40 for i in range(1,7)]
position = 1
my_signal = ''
for ukaz in ukazi:
    if ukaz[0] == 'a':
        _, add = ukaz.split(' ')
        novi_ukazi.append(0)
        novi_ukazi.append(int(add))
    else:
        novi_ukazi.append(0)

for i, ukaz in enumerate(novi_ukazi,start=0):
    if i in signal_checkers:
        my_signal += '\n'
    if i%40 in [position + j for j in [-1,0,1]]:
        my_signal += '#'
    else:
        my_signal += '.' 
    position += ukaz

print(my_signal)