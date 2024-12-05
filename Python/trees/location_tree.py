class LocationTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent= None

    def get_level(self):
        level = 0
        p = self.parent
        while p: 
            level += 1
            p = p.parent

        return level
    
    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children: 
                child.print_tree(level)
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_location_tree():
    root = LocationTree("Global")

    india = LocationTree("India")
    gujarat = LocationTree("Gujarat")
    karnataka = LocationTree("Karnataka")
    india.add_child(gujarat)
    india.add_child(karnataka)

    gujarat.add_child(LocationTree("Ahmad"))
    gujarat.add_child(LocationTree("Baroda"))

    karnataka.add_child(LocationTree("Bangluru"))
    karnataka.add_child(LocationTree("Mysore"))

    usa = LocationTree("USA")
    new_jersey = LocationTree("New Jersey")
    california = LocationTree("California")
    usa.add_child(new_jersey)
    usa.add_child(california)

    new_jersey.add_child(LocationTree("Princeton"))
    new_jersey.add_child(LocationTree("Ireton"))

    california.add_child(LocationTree("San Francisco"))
    california.add_child(LocationTree("Mountain View"))
    california.add_child(LocationTree("Palo Alto"))

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree()