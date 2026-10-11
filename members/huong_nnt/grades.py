def summary(scores: list[float]) -> dict:
    if len(scores) == 0:
        raise ValueError("Scores cannot be empty")

    minimum = min(scores)
    maximum = max(scores)

    mean = round(sum(scores) / len(scores), 2)

    ordered = sorted(scores)

    n = len(ordered)

    if n % 2 == 1:
        median = ordered[n // 2]
    else:
        middle1 = ordered[n // 2 - 1]
        middle2 = ordered[n // 2]
        median = (middle1 + middle2) / 2

    median = round(median, 2)

    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "median": median
    }


print(summary([7.5, 9, 6, 8]))
