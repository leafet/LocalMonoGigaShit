"""
Дан односвязный линейный список и указатель на голову списка P1. Необходимо
вывести указатель на пятый элемент этого списка P5. Известно, что в исходном списке не
менее 5 элементов.
"""

from GlobalTools.HandMadeList import HMList
import random as r

def main():
    new_list = HMList()

    for i in range(15):
        data = r.randint(0, 25)
        new_list.append(data)

    for item in new_list:
        print(item, end=" ")

    print()

    print(new_list[4])


if __name__ == "__main__":
    main()