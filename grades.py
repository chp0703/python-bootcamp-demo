def summary(scores: list[float]) -> dict[str, float]:
    if not scores:
        raise ValueError("scores must not be empty")

    ordered = sorted(scores)
    count = len(ordered)
    middle = count // 2

    if count % 2 == 1:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2

    return {
        "min": ordered[0],
        "max": ordered[-1],
        "mean": round(sum(scores) / count, 2),
        "median": round(median, 2),
    }


if __name__ == "__main__":
    print(summary([7.5, 9, 6, 8]))
