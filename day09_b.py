import numpy as np

with open("day09_input.txt") as f:
    ukazi = f.read()

knots = [np.array([0, 0]) for _ in range(10)]
visited = {tuple(knots[0])}
ukazi = ukazi.splitlines()

smeri = {
    'U': np.array([0, 1]),
    'D': np.array([0, -1]),
    'L': np.array([-1, 0]),
    'R': np.array([1, 0])
}

def sledi(tail, direction):
    tail[0] += smeri[direction]
    for i in range(len(tail) - 1):
        razdalja = np.linalg.norm(tail[i]-tail[i+1])
        if razdalja >= 1.9:
            tail[i+1] += np.sign(tail[i]-tail[i+1])
    return tail

for ukaz in ukazi:
    smer, steps = ukaz.split(' ')
    for k in range(int(steps)):
        knots = sledi(knots, smer)
        visited.add(tuple(knots[-1]))

print(len(set(visited)))