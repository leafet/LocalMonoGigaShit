"""
Юный путешественник решил изучить схему авиационного сообщения Схема
авиационного сообщения задана в текстовом файле с именем FileName. в виде матрицы
смежности. Первая строка файла содержит количество городов (n) n<=15, связанных
авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить номера
городов, в которые из города K можно долететь не менее чем с L пересадками и более
коротких путей к таким городам не существует. Перечислите номера таких городов в
порядке возрастания. Нумерация городов начинается с 1. Если таких городов нет,
выведите число (-1).
"""

from GlobalTools.SharedInput import GINPT
from GlobalTools.HandMadeGraph import Graph

def main():
    try:
        matrix, n = GINPT.get_matrix_from_file("FileName3.txt")
    except ValueError as e:
        print(f"Ошибка чтения файла матрицы - {e}")
        return

    if n > 15:
        print("Не может быть больше 15 городов")
        return

    g = Graph(matrix)
    K = GINPT.get_int_input("Введите номер города K: ", 1, g.size)
    L = GINPT.get_int_input("Введите минимальное число пересадок L: ", 0)

    start = K - 1
    reachable_L = set(g.reachable_within(start, L))
    reachable_L1 = set(g.reachable_within(start, L + 1))
    result = sorted(v + 1 for v in (reachable_L1 - reachable_L))

    if result:
        print(' '.join(map(str, result)))
    else:
        print(-1)

if __name__ == "__main__":
    main()