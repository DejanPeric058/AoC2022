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



def get_sum(tree: Tree, min_value: int, sez):
    if not tree.children:
        return tree.files, sez
    else:
        vsota = tree.files
        for x in tree.children:
            ggg, sez = get_sum(x, min_value, sez)
            if ggg >= min_value:
                sez.append(ggg)
            vsota += ggg
        
        if vsota >= min_value:
            sez.append(vsota)
        return vsota, sez

_, sez = get_sum(glavni,6876531,[])
print(sorted(sez)[0])