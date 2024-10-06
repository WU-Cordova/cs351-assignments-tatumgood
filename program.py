
from datastructures.avltree import AVLTree
def main():
    # tree = AVLTree[int, int]()
    # for node in [8, 9, 10, 2]:
    #     tree.insert(node, node)
    
    # print(tree.bforder())

    # def print_node(value: int) -> None:
    #     print(value)

    # #using a built in higher order func
    # _ = tree.bforder(print)
    # _ = tree.bforder(print_node)

    # _ = tree.bforder(lambda value: print(value))

    avltree = AVLTree()
    avltree.insert(5)

    print(avltree)


if __name__ == '__main__':
    main()