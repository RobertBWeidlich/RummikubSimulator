import pprint as pp
import random
import sys
import os

"""
Basic data structures for the game:
    tile:  tuple in the form ('red', 7)
    
    pool: list of tiles to be selected by players
    
    rack_a: list of Player A's tiles
    rack_b: list of Player B's tiles
    
    group: 3 or 4 tiles, same number, all different colors
    groups: list of groups
    
    run: 3 or more consecutive numbered tiles, same color
    runs: list of runs 
    
    set: group or run
"""

JOKER = 99

red_tiles = [
    ('red', 1), ('red', 2), ('red', 3), ('red', 4), ('red', 5),
    ('red', 6), ('red', 7), ('red', 8), ('red', 9), ('red', 10),
    ('red', 11), ('red', 12), ('red', 13), ('red', JOKER)]
black_tiles = [
    ('black', 1), ('black', 2), ('black', 3), ('black', 4), ('black', 5),
    ('black', 6), ('black', 7), ('black', 8), ('black', 9), ('black', 10),
    ('black', 11), ('black', 12), ('black', 13), ('black', JOKER)
]
blue_tiles = [
    ('blue', 1), ('blue', 2), ('blue', 3), ('blue', 4), ('blue', 5),
    ('blue', 6), ('blue', 7), ('blue', 8), ('blue', 9), ('blue', 10),
    ('blue', 11), ('blue', 12), ('blue', 13)
]
orange_tiles = [
    ('orange', 1), ('orange', 2), ('orange', 3), ('orange', 4), ('orange', 5),
    ('orange', 6), ('orange', 7), ('orange', 8), ('orange', 9), ('orange', 10),
    ('orange', 11), ('orange', 12), ('orange', 13)
]

all_tiles = red_tiles + black_tiles + blue_tiles + orange_tiles

pool = all_tiles.copy()
random.shuffle(pool)

rack_a = []
rack_b = []

groups = []
runs = []


def play():
    print("initial pool: ")
    pp.pprint(pool)

    # 1. Randomly choose either Player A or B to start
    first_player = random.choice(('a', 'b'))
    print(f'first player: {first_player}')

    # 2. Fill each player's racks with 13 tiles from the pool
    # tile1 = pool.pop(0)
    for i in range(0, 13):
        print(i)
        rack_a.append(pool.pop(0))
        rack_b.append(pool.pop(0))

    print("rack_a: ")
    pp.pprint(rack_a)

    print("rack_b: ")
    pp.pprint(rack_b)

    print("pool after each of 2 player gets 13 tiles: ")
    pp.pprint(pool)


if __name__ == '__main__':
    play()

    sys.exit(0)
