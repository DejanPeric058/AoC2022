
sit_dict = {
    "A":  {
        "X":4,
        "Y": 8,
        "Z": 3
    },
    "B": {
        "X": 1,
        "Y":5,
        "Z": 9
    },
    "C":{
        "X": 7,
        "Y": 2,
        "Z": 6
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