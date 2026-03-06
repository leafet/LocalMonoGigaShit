"""
Даны имена четырех файлов. Найти количество файлов с указанными именами, которые
имеются в текущем каталоге.
"""

from pathlib import Path

def find_files_with_specified_names(filenames: list[str]) -> int:
    path = Path('.')
    return sum(1 for entry in path.iterdir() if entry.is_file() and entry.stem in filenames)

def main():
    while True:
        input_command = input("Введите через пробел названия 4 файлов для поиска с расширением .bin "
                              "или добавьте EXIT в ввод для выхода из программы: ").split(" ")

        if len(input_command) != 4:
            print("Неверное количество аргументов")
            continue

        if 'EXIT' in input_command:
            break

        print(find_files_with_specified_names(input_command))


if __name__ == '__main__':
    main()