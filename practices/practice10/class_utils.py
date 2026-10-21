"""Helper module for the in-class practice (libraries)."""


def average(numbers):
    return round(sum(numbers) / len(numbers), 1)


def grade(score):
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    return "F"


if __name__ == "__main__":
    print("class_utils self-test")
    print(average([1, 2, 3]))
    print(grade(95))
