"""
Дан файл целых чисел, содержащий четное количество элементов. Удалить из данного
файла первую половину элементов.
"""

import numpy as np
import os

def read_int_data_from_bin_file(file_location: str):
    with open(file_location, "rb") as f:
        return np.fromfile(f, np.int32)

def remove_first_half_data_from_bin_file(file_location: str):
    total_size = os.path.getsize(file_location)
    bytes_to_remove = total_size // 2

    with open(file_location, 'rb') as f_read:
        f_read.seek(bytes_to_remove)
        remaining_data = f_read.read()

    with open(file_location, 'wb') as f_write:
        f_write.write(remaining_data)

def write_int_data_to_bin_file(file_location: str, data: list[int]):
    with open(file_location, "wb") as f:
        f.write(np.array(data).astype(np.int32).tobytes())

def main():
    write_int_data_to_bin_file("in3.bin", [1, 2, 3, 4, 5, 6])
    print(*read_int_data_from_bin_file("in3.bin"))
    remove_first_half_data_from_bin_file("in3.bin")
    print(*read_int_data_from_bin_file("in3.bin"))

if __name__ == "__main__":
    main()