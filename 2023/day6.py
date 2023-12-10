"""
2022 Advent of Code - Day 6

Part 1 - solved
Part 2 - solved
"""
from aocd.models import Puzzle
from math import sqrt


def part1(data):
    times = [int(x) for x in data[0].split()[1:]]
    distances = [int(x) for x in data[1].split()[1:]]
    result = 1
    for race_time, race_dist in zip(times, distances):
        qr1 = ((race_time - sqrt(race_time * race_time - 4 * race_dist)) / 2 + 1e-8).__ceil__()
        qr2 = ((race_time + sqrt(race_time * race_time - 4 * race_dist)) / 2 - 1e-8).__floor__()
        records = qr2 - qr1 + 1
        result *= records
    return result


def part2(data):
    race_time = int(''.join(data[0].split()[1:]))
    race_dist = int(''.join(data[1].split()[1:]))
    qr1 = ((race_time - sqrt(race_time * race_time - 4 * race_dist)) / 2).__ceil__()
    qr2 = ((race_time + sqrt(race_time * race_time - 4 * race_dist)) / 2).__floor__()
    return qr2 - qr1 + 1


if __name__ == '__main__':
    year, day = 2023, 6
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    puzzle_data = [x for x in puzzle.input_data.split('\n')]
    test_data = """Time:      7  15   30
Distance:  9  40  200""".split('\n')

    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')
