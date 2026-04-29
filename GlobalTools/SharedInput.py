import random

class GINPT:
    def __init__(self):
        pass

    @staticmethod
    def get_int_input(prompt: str, min_value: int = None, max_value: int = None):
        while True:
            try:
                value = int(input(prompt))
                if min_value is not None and value < min_value:
                    print(f"Значение должно быть не меньше {min_value}!")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Значение должно быть не больше {max_value}!")
                    continue
                return value
            except ValueError:
                print("Значение должно быть целым числом!")

    @staticmethod
    def get_float_input(prompt: str, min_value: float = None, max_value: float = None):
        while True:
            try:
                value = float(input(prompt))
                if min_value is not None and value < min_value:
                    print(f"Значение должно быть не меньше {min_value}!")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Значение должно быть не больше {max_value}!")
                    continue
                return value
            except ValueError:
                print("Значение должно быть числом!")

    @staticmethod
    def get_str_input(prompt: str):
        while True:
            try:
                value = str(input(prompt))
                return value
            except ValueError:
                print("Значение должно быть строкой")

    @staticmethod
    def get_rand_int_list(size: int):
        return [random.randint(1, 100) for _ in range(size)]

    @staticmethod
    def get_int_list_from_file(file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            line = f.readline()

        return list(map(int, line.split()))

    @staticmethod
    def get_matrix_from_file(file_path: str):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл '{file_path}' не найден.")
        except Exception as e:
            raise IOError(f"Ошибка при чтении файла: {e}")

        if not lines:
            raise ValueError("Файл пуст.")

        try:
            n = int(lines[0].strip())
        except ValueError:
            raise ValueError("Первая строка файла должна содержать целое число — размер матрицы.")

        if n <= 0:
            raise ValueError("Размер матрицы должен быть положительным целым числом.")

        matrix = []
        for i in range(1, n + 1):
            if i >= len(lines):
                raise ValueError(f"Недостаточно строк в файле: ожидается {n} строк матрицы, найдено {len(lines) - 1}.")
            line = lines[i].strip()
            if not line:
                raise ValueError(f"Строка {i} матрицы пуста.")
            try:
                row = list(map(int, line.split()))
            except ValueError:
                raise ValueError(f"Строка {i} содержит нечисловые значения. Используйте целые числа.")
            if len(row) != n:
                raise ValueError(f"В строке {i} ожидается {n} чисел, получено {len(row)}.")
            matrix.append(row)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] not in (0, 1):
                    raise ValueError(f"Элемент матрицы [{i + 1},{j + 1}] = {matrix[i][j]} не является 0 или 1.")

        for i in range(n):
            for j in range(i + 1, n):
                if matrix[i][j] != matrix[j][i]:
                    raise ValueError(
                        f"Матрица не симметрична: элемент [{i + 1},{j + 1}] = {matrix[i][j]} "
                        f"не равен [{j + 1},{i + 1}] = {matrix[j][i]}."
                    )


        return matrix, n


