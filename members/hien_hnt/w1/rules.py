
def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append(f"need GPA >= 2.0 (current: {gpa:.2f})")
    return reasons


if __name__ == "__main__":
    print(can_register_thesis(118, 1.9))
    print(missing(118, 1.9))
