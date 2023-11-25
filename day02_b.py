
sit_dict = {
    "A":  {
        "X": 3, # Chooses rock, need to lose, choose scissors
        "Y": 4, # choose rock
        "Z": 8  # choose paper
    },
    "B": {
        "X": 1, # Chooses paper, need to lose, choose rock
        "Y": 5, # choose paper
        "Z": 9  # choose scissors
    },
    "C":{
        "X": 2, # Chooses scissors, need to lose, choose paper
        "Y": 6, # choose scissors
        "Z": 7  # choose rock
    }
}

first = ["A", "B", "C"]
second = ["X", "Y", "Z"]

my_sum = 0

with open("day2_input.txt", encoding="utf-8") as f:
    for i in range(2500):
        x = f.readline()
        a, b = x.split(' ')
        b = b[:-1]
        my_sum += sit_dict[a][b]
print(my_sum)