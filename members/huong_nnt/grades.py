
def summary(scores: list[float]) -> dict:
    # Neu danh sach rong thi bao loi
    if len(scores) == 0:
        raise ValueError("Scores cannot be empty")

    # Tim diem nho nhat va lon nhat
    minimum = min(scores)
    maximum = max(scores)

    # Tinh diem trung binh, lam tron 2 chu so
    mean = round(sum(scores) / len(scores), 2)

    # Sap xep diem tu nho den lon
    ordered = sorted(scores)

    # Dem so luong diem
    n = len(ordered)

    # Tinh trung vi
    if n % 2 == 1:
        median = ordered[n // 2]
    else:
        middle1 = ordered[n // 2 - 1]
        middle2 = ordered[n // 2]
        median = (middle1 + middle2) / 2

    median = round(median, 2)

    # Tra ve dictionary
    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "median": median
    }


print(summary([7.5, 9, 6, 8]))
