def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:

    grouped: dict[str, list[str]] = {}
    for course, day in courses:
        grouped.setdefault(day, []).append(course)
    return {day: sorted(day_courses) for day, day_courses in grouped.items()}


if __name__ == "__main__":
    print(by_day([("CSC1001", "Mon"), ("MTH0003", "Tue"), ("CSC1000", "Mon")]))
