"""
Даны ссылки A1, A2 и A3 на первый, последний и текущий элементы непустого
двусвязного списка. Также даны пять чисел. Включить в класс IntList (см. задание Dynamic59)
процедуру InsertAfter(D), которая вставляет новый элемент со значением D после текущего
элемента списка (D — входной параметр целого типа). Вставленный элемент становится
текущим. С помощью метода InsertAfter вставить пять данных чисел в исходный список и
вывести ссылки на первый, последний и текущий элементы полученного списка.
"""

from GlobalTools.HandMadeDLlist import HMDLList, Node
import random as r

class IntList(HMDLList):
    def insert_after(self, data):
        if self.current is None:
            self.append(data)
            return

        new_node = Node(data)

        new_node.prev = self.current
        new_node.next = self.current.next

        if self.current.next is not None:
            self.current.next.prev = new_node
        else:
            self.last = new_node

        self.current.next = new_node
        self.current = new_node
        self.len += 1


def main():
    dl_list = IntList()

    initial_values = [10, 20, 30, 40, 50]
    for value in initial_values:
        dl_list.append(value)

    print("Исходный список:")
    for item in dl_list:
        print(item.data, end=" ")
    print()

    print(f"A1 (first): {dl_list.first.data}")
    print(f"A2 (last): {dl_list.last.data}")
    print(f"A3 (current): {dl_list.current.data}")

    values_to_insert = [r.randint(1, 100) for _ in range(5)]
    print(f"\nЧисла для вставки: {values_to_insert}")

    for val in values_to_insert:
        dl_list.insert_after(val)

    print("\nСписок после вставки:")
    for item in dl_list:
        print(item.data, end=" ")
    print()

    print(f"\nA1 (first): {dl_list.first.data}")
    print(f"A2 (last): {dl_list.last.data}")
    print(f"A3 (current): {dl_list.current.data}")


if __name__ == "__main__":
    main()
