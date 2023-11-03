class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def add_child(self, child_node, is_left=True):
        if is_left:
            self.left = child_node
        else:
            self.right = child_node

def create_directory_tree():
    root = Node("Root")
    documents = Node("Documents")
    root.add_child(documents, is_left=True)

    music = Node("Music")
    pictures = Node("Pictures")
    documents.add_child(music, is_left=True)
    documents.add_child(pictures, is_left=False)

    # Adding subdirectories for 'Music'
    rock = Node("Rock")
    jazz = Node("Jazz")
    music.add_child(rock, is_left=True)
    music.add_child(jazz, is_left=False)

    # Adding subdirectories for 'Pictures'
    selfies = Node("Selfies")
    screenshots = Node("Screenshots")
    pictures.add_child(selfies, is_left=True)
    pictures.add_child(screenshots, is_left=False)

    return root

def traverse_directory_tree(node, depth=0):
    if node:
        print("  " * depth + node.name)
        traverse_directory_tree(node.left, depth + 1)
        traverse_directory_tree(node.right, depth + 1)

root_directory = create_directory_tree()
traverse_directory_tree(root_directory)

