"""
Дан файл вещественных чисел. Создать файл целых чисел, содержащий длины всех
убывающих последовательностей элементов исходного файла. Например, для исходного файла
с элементами 1.7, 4.5, 3.4, 2.2, 8.5, 1.2 содержимое результирующего файла должно быть
следующим: 3, 2.
"""

import numpy as np

def get_descending_series_lengths(series: list[float]):
    arr = np.array(series)

    diff = np.diff(arr)
    break_points = np.where(diff > 0)[0] + 1

    sequences = np.split(arr, break_points)

    return [len(seq.tolist()) for seq in sequences if len(seq) > 1 and all(np.diff(seq) < 0)]

def read_float_data_from_bin_file(file_location: str):
    with open(file_location, "rb") as f:
        return np.fromfile(f, np.float32)

def read_int_data_from_bin_file(file_location: str):
    with open(file_location, "rb") as f:
        return np.fromfile(f, np.int32)

def write_float_data_to_bin_file(file_location: str, data: list[float]):
    with open(file_location, "wb") as f:
        f.write(np.array(data).astype(np.float32).tobytes())

def write_int_data_to_bin_file(file_location: str, data: list[int]):
    with open(file_location, "wb") as f:
        f.write(np.array(data).astype(np.int32).tobytes())

def main():
    write_float_data_to_bin_file("in.bin", [3, 2, 1, 0, -34, 3, 2, 5, 4, 5, 2, 43, 34, 23, 12, 11, 1])

    series_array_to_process = read_float_data_from_bin_file("in.bin").tolist()
    series_lengths = get_descending_series_lengths(series_array_to_process)
    write_int_data_to_bin_file("out.bin", series_lengths)
    print(*read_int_data_from_bin_file("out.bin"), sep=", ")

if __name__ == '__main__':
    main()
