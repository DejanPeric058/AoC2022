import numpy as np

with open("day08_input.txt") as f:
    input_data = f.read()

count_trees = 0
tree_columns = input_data.split('\n')
tree_map = np.array([[int(k) for k in row] for row in tree_columns])
size = len(tree_map) - 1

for i, row in enumerate(tree_map):
    for j, height in enumerate(row):
        if i == 0 or j == 0 or i == size or j == size:
            count_trees += 1
        else:
            max_up = max(tree_map[:, j][:i])
            max_down = max(tree_map[:, j][i+1:])
            max_left = max(tree_map[i, :][:j])
            max_right = max(tree_map[i, :][j+1:])
            if height > min(max_up, max_down, max_left, max_right):
                count_trees += 1

print(count_trees)