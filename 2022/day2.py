"""
Advent of Code - Day 2
"""
from aocd.models import Puzzle

SCORING = {
    'A X': 4, # Rock = Rock, 1 + 3
    'A Y': 8, # Rock < Paper, 2 + 6
    'A Z': 3, # Rock > Scissors, 3 + 0
    'B X': 1, # Paper > Rock, 1 + 0
    'B Y': 5, # Paper = Paper, 2 + 3
    'B Z': 9, # Paper < Scissors, 3 + 6
    'C X': 7, # Scissors < Rock, 1 + 6
    'C Y': 2, # Scissors > Paper, 2 + 0
    'C Z': 6, # Scissors = Scissors, 3 + 3
}
SELECTORS = {
    'X': {'A': 'Z', 'B': 'X', 'C': 'Y'},
    'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'},
    'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'},
}


def part1(data):
    total_score = 0
    for round in data:
        total_score += SCORING.get(round)
    return total_score


def part2(data):
    total_score = 0
    for round in data:
        opponent, strategy = round.split()
        play = SELECTORS.get(strategy).get(opponent)
        total_score += SCORING.get(f'{opponent} {play}')
    return total_score


if __name__ == '__main__':
    year, day = 2022, 2
    puzzle = Puzzle(year, day)
    # This line changes with the data, massage as necessary:
    # puzzle_data = [x for x in puzzle.example_data.split('\n')]
    puzzle_data = [x for x in puzzle.input_data.split('\n')]

    result1 = part1(puzzle_data)
    result2 = part2(puzzle_data)

    print(f'{puzzle.title} Solutions:')
    print(f'\tPart 1: {result1}')
    print(f'\tPart 2: {result2}')
