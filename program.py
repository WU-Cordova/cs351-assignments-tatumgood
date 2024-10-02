
from datastructures.avltree import AVLTree
def main():
    tree = AVLTree[int, int]()
    for node in [8, 9, 10, 2, 1, 5, 3, 6, 4, 7]:
        tree.insert(node, node)
    
    print(tree.inorder())

if __name__ == '__main__':
    main()