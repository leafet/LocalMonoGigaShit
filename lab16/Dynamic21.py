"""
Даны две очереди; начало и конец первой равны A1 и A2, а второй — A3 и A4
(если очередь является пустой, то соответствующие объекты равны null). Переместить все
элементы первой очереди (в порядке от начала к концу) в конец второй очереди и вывести
ссылки на начало и конец преобразованной второй очереди. Новые объекты типа Node не
создавать.
"""

from GlobalTools.HandMadeQueue import HMQueue
from GlobalTools.SharedInput import GTLS

def main():
    Q1 = HMQueue()
    Q2 = HMQueue()

    A1 = GTLS.get_str_input("Введите начало 1 очереди: ")
    A2 = GTLS.get_str_input("Введите конец 1 очереди: ")

    A3 = GTLS.get_str_input("Введите начало 2 очереди: ")
    A4 = GTLS.get_str_input("Введите конец 2 очереди: ")

    Q1.enqueue(A2)

    values1 = [5, 6, 7, 8]

    for value in values1:
        Q1.enqueue(value)

    Q1.enqueue(A1)

    Q2.enqueue(A3)

    values2 = [1, 2, 3, 4]

    for value in values2:
        Q2.enqueue(value)

    Q2.enqueue(A4)

    while Q2.Size != 0:
        Q1.enqueue_by_node(Q2.dequeue_by_node())

    while Q1.Size != 0:
        print(Q1.dequeue())

if __name__ == "__main__":
    main()