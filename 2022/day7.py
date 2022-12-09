"""
2022 Advent of Code - Day 7
I didn't figure today out...may circle back when I have time, but this solution is
courtesy of https://github.com/alfredgamulo/advent_of_code/blob/main/2022/07/main.py

Learnings:
- don't overcomplicate things
- use well known tools for existing purposes like file systems
- match is like built-in regex, need to use this more
"""

import sys
from collections import defaultdict
from pathlib import Path


def run(lines):
    path = Path()
    filesizes = {}
    for line in lines:
        match line.split():
            case ("$", "cd", dir):
                path = path.joinpath(dir).resolve()
            case ("$", "ls"):
                ...
            case ("dir", dir):
                ...
            case (num, file):
                filesizes[path.joinpath(file)] = int(num)

    dir_sizes = defaultdict(int)
    for f, v in filesizes.items():
        for p in f.parents:
            dir_sizes[str(p)] += v

    p1_target = 100000  # magic number
    print("Part 1:", sum(v for v in dir_sizes.values() if v <= p1_target))

    p2_target = 30000000 - (70000000 - dir_sizes["/"])  # magic numbers
    for v in sorted(dir_sizes.values()):
        if v > p2_target:
            print("Part 2:", v)
            break


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    run(lines)
