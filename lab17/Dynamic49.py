"""
Дан первый элемент A1 непустого двусвязного списка. Перегруппировать
элементы списка, переместив все элементы с нечетными номерами в конец списка (в том же
порядке) и вывести ссылку на первый элемент преобразованного списка. Новые объекты типа
Node не создавать, свойства Data не изменять.
"""

from GlobalTools.HandMadeDLlist import HMDLList, Node

def regroup_list(dl_list: HMDLList) -> Node:
    if dl_list.first is None or dl_list.first.next is None:
        return dl_list.first

    even_first = None
    even_last = None
    odd_first = None
    odd_last = None
    
    current = dl_list.first
    index = 1
    
    while current is not None:
        next_node = current.next

        current.prev = None
        current.next = None
        
        if index % 2 == 1:
            if odd_first is None:
                odd_first = current
                odd_last = current
            else:
                odd_last.next = current
                current.prev = odd_last
                odd_last = current
        else:  # чётный номер
            if even_first is None:
                even_first = current
                even_last = current
            else:
                even_last.next = current
                current.prev = even_last
                even_last = current
        
        current = next_node
        index += 1

    if even_last and odd_first:
        even_last.next = odd_first
        odd_first.prev = even_last

    if even_first:
        dl_list.first = even_first
        dl_list.last = odd_last if odd_first else even_last
    elif odd_first:
        dl_list.first = odd_first
        dl_list.last = odd_last
    else:
        dl_list.first = None
        dl_list.last = None

    if dl_list.first:
        dl_list.first.prev = None
    if dl_list.last:
        dl_list.last.next = None

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

    new_first = regroup_list(dl_list)

    print("\nСписок после перегруппировки:")
    for i, item in enumerate(dl_list, 1):
        print(f"{i}: {item.data}", end="  ")
    print()

    print(f"\nНовый первый элемент: {new_first.data}")


if __name__ == "__main__":
    main()
