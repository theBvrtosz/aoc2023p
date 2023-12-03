class AocDay:
    def __init__(self, day_number: int, test: bool) -> None:
        self.day_number = day_number
        self._read_day_input(test)

    def part1(self):
        raise NotImplementedError

    def part2(self):
        raise NotImplementedError

    def _read_day_input(self, test: bool):
        with open(
            f"./inputs/d{self.day_number}/d{self.day_number}-{'test-' if test else ''}input.txt",
            "r",
        ) as f:
            self.input_lines = f.read().splitlines()
