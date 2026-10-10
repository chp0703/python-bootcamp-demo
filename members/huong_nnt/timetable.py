
def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Python dictionary co the dung setdefault() de tao danh sach
    cho mot ngay neu ngay do chua ton tai.
    """
    result = {}

    # Gom cac mon hoc theo ngay
    for course, day in schedule:
        result.setdefault(day, []).append(course)

    # Sap xep cac mon trong tung ngay
    for day in result:
        result[day].sort()

    return result


schedule = [
    ("CSC10014", "Mon"),
    ("MTH00003", "Tue"),
    ("CSC10001", "Mon")
]

print(by_day(schedule))
