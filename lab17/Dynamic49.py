"""
Дан первый элемент A1 непустого двусвязного списка. Перегруппировать
элементы списка, переместив все элементы с нечетными номерами в конец списка (в том же
порядке) и вывести ссылку на первый элемент преобразованного списка. Новые объекты типа
Node не создавать, свойства Data не изменять.
"""

from GlobalTools.HandMadeDLlist import HMDLList, Node

def regroup_odd_to_end(dl_list: HMDLList):
    if dl_list.len <= 1:
        return dl_list.first

    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None

    current = dl_list.first
    position = 1

    while current is not None:
        next_node = current.next

        if position % 2 == 0:
            if even_head is None:
                even_head = current
                even_tail = current
                even_tail.prev = None
            else:
                even_tail.next = current
                current.prev = even_tail
                even_tail = current
        else:
            if odd_head is None:
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                current.prev = odd_tail
                odd_tail = current

        current = next_node
        position += 1

    if even_tail is not None:
        even_tail.next = odd_head
    if odd_head is not None:
        odd_head.prev = even_tail

    if odd_tail is not None:
        odd_tail.next = None

    dl_list.first = even_head if even_head else odd_head
    dl_list.last = odd_tail if odd_tail else even_tail

    return dl_list.first


def main():
    dl_list = HMDLList()

    values = [12, 45, 78, 23, 56, 89, 34, 67, 91, 15]
    for value in values:
        dl_list.append(value)

    print("Исходный список:")
    for i, item in enumerate(dl_list, 1):
        print(f"{i}: {item.data}", end="  ")
    print()

    a1 = dl_list.first
    print(f"Первый элемент A1: {a1.data}")

    new_first = regroup_odd_to_end(dl_list)

    print("\nСписок после перегруппировки:")
    for i, item in enumerate(dl_list, 1):
        print(f"{i}: {item.data}", end="  ")
    print()

    print(f"\nНовый первый элемент: {new_first.data}")


if __name__ == "__main__":
    main()
