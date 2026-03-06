"""
Имеется информация об учениках младшей школы. Для всех учеников известны:
фамилия, имя и класс. Для учеников 1-х классов дополнительно известна их скорость чтения
(слов в минуту, тип int). Для учеников 4-х классов известны баллы итоговой аттестации
(единый муниципальный тест от 1 до 100 баллов, тип float). Для учеников 2-х и 3-х классов
известны данные итоговой школьной контрольной по математике (оценки от 1 до 10 баллов,
тип float). Написать функцию, позволяющую ввести с клавиатуры данные для одного ученика.
Используя эту функцию, ввести сведения об N учениках и сохранить их в бинарном файле.
Распечатать на экране содержимое данного файла в виде таблицы.
"""

import pickle


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


class JuniorSchoolStudent:
    def __init__(self, first_name: str, second_name: str, grade: int):
        self.first_name = first_name
        self.second_name = second_name
        self.grade = grade

    def __str__(self):
        return f"{self.first_name:<15} {self.second_name:<15} {self.grade:<6} -"


class JSSFirstGrade(JuniorSchoolStudent):
    def __init__(self, first_name: str, second_name: str, wpm: int):
        super().__init__(first_name, second_name, 1)
        self.wpm = wpm

    def __str__(self):
        return f"{self.first_name:<15} {self.second_name:<15} {self.grade:<6} Скорость чтения: {self.wpm} слов/мин"


class JSSFourthGrade(JuniorSchoolStudent):
    def __init__(self, first_name: str, second_name: str, final_certification_score: float):
        super().__init__(first_name, second_name, 4)
        self.final_certification_score = final_certification_score

    def __str__(self):
        return f"{self.first_name:<15} {self.second_name:<15} {self.grade:<6} Аттестация: {self.final_certification_score} баллов"


class JSSSecondAndThirdGrade(JuniorSchoolStudent):
    def __init__(self, first_name: str, second_name: str, grade: int, math_score: float):
        super().__init__(first_name, second_name, grade)
        self.math_score = math_score

    def __str__(self):
        return f"{self.first_name:<15} {self.second_name:<15} {self.grade:<6} Математика: {self.math_score} баллов"


class SchoolInformationSystem:
    def __init__(self):
        self.students: list[JuniorSchoolStudent] = []
        self.database_file_location: str = "./data_task2.bin"

    @staticmethod
    def input_student():
        print("\nВведите данные ученика:")
        first_name = input("Фамилия: ")
        second_name = input("Имя: ")
        
        grade = get_int_input("Класс (1-4): ", min_value=1, max_value=4)

        if grade == 1:
            wpm = get_int_input("Скорость чтения (слов в минуту): ", min_value=1)
            return JSSFirstGrade(first_name, second_name, wpm)
        elif grade == 4:
            score = get_float_input("Баллы итоговой аттестации (1-100): ", min_value=1, max_value=100)
            return JSSFourthGrade(first_name, second_name, score)
        else:
            math_score = get_float_input("Оценка за контрольную по математике (1-10): ", min_value=1, max_value=10)
            return JSSSecondAndThirdGrade(first_name, second_name, grade, math_score)

    def populate_database_file(self, students_data: list[JuniorSchoolStudent]):
        with open(self.database_file_location, "wb") as f:
            pickle.dump(students_data, f)

    def populate_students_from_database_file(self):
        with open(self.database_file_location, "rb") as f:
            try:
                self.students = pickle.load(f)
            except ValueError as e:
                raise e

    def print_students(self):
        print("\n" + "=" * 90)
        print(f"{'Фамилия':<15} {'Имя':<15} {'Класс':<6} {'Доп. информация':<50}")
        print("=" * 90)

        for student in self.students:
            print(student)

        print("=" * 90)


def main():
    school_system = SchoolInformationSystem()

    n = get_int_input("Введите количество учеников: ", min_value=1)

    students: list[JuniorSchoolStudent] = []

    for i in range(n):
        print(f"\n--- Ученик {i + 1} из {n} ---")
        student = SchoolInformationSystem().input_student()
        if student:
            students.append(student)

    school_system.populate_database_file(students)

    print("\nДанные сохранены в файл data_task2.bin")

    try:
        school_system.populate_students_from_database_file()
    except ValueError as e:
        print(f"Ошибка чтения файла данных: {e}")
        return

    school_system.print_students()


if __name__ == "__main__":
    main()