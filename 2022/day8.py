"""
2022 Advent of Code - Day 8
"""
from aocd.models import Puzzle
import pandas as pd


def part1(data):
    grid = []
    for line in data:
        grid.append(list(line))
    df = pd.DataFrame(grid)
    rows = len(df.axes[0])
    cols = len(df.axes[1])
    visible_trees = (rows * 2) + (cols * 2) - 4
    for row in range(rows-2):
        for col in range(cols-2):
            cell_height = int(grid[row+1][col+1])
            col_heights = df.iloc[:, col+1].tolist()
            row_heights = df.iloc[row+1, :].tolist()
            left = [int(x) for x in row_heights[:col+1]]
            right = [int(x) for x in row_heights[col+2:]]
            top = [int(x) for x in col_heights[:row+1]]
            bottom = [int(x) for x in col_heights[row+2:]]
            if all(tree < cell_height for tree in left):
                visible_trees += 1
            elif all(tree < cell_height for tree in top):
                visible_trees += 1
            elif all(tree < cell_height for tree in right):
                visible_trees += 1
            elif all(tree < cell_height for tree in bottom):
                visible_trees += 1
    return visible_trees


def part2(data):
    best_view = 0
    grid = []
    for line in data:
        grid.append(list(line))
    df = pd.DataFrame(grid)
    rows = len(df.axes[0])
    cols = len(df.axes[1])
    for row in range(rows-2):
        for col in range(cols-2):
            cell_height = int(grid[row+1][col+1])
            col_heights = df.iloc[:, col+1].tolist()
            row_heights = df.iloc[row+1, :].tolist()
            left = [int(x) for x in row_heights[:col+1]]
            right = [int(x) for x in row_heights[col+2:]]
            top = [int(x) for x in col_heights[:row+1]]
            bottom = [int(x) for x in col_heights[row+2:]]
            ld = td = rd = bd = 0

            for i, item in enumerate(reversed(left)):
                if item <= cell_height:
                    ld += 1
                    if item == cell_height:
                        break
                elif item > cell_height:
                    ld += 1
                    break
            for i, item in enumerate(reversed(top)):
                if item <= cell_height:
                    td += 1
                    if item == cell_height:
                        break
                elif item > cell_height:
                    td += 1
                    break
            for i, item in enumerate(right):
                if item <= cell_height:
                    rd += 1
                    if item == cell_height:
                        break
                elif item > cell_height:
                    rd += 1
                    break
            for i, item in enumerate(bottom):
                if item <= cell_height:
                    bd += 1
                    if item == cell_height:
                        break
                elif item > cell_height:
                    bd += 1
                    break

            current_view = ld * td * rd * bd
            if current_view > best_view:
                best_view = current_view
    return best_view


if __name__ == '__main__':
    year, day = 2022, 8
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    # puzzle_data = [x for x in puzzle.example_data.split('\n')]
    puzzle_data = [x for x in puzzle.input_data.split('\n')]

    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')