class Node:
    def __init__(self, title, level, page_number):
        self.title = title
        self.level = level
        self.page_number = page_number
        self.children = []
        self.content = ""

    def add_child(self, node):
        self.children.append(node)