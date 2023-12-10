"""
2022 Advent of Code - Day 3
   Part 1 - working on test data but not puzzle data, towel thrown
   Part 2 - unattempted
"""
import operator
from aocd.models import Puzzle


def part1(data):
    # find symbols
    neighbor_directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    symbols = []
    for row, line in enumerate(data):
        for col, c in enumerate(line):
            if not c.isdigit() and c != '.':
                # find neighbors
                neighbors = []
                for test_coord in neighbor_directions:
                    neighbor = tuple(map(operator.add, (row, col), test_coord))
                    neighbors.append(neighbor)
                # store coords
                symbols.append(((row, col), neighbors))

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
        if start is not None:
            numbers.append((int(number), [(row, c) for c in range(start, len(line))]))

    # Extract the coordinate lists from the tuples
    valid_numbers = []
    for symbol in symbols:
        symbol_neighbors = set(symbol[1])
        for number in numbers:
            number_coords = set(number[1])
            if number_coords.intersection(symbol_neighbors):
                valid_numbers.append(number[0])
    print(valid_numbers)
    return sum(set(valid_numbers))


# def part2(data):
#     return None


if __name__ == '__main__':
    year, day = 2023, 3
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    puzzle_data = [x for x in puzzle.input_data.split('\n')]
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

    result1 = part1(puzzle_data)
    # result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    # print(f'\tPart 2: {result2}')
