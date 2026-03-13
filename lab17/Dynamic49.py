"""
Дан первый элемент A1 непустого двусвязного списка. Перегруппировать
элементы списка, переместив все элементы с нечетными номерами в конец списка (в том же
порядке) и вывести ссылку на первый элемент преобразованного списка. Новые объекты типа
Node не создавать, свойства Data не изменять.
"""
from unittest import skip

from GlobalTools.HandMadeDLlist import HMDLList


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

    for i in range(len(dl_list)):
        if i % 2 == 0:
            dl_list.move_to_end(dl_list[i])

    for i, item in enumerate(dl_list, 1):
        print(f"{i}: {item.data}", end="  ")
    print()

    # print("\nСписок после перегруппировки:")
    # for i, item in enumerate(dl_list, 1):
    #     print(f"{i}: {item.data}", end="  ")
    # print()
    #
    # print(f"\nНовый первый элемент: {new_first.data}")


if __name__ == "__main__":
    main()
