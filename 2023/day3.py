"""
2022 Advent of Code - Day 3
"""
import re
from aocd.models import Puzzle


def is_valid(row, col, grid_size):
    return 0 <= row <= grid_size[0] and 0 <= col <= grid_size[1]


def part1(data):
    # find symbols
    symbols = []
    for row, line in enumerate(data):
        for col, c in enumerate(line):
            if not c.isdigit() and c != '.':

                # store coords
                symbols.append((row, col))

    # find numbers
    numbers = []
    for row, line in enumerate(data):
        start = None
        number = ""
        for col, c in enumerate(line):
            if c.isdigit():
                if start is None:
                    start = col
                number += c
            elif start is not None:
                end = col
                # Add numbers and their coords
                numbers.append((int(number), [(row, c) for c in range(start, end)]))
                start = None
                number = ""

        # # Check for any pending number at the end of the row
        # if start is not None:
        #     numbers.append((int(number), [(row, c) for c in range(start, len(line))]))

    return symbols, numbers


# def part2(data):
#     return None


if __name__ == '__main__':
    year, day = 2023, 3
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    # puzzle_data = [x for x in puzzle.input_data.split('\n')]
    test_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]

    result1 = part1(test_data)
    # result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    # print(f'\tPart 2: {result2}')



# def parse_data(grid_data):
#     """Parse input."""
#     numbers, symbols = [], {}
#     parsing_number = False
#     for row, line in enumerate(grid_data):
#         for col, char in enumerate(line):
#             if char == ".":
#                 parsing_number = False
#                 continue
#             if not char.isdigit():
#                 parsing_number = False
#                 symbols[(col, row)] = char
#             if char.isdigit() and not parsing_number:
#                 number = ""
#                 parsing_number = True
#                 for digit in line[col:]:
#                     if digit.isdigit():
#                         number += digit
#                     else:
#                         break
#                 numbers.append((int(number), neighbors(len(number), col, row)))
#     return numbers, symbols