import numpy as np

with open("day08_input.txt") as f:
    input_data = f.read()

max_scenic_score = 0
tree_columns = input_data.split('\n')
tree_map = np.array([[int(k) for k in row] for row in tree_columns])
size = len(tree_map) - 1

def number_of_trees(trees, height):
    for i, h in enumerate(trees):
        if h >= height:
            return i + 1
    return i + 1

for i, row in enumerate(tree_map):
    for j, height in enumerate(row):
        if i == 0 or j == 0 or i == size or j == size:
            pass
        else:
            trees_up = number_of_trees(tree_map[:, j][:i][::-1], height)
            trees_down = number_of_trees(tree_map[:, j][i+1:], height)
            trees_left = number_of_trees(tree_map[i, :][:j][::-1], height)
            trees_right = number_of_trees(tree_map[i, :][j+1:], height)
            scenic_score = trees_up * trees_down * trees_left * trees_right
            max_scenic_score = max(max_scenic_score, scenic_score)

print(max_scenic_score)