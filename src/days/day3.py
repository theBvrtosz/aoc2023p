from .aoc_day import AocDay


class Day3(AocDay):
    def __init__(self) -> None:
        super().__init__(3, False)

    def __get_dotted_row(self, col_number):
        return "." * col_number

    def __add_dots_to_row(self, row):
        return "." + row + "."

    def __surround_table_with_dots(self):
        col_number = len(self.input_lines[0])
        surrounded_table = [self.__get_dotted_row(col_number)]
        for row in self.input_lines:
            surrounded_table.append(self.__add_dots_to_row(row))
        surrounded_table.append(self.__get_dotted_row(col_number))
        return surrounded_table

    def __find_numbers_in_row(self, row):
        numbers_in_row = []
        current_number = ""
        for char_idx in range(1, len(row)):
            char = row[char_idx]
            if char.isnumeric():
                current_number += char
                next_char = row[char_idx + 1]
                if not next_char.isnumeric():
                    numbers_in_row.append(current_number)
                    current_number = ""
        return numbers_in_row

    def __get_numbers_sum_from_row(self, row_idx, table, numbers):
        row = table[row_idx]
        row_sum = 0
        for number in numbers:
            number_start_idx = row.find(number)
            number_end_idx = number_start_idx + len(number) - 1

            previous_row_surronding = list(
                table[row_idx - 1][number_start_idx - 1 : number_end_idx + 2]
            )
            next_row_surrounding = list(
                table[row_idx + 1][number_start_idx - 1 : number_end_idx + 2]
            )
            chars_in_numbers_row = [
                row[number_start_idx - 1],
                row[number_end_idx + 1],
            ]

            chars_surrounding_number = set(
                previous_row_surronding + next_row_surrounding + chars_in_numbers_row
            )
            with open("gowno.txt", "a") as file:
                for char in chars_surrounding_number:
                    if not char.isnumeric() and char != ".":
                        row_sum += int(number)
                        break

        return row_sum

    def part1(self):
        input_table = self.__surround_table_with_dots()
        input_row_number = len(input_table)
        table_sum = 0

        for row_idx in range(1, input_row_number):
            row = input_table[row_idx]
            numbers_in_row = self.__find_numbers_in_row(row)
            row_sum = self.__get_numbers_sum_from_row(
                row_idx, input_table, numbers_in_row
            )
            table_sum += row_sum

        return table_sum

    def part2(self):
        return super().part2()
