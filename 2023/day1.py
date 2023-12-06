"""
Advent of Code - Day 1
"""


def part1(data) -> int:
    calibration_value_sum: int = 0
    for l in data:
        digits_from_string = [x for x in l if x.isdigit()]
        calibration_value_sum += int(f'{digits_from_string[0]}{digits_from_string[-1]}')
    return calibration_value_sum


def part2(data):
    # not my solution...very slightly modified for clarity
    # https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/1.py
    numbers_as_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    calibration_value_sum = 0
    for l in data:
        nums = []
        for i, c in enumerate(l):
            if c.isdigit():
                nums.append(c)
            for d, s_num in enumerate(numbers_as_strings):
                if l[i:].startswith(s_num):
                    nums.append(str(d + 1))
        calibration_value_sum += int(nums[0] + nums[-1])
    return calibration_value_sum


if __name__ == '__main__':
    with open('day1.txt') as f:
        puzzle_data = [l.rstrip() for l in f]

    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data)

    print(f'Day 1 Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')
