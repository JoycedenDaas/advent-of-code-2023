from pathlib import Path

NUMBERS_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_number(string: str) -> str:
    for s in string:
        if s.isdigit():
            return s

    raise ValueError(f"No number found in string {string}")


def get_calibration_value(line: str) -> int:
    return int(get_number(line) + get_number(reversed(line)))


def convert(string: str) -> str:
    # Keep start and end letter
    for s, num in NUMBERS_MAP.items():
        string = string.replace(s, f"{s[0]}{num}{s[-1]}")

    return string


def main():
    # constants
    data_location = Path("./data/day_1.txt")

    with open(data_location, "r") as f:
        lines = f.readlines()

    # Part 1
    total = sum([get_calibration_value(line) for line in lines])
    print(f"Answer 1: {total=}")

    # Part 2
    total = sum([get_calibration_value(convert(line)) for line in lines])
    print(f"Answer 2: {total=}")


if __name__ == "__main__":
    main()
