"""
Дан односвязный линейный список и указатель на голову списка P1. Необходимо
вставить значение M перед каждым вторым элементом списка, и вывести ссылку на последний
элемент полученного списка P2. При нечетном числе элементов исходного списка в конец
списка вставлять не надо.
"""

from GlobalTools.HandMadeList import HMList
from GlobalTools.SharedInput import GINPT
import random as r

def copy_with_insert_before_even(source: HMList, value):
    result = HMList()
    position = 1

    for node in source:
        if position % 2 == 0:
            result.append(value)

        result.append(node.data)
        position += 1

    return result

def main():
    source_list = HMList()

    for i in range(4):
        data = r.randint(0, 25)
        source_list.append(data)

    m = GINPT.get_int_input("Введите M: ")

    print("Исходный список:")
    for item in source_list:
        print(item.data, end=" ")

    result_list = copy_with_insert_before_even(source_list, m)

    print("\nНовый список после вставки:")
    for item in result_list:
        print(item.data, end=" ")

    print(f"\nПоследний элемент (P2): {result_list[result_list.len-1].data}")


if __name__ == "__main__":
    main()
