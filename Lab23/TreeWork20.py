"""Дано бинарное дерево и корень дерева P1. Необходимо определить, является ли
дерево АВЛ-сбалансированным. В качестве результата вывести логическое значение: True или
False. Дерево называется АВЛ-сбалансированным, если для каждой его вершины выполнено
условие: высота ее левого и правого поддерева отличается не больше, чем на 1."""

from GlobalTools.HandMadeBST import BinarySearchTree
from GlobalTools.SharedInput import GINPT

def main():
    tree = BinarySearchTree()
    values = GINPT.get_rand_int_list(15)

    print("Начальные значения случайные")
    print(*values)

    for v in values:
        tree.insert(v)

    print(tree.is_avl())

    tree2 = BinarySearchTree()
    values2 = GINPT.get_int_list_from_file("mockdata.txt")
    print("Начальные значения заготовленные")
    print(*values2)

    for v in values2:
        tree2.insert(v)

    print(tree2.is_avl())

if __name__ == "__main__":
    main()