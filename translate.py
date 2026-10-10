"""W1.4: Bài của member 2 - insertion sort tại chỗ."""


def insertion_sort(values: list[int]) -> list[int]:
    """Sắp xếp tăng dần ngay trên list đầu vào và trả về chính list đó.

    Mỗi bước chèn một phần tử vào đoạn bên trái đã được sắp xếp.
    Khác cú pháp C++ for (int i = 1; i < n; ++i), Python dùng
    for i in range(1, len(values)) và thụt lề để xác định khối lệnh.
    """
    for i in range(1, len(values)):
        current = values[i]
        j = i - 1
        while j >= 0 and values[j] > current:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = current
    return values


if __name__ == "__main__":
    numbers = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(numbers))
