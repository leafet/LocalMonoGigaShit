"""Дано бинарное дерево и корень дерева P1. Необходимо определить, является ли
дерево АВЛ-сбалансированным. В качестве результата вывести логическое значение: True или
False. Дерево называется АВЛ-сбалансированным, если для каждой его вершины выполнено
условие: высота ее левого и правого поддерева отличается не больше, чем на 1."""

from GlobalTools.HandMadeBT import BinaryTree
from GlobalTools.SharedInput import GINPT

def main():
    tree = BinaryTree()
    values = GINPT.get_rand_int_list(15)

    print("Начальные значения")
    print(*values)

    for v in values:
        tree.insert(v)

    print(tree.is_avl())


if __name__ == "__main__":
    main()