"""
Даны ссылки A1, A2 и A3 на первый, последний и текущий элементы непустого
двусвязного списка. Также даны пять чисел. Включить в класс IntList (см. задание Dynamic59)
процедуру InsertAfter(D), которая вставляет новый элемент со значением D после текущего
элемента списка (D — входной параметр целого типа). Вставленный элемент становится
текущим. С помощью метода InsertAfter вставить пять данных чисел в исходный список и
вывести ссылки на первый, последний и текущий элементы полученного списка.
"""

from GlobalTools.HandMadeDLlist import Node


class IntList:
    def __init__(self, aFirst: Node = None, aLast: Node = None, aCurrent: Node = None):
        self.__first = aFirst
        self.__last = aLast
        self.__current = aCurrent

    def insert_last(self, data: int):
        """Добавляет новый элемент со значением D в конец списка.
        Добавленный элемент становится текущим."""
        new_node = Node(data)
        
        if self.__first is None:
            # Пустой список
            self.__first = new_node
            self.__last = new_node
            self.__current = new_node
        else:
            # Добавляем в конец
            new_node.prev = self.__last
            self.__last.next = new_node
            self.__last = new_node
            self.__current = new_node

    def put(self):
        """Выводит ссылки на поля first, last и current."""
        print(f"first: {id(self.__first) if self.__first else 'null'}")
        print(f"last: {id(self.__last) if self.__last else 'null'}")
        print(f"current: {id(self.__current) if self.__current else 'null'}")

    def get_first(self) -> Node:
        return self.__first

    def get_last(self) -> Node:
        return self.__last

    def get_current(self) -> Node:
        return self.__current

    def to_list(self) -> list:
        """Возвращает список значений для отладки."""
        result = []
        current = self.__first
        while current is not None:
            result.append(current.data)
            current = current.next
        return result


def main():
    # Создаём пустой список (A1 = A2 = A3 = null)
    int_list = IntList()

    print("Исходный список (пустой):")
    int_list.put()
    print()

    # Число N и набор из N чисел
    N = 5
    values = [10, 25, 37, 42, 58]

    print(f"Добавляем {N} чисел: {values}")
    for val in values:
        int_list.insert_last(val)

    print("\nСписок после добавления:")
    print(f"Значения: {int_list.to_list()}")
    print()

    print("Ссылки на первый, последний и текущий элементы:")
    int_list.put()


if __name__ == "__main__":
    main()
