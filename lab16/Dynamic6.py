"""
Дана вершина A1 стека, содержащего не менее десяти элементов. Извлечь из стека
первые девять элементов и вывести их значения. Вывести также ссылку на новую вершину
стека. После извлечения элементов из стека освобождать ресурсы, которые они использовали,
вызывая для этих элементов метод Dispose.
"""

from GlobalTools.HandMadeStack import HMStack
from GlobalTools.SharedInput import GINPT

def main():
    a1 = GINPT.get_str_input("Введите вершину: ")

    stack = HMStack()

    values = [15, 14, 36, 94, 3, 8, 54, 26, 12, 32, 4, 0]

    print("Значения вносимые в стек:")

    for value in values:
        stack.push(value)

    stack.push(a1)

    print(*values)
    print(f"Вершина - {stack.peek()}")

    for i in range(9):
        print(f"Забираем {i + 1} = {stack.pop()}")

    print(f"Новая вершина {stack.top}")


if __name__ == "__main__":
    main()