from pathlib import Path


def get_number(string: str) -> int:
    for s in string:
        if s.isdigit():
            return int(s)

    raise ValueError(f"No number found in string {string}")


numbers_map = {
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


def convert(string: str) -> str:
    for str_number, int_number in numbers_map.items():
        string = string.replace(
            str_number, f"{str_number[0]}{int_number}{str_number[-1]}"
        )

    return string


def main():
    # constants
    data_location = Path("./data/day_1_joyce.txt")

    with open(data_location, "r") as f:
        lines = f.readlines()

    # Part 1
    total = sum([get_number(line) * 10 + get_number(line[::-1]) for line in lines])
    print(f"Answer 1: {total=}")

    # Part 2
    converted_lines = [convert(line) for line in lines]
    total = sum(
        [get_number(line) * 10 + get_number(line[::-1]) for line in converted_lines]
    )
    print(f"Answer 2: {total=}")


if __name__ == "__main__":
    main()
