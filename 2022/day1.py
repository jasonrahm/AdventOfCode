"""
Advent of Code - Day 1
"""
from aocd.models import Puzzle


def part1(data):
    return max([sum([int(x) for x in elf_snacks.split('\n')]) for elf_snacks in data])


def part2(data):
    return sum(sorted([sum([int(x) for x in elf_snacks.split('\n')]) for elf_snacks in data])[-3:])


if __name__ == '__main__':
    year, day = 2022, 1
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    puzzle_data = [x for x in puzzle.input_data.split('\n\n')]

    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')
