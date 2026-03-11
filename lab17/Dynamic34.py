"""
Дано число D и ссылка A0 на один из элементов непустого двусвязного списка.
Вставить после данного элемента списка новый элемент со значением D и вывести ссылку на
добавленный элемент списка.
"""

from GlobalTools.HandMadeDLlist import HMDLList, Node
import random as r

def insert_after_node(dl_list: HMDLList, node: Node, data):
    new_node = Node(data)

    new_node.prev = node
    new_node.next = node.next

    if node.next is not None:
        node.next.prev = new_node
    else:
        dl_list.last = new_node

    node.next = new_node
    dl_list.len += 1

    return new_node


def main():
    dl_list = HMDLList()

    values = [12, 45, 78, 23, 56, 89, 34]
    for value in values:
        dl_list.append(value)

    print("Исходный список:")
    for item in dl_list:
        print(item.data, end=" ")
    print()

    index = r.randint(0, dl_list.len - 1)
    a0 = dl_list.first
    for _ in range(index):
        a0 = a0.next

    print(f"Элемент A0 (индекс {index}): {a0.data}")

    d = r.randint(1, 100)
    print(f"Значение D: {d}")

    new_node = insert_after_node(dl_list, a0, d)

    print("Список после вставки:")
    for item in dl_list:
        print(item.data, end=" ")
    print()

    print(f"Ссылка на добавленный элемент: {new_node}")
    print(f"Значение добавленного элемента: {new_node.data}")


if __name__ == "__main__":
    main()
