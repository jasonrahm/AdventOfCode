"""
2022 Advent of Code - Day 5
"""
from aocd.models import Puzzle
from collections import deque
from itertools import islice, repeat
import re


def build_stack(data):
    head = list(islice(data, 0, 8))
    st1, st2, st3, st4, st5, st6, st7, st8, st9 = deque(), deque(), deque(), deque(), deque(), deque(), deque(), deque(), deque()
    for stackline in reversed(head):
        stacklist = list(stackline)
        if stacklist[1].isalpha():
            st1.append(stacklist[1])
        if stacklist[5].isalpha():
            st2.append(stacklist[5])
        if stacklist[9].isalpha():
            st3.append(stacklist[9])
        if stacklist[13].isalpha():
            st4.append(stacklist[13])
        if stacklist[17].isalpha():
            st5.append(stacklist[17])
        if stacklist[21].isalpha():
            st6.append(stacklist[21])
        if stacklist[25].isalpha():
            st7.append(stacklist[25])
        if stacklist[29].isalpha():
            st8.append(stacklist[29])
        if stacklist[33].isalpha():
            st9.append(stacklist[33])
    return {1: st1, 2: st2, 3: st3, 4: st4, 5: st5, 6: st6, 7: st7, 8: st8, 9: st9}


def part1(data):
    stacks = build_stack(data)

    moves = islice(data, 10, None)
    for move in moves:
        move_num, src, dst = re.findall(r'\d+', move)
        for _ in repeat(None, int(move_num)):
            container = stacks[int(src)].pop()
            stacks[int(dst)].append(container)

    return ''.join([q.pop() for q in stacks.values()])


def part2(data):
    stacks = build_stack(data)

    moves = islice(data, 10, None)
    for move in moves:
        move_num, src, dst = re.findall(r'\d+', move)
        pop_group = []
        for _ in repeat(None, int(move_num)):
            pop_group.append(stacks[int(src)].pop())
        stacks[int(dst)].extend(reversed(pop_group))

    return ''.join([q.pop() for q in stacks.values()])


if __name__ == '__main__':
    year, day = 2022, 5
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    # puzzle_data = [x for x in puzzle.example_data.split('\n')]
    puzzle_data = [x for x in puzzle.input_data.split('\n')]

    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')
