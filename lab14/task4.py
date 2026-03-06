"""
Даны три файла вещественных чисел с именами S1, S2 и S3, элементы которых
упорядочены по убыванию. Объединить эти файлы в новый файл с именем S4 так, чтобы его
элементы также оказались упорядоченными по убыванию.
"""
import numpy as np

def read_float_data_from_bin_file(file_location: str):
    with open(file_location, "rb") as f:
        return np.fromfile(f, np.float32)

def write_float_data_to_bin_file(file_location: str, data: list[float]):
    with open(file_location, "wb") as f:
        f.write(np.array(data).astype(np.float32).tobytes())

def join_files_keeping_descending_order_of_content(in_files: list[str], out_file: str):
    output_to_write = []

    for file in in_files:
        output_to_write.extend(read_float_data_from_bin_file(file).tolist())

    output_to_write.sort(reverse=True)

    write_float_data_to_bin_file(out_file, output_to_write)

def main():
    write_float_data_to_bin_file("S1.bin", [10.0, 8.1, 4.2, 3.3])
    write_float_data_to_bin_file("S2.bin", [8.2, 4.1, 3.2, 2.1])
    write_float_data_to_bin_file("S3.bin", [4.0, 3.1, 2.0, 1.0])

    file_names = ["S1.bin", "S2.bin", "S3.bin"]

    for file in file_names:
        print(*read_float_data_from_bin_file(file))

    join_files_keeping_descending_order_of_content(file_names, "S4.bin")

    print(*read_float_data_from_bin_file("S4.bin"))

if __name__ == "__main__":
    main()
