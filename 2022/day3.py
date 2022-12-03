"""
Advent of Code - Day 3
"""
from aocd.models import Puzzle
from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def split5050(rucksack):
    half = int(len(rucksack) / 2)
    return rucksack[:half], rucksack[half:]


def get_priority(letter):
    if letter.isupper():
        offset = 38
    else:
        offset = 96
    return ord(letter) - offset


def part1(data):
    item_priorities = 0
    for rucksack in data:
        c1, c2 = split5050(rucksack)
        error_item = list(set(c1).intersection(set(c2)))[0]
        error_item_priority = get_priority(error_item)
        item_priorities += error_item_priority
    return item_priorities


def part2(data):
    badge_priorities = 0
    for rucksacks in grouper(data, 3):
        rs1, rs2, rs3 = rucksacks
        badge = list(set(rs1) & set(rs2) & set(rs3))[0]
        badge_priority = get_priority(badge)
        badge_priorities += badge_priority
    return badge_priorities


if __name__ == '__main__':
    year, day = 2022, 3
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    # puzzle_data = [x for x in puzzle.example_data.split('\n')]
    puzzle_data = [x for x in puzzle.input_data.split('\n')]

    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')
