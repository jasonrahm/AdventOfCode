"""
2022 Advent of Code - Day 4

Part 1 - solved
Part 2 - unattempted
"""
from aocd.models import Puzzle


def part1(data):
    total_points = 0
    for line in data:
        points = 0
        winning_numbers, my_numbers = line.split(':')[1].split('|')
        winning_numbers = set([int(num) for num in winning_numbers.split() if num.strip()])
        my_numbers = set([int(num) for num in my_numbers.split() if num.strip()])
        matching_numbers = len(winning_numbers.intersection(my_numbers))
        if matching_numbers == 1:
            total_points += 1
        elif matching_numbers > 1:
            total_points += 1 * 2 ** (matching_numbers - 1)

    return total_points


# def part2(data):
#     return None


if __name__ == '__main__':
    year, day = 2023, 4
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    puzzle_data = [x for x in puzzle.input_data.split('\n')]
    test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')

    result1 = part1(puzzle_data)
    # result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    # print(f'\tPart 2: {result2}')
