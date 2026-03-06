"""
На вход подаются сведения о клиентах фитнес-центра. В первой строке
указывается целое число N, а каждая из последующих N строк имеет формат
<Номер месяца> <Год> <Код клиента> <Продолжительность занятий (в часах)>
Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, код клиента —
в диапазоне 10–99, продолжительность занятий — в диапазоне 1−30. Найти строку исходных
данных с максимальной продолжительностью занятий. Вывести эту продолжительность, а
также соответствующие ей год и номер месяца (в указанном порядке). Если имеется несколько
строк с максимальной продолжительностью, то вывести данные, соответствующие самой
поздней дате.
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


class FitnessCenterClientRecord:
    def __init__(self, mounth: int, year: int, client_code: int, exercises_length: int):
        if mounth < 0 or mounth > 12:
            raise ValueError("mounth must be between 0 and 12")
        if year < 2000 or year > 2010:
            raise ValueError("year must be between 0 and 2000")
        if client_code < 10 or client_code > 99:
            raise ValueError("client_code must be between 10 and 99")
        if exercises_length < 1 or exercises_length > 30:
            raise ValueError("exercises_length must be between 1 and 30")

        self.mounth = mounth
        self.year = year
        self.client_code = client_code
        self.exercises_length = exercises_length

    def __str__(self):
        return f"Количество часов {self.exercises_length} у клиента {self.year} года в {self.mounth} месяце"

class FitnessCenterInfoSystem:
    def __init__(self):
        self.clients: list[FitnessCenterClientRecord] = []
        self.database_file_location: str = "./data_task1.bin"

    @staticmethod
    def input_client():
        print("\nВведите данные клиента:")
        month = get_int_input("Номер месяца (1-12): ", min_value=1, max_value=12)
        year = get_int_input("Год (2000-2010): ", min_value=2000, max_value=2010)
        client_code = get_int_input("Код клиента (10-99): ", min_value=10, max_value=99)
        exercises_length = get_int_input("Продолжительность занятий (1-30 часов): ", min_value=1, max_value=30)

        return FitnessCenterClientRecord(month, year, client_code, exercises_length)

    def populate_database_file_with_client_data(self, clients_data: list[FitnessCenterClientRecord]):
        with open(self.database_file_location, "wb") as f:
            pickle.dump(clients_data, f)

    def populate_clients_from_database_file(self):
        with open(self.database_file_location, "rb") as f:
            try:
                self.clients = pickle.load(f)
            except ValueError as e:
                raise e

    def show_all_records(self):
        for client in self.clients:
            print(f"{client} с кодом {client.client_code}")

    def find_maximal_exercise_record(self):
        maximal_ex_len = max(self.clients, key=lambda client: client.exercises_length).exercises_length

        maximals = [record for record in self.clients if record.exercises_length == maximal_ex_len]

        return max(maximals, key=lambda client: (client.year, client.mounth))

def main():
    fitness_center_system = FitnessCenterInfoSystem()

    n = get_int_input("Введите количество клиентов: ", min_value=1)

    clients = []

    for i in range(n):
        print(f"\n--- Клиент {i + 1} из {n} ---")
        client = fitness_center_system.input_client()
        if client:
            clients.append(client)

    fitness_center_system.populate_database_file_with_client_data(clients)

    print("\nДанные сохранены в файл data_task1.bin")

    try:
        fitness_center_system.populate_clients_from_database_file()
    except ValueError as e:
        print(f"Ошибка чтения файла данных: {e}")
        return

    fitness_center_system.show_all_records()

    print()

    result = fitness_center_system.find_maximal_exercise_record()
    print(f"Максимальная продолжительность: {result.exercises_length} часов")
    print(f"Год: {result.year}, Месяц: {result.mounth}")

if __name__ == "__main__":
    main()