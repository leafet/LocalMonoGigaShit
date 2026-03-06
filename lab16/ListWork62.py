"""
Дан текстовый файл в первой строке которого хранится число N, а во второй
строке N целых чисел. Необходимо создать упорядоченный по убыванию список, в который
поместить все эти элементы, при этом очередной элемент вставлять в список так, чтобы не
нарушалась его упорядоченность.
"""

from GlobalTools.HandMadeList import HMList


def insert_sorted_desc(lst: HMList, value):
    if lst.len == 0:
        lst.append(value)
        return

    for i, node in enumerate(lst):
        if value > node.data:
            lst.insert(i, value)
            return

    lst.append(value)


def main():
    with open("./ListWork62.txt", "r") as f:
        n = int(f.readline().strip())
        numbers = list(map(int, f.readline().strip().split()))

    sorted_list = HMList()

    for num in numbers:
        insert_sorted_desc(sorted_list, num)

    for item in sorted_list:
        print(item.data, end=" ")

    print()


if __name__ == "__main__":
    main()
