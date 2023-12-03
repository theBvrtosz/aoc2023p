from .aoc_day import AocDay


class Day2(AocDay):
    def __init__(self) -> None:
        super().__init__(2, False)
        self.__parse_input()

    def __parse_input(self):
        self.parsed_games = {}
        for game in self.input_lines:
            game_splitted = game.split(":")
            game_id = int(game_splitted[0].replace("Game ", ""))
            cube_reveals = game_splitted[-1].split(";")
            self.parsed_games[game_id] = {}
            for reveal in cube_reveals:
                cubes = reveal.split(",")
                for cube in cubes:
                    cube_splitted = cube.strip().split(" ")
                    cubes_count, cubes_colour = int(cube_splitted[0]), cube_splitted[1]
                    if cubes_colour in self.parsed_games[game_id].keys():
                        cubes_count = max(
                            cubes_count, self.parsed_games[game_id][cubes_colour]
                        )
                    self.parsed_games[game_id][cubes_colour] = cubes_count

    def part1(self):
        red_cubes_count = 12
        green_cubes_count = 13
        blue_cubes_count = 14
        game_id_sum = 0
        for game_id in self.parsed_games:
            cubes = self.parsed_games[game_id]

            if (
                cubes["red"] <= red_cubes_count
                and cubes["green"] <= green_cubes_count
                and cubes["blue"] <= blue_cubes_count
            ):
                game_id_sum += game_id

        return game_id_sum

    def part2(self):
        sum_of_power = 0
        for game_id in self.parsed_games:
            game: dict = self.parsed_games[game_id]
            game_power = game.get("red", 1) * game.get("green", 1) * game.get("blue", 1)
            sum_of_power += game_power
        return sum_of_power
