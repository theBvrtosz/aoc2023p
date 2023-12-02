from days import (
    Day1,
)

DAY_MAP = {
    "day1": Day1
}

DAY_NUMBER = 1 

if __name__ == "__main__":
    day = DAY_MAP[f"day{DAY_NUMBER}"]()
    day_p1_solution = day.part1()
    day_p2_solution = day.part2()

    print(day_p1_solution)
    print(day_p2_solution)