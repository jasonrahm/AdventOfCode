"""
2022 Advent of Code - Day 4
"""
import re
from aocd.models import Puzzle


def subset(r1, r2):
    return (r1.start in r2 and r1[-1] in r2) or (r2.start in r1 and r2[-1] in r1)


def part1(data):
    fully_contained = 0
    for elf_pair in data:
        e1x, e1y, e2x, e2y = re.findall(r'\d+', elf_pair)
        if subset(range(int(e1x), int(e1y) + 1), range(int(e2x), int(e2y) + 1)):
            fully_contained += 1
    return fully_contained


def part2(data):
    overlaps = 0
    for elf_pair in data:
        e1x, e1y, e2x, e2y = re.findall(r'\d+', elf_pair)
        if len(set.intersection(set(range(int(e1x), int(e1y) + 1)), set(range(int(e2x), int(e2y) + 1)))) > 0:
            overlaps += 1
    return overlaps


if __name__ == '__main__':
    year, day = 2022, 4
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    # puzzle_data = [x for x in puzzle.example_data.split('\n')]
    puzzle_data = [x for x in puzzle.input_data.split('\n')]

    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')
