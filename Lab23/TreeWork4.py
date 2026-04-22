"""Дано бинарное дерево и корень дерева P1. Необходимо вывести содержимое
листьев дерева, перечисляя их слева направо."""

from GlobalTools.HandMadeBT import BinaryTree
from GlobalTools.SharedInput import GINPT

def main():
    tree = BinaryTree()
    values = GINPT.get_rand_int_list(15)

    print("Начальные значения")
    print(*values)

    for v in values:
        tree.insert(v)

    leaves = tree.get_leaves()

    if leaves:
        print(' '.join(map(str, leaves)))
    else:
        print(-1)

if __name__ == "__main__":
    main()