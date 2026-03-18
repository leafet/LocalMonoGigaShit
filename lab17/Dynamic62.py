"""
Даны ссылки A1, A2 и A3 на первый, последний и текущий элементы непустого
двусвязного списка. Также даны пять чисел. Включить в класс IntList (см. задание Dynamic59)
процедуру InsertAfter(D), которая вставляет новый элемент со значением D после текущего
элемента списка (D — входной параметр целого типа). Вставленный элемент становится
текущим. С помощью метода InsertAfter вставить пять данных чисел в исходный список и
вывести ссылки на первый, последний и текущий элементы полученного списка.
"""

from GlobalTools.HandMadeDLlist import HMDLList

class IntList(HMDLList):

    # метод из Dynamic59
    def InsertLast(self, D: int):
        return self.append(D)

    # метод из нового задания
    def InsertAfter(self, D: int):
        return self.insert_after_current(D)

    def Put(self):
        if self.first:
            print(f"first: id {self.first} with value {self.first.data}")
        else:
            print("first: null")

        if self.last:
            print(f"last: id {self.last} with value {self.last.data}")
        else:
            print("last: null")

        if self.current:
            print(f"current: id {self.current} with value {self.current.data}")
        else:
            print("current: null")

def main():
    initial_values = [12, 54, 34, 765, 12, 45, 878]

    int_list = IntList()

    for value in initial_values:
        int_list.InsertLast(value)

    print("Исходный список:")
    print([node.data for node in int_list])

    values = [10, 25, 37, 42, 58]

    print("\nВставляем через InsertAfter:")
    for val in values:
        int_list.InsertAfter(val)

    print("\nСписок:")
    print([node.data for node in int_list])

    print("\nСсылки:")
    int_list.Put()



if __name__ == "__main__":
    main()
