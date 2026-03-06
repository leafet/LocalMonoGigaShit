"""
ExamTaskC16. На вход подаются сведения о клиентах фитнес-центра. В первой строке
указывается код K одного из клиентов, во второй строке — целое число N, а каждая из
последующих N строк имеет формат
<Продолжительность занятий (в часах)> <Код клиента> <Год> <Номер месяца>
Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, код клиента —
в диапазоне 10–99, продолжительность занятий — в диапазоне 1–30. Для каждого года, в
котором клиент с кодом K посещал центр, определить месяц, в котором продолжительность
занятий данного клиента была наименьшей для данного года (если таких месяцев несколько,
то выбирать месяц с наибольшим номером; месяцы с нулевой продолжительностью занятий не
учитывать). Сведения о каждом годе выводить на новой строке в следующем порядке:
наименьшая продолжительность занятий, год, номер месяца. Упорядочивать сведения по
возрастанию продолжительности занятий, а при равной продолжительности — по
возрастанию номера года. Если данные о клиенте с кодом K отсутствуют, то вывести строку
«Нет данных».
"""

from GlobalTools.SharedInput import GINPT

import pickle

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
        self.database_file_location: str = "./data_task3.bin"

    @staticmethod
    def input_client():
        print("\nВведите данные клиента:")
        exercises_length = GINPT.get_int_input("Продолжительность занятий (1-30 часов): ", min_value=1, max_value=30)
        client_code = GINPT.get_int_input("Код клиента (10-99): ", min_value=10, max_value=99)
        year = GINPT.get_int_input("Год (2000-2010): ", min_value=2000, max_value=2010)
        month = GINPT.get_int_input("Номер месяца (1-12): ", min_value=1, max_value=12)


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

    def get_client_info_by_years(self, client_code: int):
        years_data = {}

        for client in self.clients:
            if client.client_code == client_code:
                if client.year not in years_data:
                    years_data[client.year] = {}
                years_data[client.year][client.mounth] = client.exercises_length

        if not years_data:
            return None

        result = []
        for year, months_data in years_data.items():
            min_duration = min(months_data.values())

            min_months = [month for month, duration in months_data.items()
                          if duration == min_duration]

            selected_month = max(min_months)

            result.append({
                'duration': min_duration,
                'year': year,
                'month': selected_month
            })

        result.sort(key=lambda x: (x['duration'], x['year']))

        return result

def main():
    fitness_center_system = FitnessCenterInfoSystem()

    k = GINPT.get_int_input("Введите код клиента: ", min_value=10, max_value=99)

    n = GINPT.get_int_input("Введите количество клиентов: ", min_value=1)

    clients = []

    for i in range(n):
        print(f"\n--- Клиент {i + 1} из {n} ---")
        client = fitness_center_system.input_client()
        if client:
            clients.append(client)

    fitness_center_system.populate_database_file_with_client_data(clients)

    print("\nДанные сохранены в файл data_task3.bin")

    try:
        fitness_center_system.populate_clients_from_database_file()
    except ValueError as e:
        print(f"Ошибка чтения файла данных: {e}")
        return

    fitness_center_system.show_all_records()

    print()
    print("Данные об активности клиента по годам")
    result = fitness_center_system.get_client_info_by_years(k)

    if result is None:
        print("Нет данных")
        return

    for item in result:
        print(f"Продолжительность {item['duration']} год {item['year']} месяц {item['month']}")

if __name__ == "__main__":
    main()