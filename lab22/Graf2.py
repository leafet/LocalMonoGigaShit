"""
Дано описание неориентированного графа в текстовом файле с именем FileName. в
виде матрицы смежности. Первая строка файла содержит количество вершин графа (n), а
следующие n строк содержат матрицу смежности (m), m[i][j]=0, если ребра между
вершинами i и j не существует. Определить степень для каждой вершины графа. Вывести
степени вершин, перечисляя их в порядке возрастания номеров вершин. Если в графе
имеются петли, то каждая петля в степени вершины учитывается дважды.
"""

from GlobalTools.SharedInput import GINPT
from GlobalTools.HandMadeGraph import Graph

def main():
    try:
        adj_matr, n = GINPT.get_matrix_from_file("FileName.txt")
    except (ValueError, IOError) as e:
        print(f"Ошибка чтения файла матрицы - {e}")
        return

    myGr = Graph(adj_matr)

    for vertex in myGr.vertices:
        print(f"Степень вершины {vertex.id} = {vertex.degree}")


if __name__ == "__main__":
    main()