import numpy as np

with open("day09_input.txt") as f:
    ukazi = f.read()

h = np.array([0, 0])
t = np.array([0, 0])
visited = {tuple(t)}
ukazi = ukazi.splitlines()

smeri = {
    'U': np.array([0, 1]),
    'D': np.array([0, -1]),
    'L': np.array([-1, 0]),
    'R': np.array([1, 0])
}

def sledi(head, tail, direction):
    head += smeri[direction]
    razdalja = np.linalg.norm(head-tail)
    if razdalja >= 1.9:
        tail += np.sign(head-tail)
    return head, tail

for ukaz in ukazi:
    smer, steps = ukaz.split(' ')
    for k in range(int(steps)):
        h, t = sledi(h, t, smer)
        visited.add(tuple(t))

print(len(set(visited)))