"""
2022 Advent of Code - Day X

Part 1 -
Part 2 -
"""
from aocd.models import Puzzle


def part1(data):
    return None


# def part2(data):
#     return None


if __name__ == '__main__':
    year, day = 2023, 1
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    puzzle_data = [x for x in puzzle.input_data.split('\n')]

    result1 = part1(puzzle_data)
    # result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    # print(f'\tPart 2: {result2}')
