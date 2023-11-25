with open("day07_input.txt", encoding='utf-8') as f:
    commands = f.readlines()


class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None, vsota=None, parent=None):
        self.name = name
        self.children = []
        self.parent = parent
        self.vsota = vsota
        self.files = 0
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def add_file(self, file):
        self.files += file

    def find_child(self, name_of_a_child):
        for child in self.children:
            assert isinstance(child, Tree)
            if child.name == name_of_a_child:
                return child
        return None
    def sum_vsota(self):
        vsota = 0
        for child in self.children:
            assert isinstance(child, Tree)
            if child.vsota is None:
                self.vsota = None
                return None
            else:
                vsota += child.vsota
        self.vsota = vsota


folder = Tree(name='/')
glavni = folder
for command in commands[1:]:
    command = command[:-1]
    parts = command.split(' ')
    if parts[0] == '$':
        if parts[1] == 'cd':
            if parts[2] == '..':
                folder = folder.parent
            else:
                folder = folder.find_child(name_of_a_child=parts[2])
        else:
            pass
    elif parts[0] == 'dir':
        subfolder = Tree(name=parts[1], parent=folder)
        folder.add_child(subfolder)
    else:
        folder.add_file(file=int(parts[0]))



def get_sum(tree: Tree, max_value: int, all_sum):
    if not tree.children:
        return tree.files, all_sum
    else:
        vsota = tree.files
        for x in tree.children:
            ggg, all_sum = get_sum(x, max_value, all_sum)
            if ggg <= max_value:
                all_sum += ggg
            vsota += ggg
        return vsota, all_sum




print(get_sum(glavni,100000,0))