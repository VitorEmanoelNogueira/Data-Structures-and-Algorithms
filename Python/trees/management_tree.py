class ManagementTree:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent= None

    def get_level(self):
        level = 0
        p = self.parent
        while p: 
            level += 1
            p = p.parent

        return level
    
    def print_tree(self, option):
        if option == "both":
            value = f"{self.name} ({self.designation})"
        elif option == "name":
            value = self.name
        elif option == "designation":
            value = self.designation
        
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(option)
        

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    ceo = ManagementTree("Nilupul", "CEO")

    cto = ManagementTree("Chinmay", "CTO")
    infrastucture = ManagementTree("Vishwa", "Infrastructure Head")
    applicant = ManagementTree("Aamir", "Application Head")
    cto.add_child(infrastucture)
    cto.add_child(applicant)

    infrastucture.add_child(ManagementTree("Dhaval", "Cloud Manager"))
    infrastucture.add_child(ManagementTree("Abhijit", "App Manager"))
    
    hr = ManagementTree("Gels", "HR Head")
    hr.add_child(ManagementTree("Peter", "Recruitment Manager"))
    hr.add_child(ManagementTree("Waqas", "Policy Manager"))

    ceo.add_child(cto)
    ceo.add_child(hr)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")