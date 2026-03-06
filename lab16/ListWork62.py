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
        nums_line = f.readline().strip()

    sorted_list = HMList()

    num_start = 0
    for i in range(n):
        num_end = num_start
        while num_end < len(nums_line) and nums_line[num_end] != ' ':
            num_end += 1
        num = int(nums_line[num_start:num_end])
        insert_sorted_desc(sorted_list, num)
        num_start = num_end + 1

    for item in sorted_list:
        print(item.data, end=" ")

    print()


if __name__ == "__main__":
    main()
