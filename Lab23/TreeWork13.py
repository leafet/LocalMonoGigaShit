"""Дан корень P1 непустого дерева. Листом дерева называется его вершина, не
имеющая дочерних вершин. Вывести количество листьев для данного дерева."""

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

    print(f"В дереве {len(leaves)} листьев")


if __name__ == "__main__":
    main()