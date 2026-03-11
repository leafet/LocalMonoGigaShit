"""
Даны ссылки A1 и A2 на барьерные элементы двух двусвязных списков (о списке
с барьерным элементом см. задание Dynamic70). Объединить исходные списки, связав конец
первого и начало второго списка (барьерным элементом объединенного списка должен
остаться барьерный элемент второго списка). Вывести ссылки на первый и последний
элементы объединенного списка (если объединенный список является пустым, то дважды
вывести ссылку на его барьерный элемент). После удаления лишнего барьерного элемента
вызвать для него метод Dispose.
"""

from GlobalTools.HandMadeDLlist import Node

class BarrierNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.is_barrier = True

    def dispose(self):
        self.prev = None
        self.next = None
        self.data = None
        self.is_barrier = False


class BarrierList:
    def __init__(self, barrier_node: BarrierNode):
        self.barrier = barrier_node
        self.first = None
        self.last = None
        self.len = 0

    def append(self, data):
        new_node = Node(data)
        if self.first is None:
            self.barrier.next = new_node
            new_node.prev = self.barrier
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
        self.len += 1


def merge_barrier_lists(list1: BarrierList, list2: BarrierList, barrier1: BarrierNode):
    if list1.first is None:
        barrier1.dispose()
        return list2.barrier, list2.last

    if list2.first is None:
        return list2.barrier, list2.last

    list1.last.next = list2.first
    list2.first.prev = list1.last

    barrier2 = list2.barrier
    barrier2.prev = list1.last

    barrier1.dispose()

    return barrier2, list2.last


def main():
    barrier1 = BarrierNode("BARRIER1")
    barrier2 = BarrierNode("BARRIER2")

    list1 = BarrierList(barrier1)
    list2 = BarrierList(barrier2)

    values1 = [15, 25, 35, 45]
    values2 = [55, 65, 75]

    for val in values1:
        list1.append(val)

    for val in values2:
        list2.append(val)

    print("Список 1 (с барьером):")
    current = barrier1.next
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

    print("Список 2 (с барьером):")
    current = barrier2.next
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

    print(f"\nA1 (барьер 1): {barrier1}")
    print(f"A2 (барьер 2): {barrier2}")

    merged_barrier, merged_last = merge_barrier_lists(list1, list2, barrier1)

    print("\nОбъединенный список:")
    current = list1.first
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

    first_element = list1.first if list1.first else merged_barrier
    last_element = merged_last if merged_last else merged_barrier

    print(f"\nПервый элемент: {first_element}")
    if first_element != merged_barrier:
        print(f"Значение первого элемента: {first_element.data}")
    print(f"Последний элемент: {last_element}")
    if last_element != merged_barrier:
        print(f"Значение последнего элемента: {last_element.data}")


if __name__ == "__main__":
    main()
