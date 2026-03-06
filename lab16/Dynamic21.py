"""
Даны две очереди; начало и конец первой равны A1 и A2, а второй — A3 и A4
(если очередь является пустой, то соответствующие объекты равны null).
Переместить все элементы первой очереди (в порядке от начала к концу) в конец
второй очереди и вывести ссылки на начало и конец преобразованной второй очереди.
Новые объекты типа Node не создавать.
"""

from GlobalTools.HandMadeQueue import HMQueue
from GlobalTools.SharedInput import GINPT

def main():
    q1 = HMQueue()
    q2 = HMQueue()

    a1 = GINPT.get_str_input("Введите начало 1 очереди: ")
    a2 = GINPT.get_str_input("Введите конец 1 очереди: ")

    a3 = GINPT.get_str_input("Введите начало 2 очереди: ")
    a4 = GINPT.get_str_input("Введите конец 2 очереди: ")

    q1.enqueue(a2)

    values1 = [5, 6, 7, 8]

    for value in values1:
        q1.enqueue(value)

    q1.enqueue(a1)

    q2.enqueue(a3)

    values2 = [1, 2, 3, 4]

    for value in values2:
        q2.enqueue(value)

    q2.enqueue(a4)

    while q2.size != 0:
        q1.enqueue_by_node(q2.dequeue_by_node())

    print("Итоговая очередь")

    while q1.size != 0:
        print(q1.dequeue())


if __name__ == "__main__":
    main()