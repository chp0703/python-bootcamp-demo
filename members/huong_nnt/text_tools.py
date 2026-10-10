
def word_count(text: str) -> dict[str, int]:
    # Chuyen thanh chu thuong
    text = text.lower()

    # Thay dau cau bang khoang trang
    for mark in ".,!?:;":
        text = text.replace(mark, " ")

    # Tach van ban thanh cac tu
    words = text.split()

    # Tao dictionary rong
    counts = {}

    # Dem so lan xuat hien cua tung tu
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)

    # Chuyen dictionary thanh danh sach cac cap (tu, so lan)
    items = list(counts.items())

    # Sap xep: so lan giam dan, tu tang dan
    items.sort(key=lambda item: (-item[1], item[0]))

    # Lay k phan tu dau tien
    return items[:k]


print(word_count("Git is fun. Git is fast!"))
print(top_k("Git is fun. Git is fast!", 2))