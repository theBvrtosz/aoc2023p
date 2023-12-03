from .aoc_day import AocDay

import re


class Day1(AocDay):
    def __init__(self) -> None:
        super().__init__(1, False)

    def __remove_non_numerics_from_calibration_values(self, calibration_values):
        return (
            re.sub("[^0-9]", "", calibration_value)
            for calibration_value in calibration_values
        )

    def __extract_two_digit_from_calibration_values(self, calibration_values):
        return (
            int(f"{numeric_value[0]}{numeric_value[-1]}")
            for numeric_value in calibration_values
            if len(numeric_value) > 0
        )

    def part1(self):
        extracted_numerics = self.__remove_non_numerics_from_calibration_values(
            self.input_lines
        )
        two_digit_numerics = self.__extract_two_digit_from_calibration_values(
            extracted_numerics
        )
        return sum(two_digit_numerics)

    def part2(self):
        spelled_numbers = {
            "one": "one1one",
            "two": "two2two",
            "three": "three3three",
            "four": "four4four",
            "five": "five5five",
            "six": "six6six",
            "seven": "seven7seven",
            "eight": "eight8eight",
            "nine": "nine9nine",
        }
        no_spelled_numerics = []
        for corrupted_value in self.input_lines:
            for spelled_number in spelled_numbers.keys():
                corrupted_value = corrupted_value.replace(
                    spelled_number, spelled_numbers[spelled_number]
                )
            no_spelled_numerics.append(corrupted_value)

        extracted_numerics = self.__remove_non_numerics_from_calibration_values(
            no_spelled_numerics
        )
        two_digit_numerics = self.__extract_two_digit_from_calibration_values(
            extracted_numerics
        )
        return sum(two_digit_numerics)
