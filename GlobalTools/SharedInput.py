class GTLS:
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
