"""
2022 Advent of Code - Day 6
"""
from aocd.models import Puzzle
from collections import Counter, deque


def part1(data):
    chars = deque(maxlen=4)
    marker_index = 0
    for i, c in enumerate(data[0]):
        chars.append(c)
        if len(Counter(chars)) == 4:
            marker_index = i + 1
            break
    return marker_index


def part2(data, skip_count):
    chars = deque(maxlen=14)
    marker_index = 0
    for i, c in enumerate(data[0][skip_count-1:]):
        chars.append(c)
        if len(Counter(chars)) == 14:
            print(Counter(chars))
            marker_index = skip_count + i
            break
    return marker_index


if __name__ == '__main__':
    year, day = 2022, 6
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    # puzzle_data = [x for x in puzzle.example_data.split('\n')]
    puzzle_data = [x for x in puzzle.input_data.split('\n')]

    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data, result1)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')