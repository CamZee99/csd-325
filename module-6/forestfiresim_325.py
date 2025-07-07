"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = 'L'  # New constant for lake

# Probability settings
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                current = forest[(x, y)]

                # Preserve water tiles exactly as-is
                if current == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                # Grow tree in empty space
                if current == EMPTY and random.random() <= GROW_CHANCE:
                    nextForest[(x, y)] = TREE

                # Tree struck by lightning
                elif current == TREE and random.random() <= FIRE_CHANCE:
                    nextForest[(x, y)] = FIRE

                # Fire spreads to neighbors
                elif current == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = (x + ix, y + iy)
                            if (ix == 0 and iy == 0) or neighbor not in forest:
                                continue
                            if forest.get(neighbor) == TREE:
                                nextForest[neighbor] = FIRE
                    nextForest[(x, y)] = EMPTY

                else:
                    nextForest[(x, y)] = current  # Copy unchanged

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest with a lake in the center."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    
    # Define lake region (roughly centered)
    lake_left = WIDTH // 3
    lake_right = 2 * WIDTH // 3
    lake_top = HEIGHT // 3
    lake_bottom = 2 * HEIGHT // 3

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if lake_left <= x <= lake_right and lake_top <= y <= lake_bottom:
                forest[(x, y)] = WATER  # Place lake
            elif random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def displayForest(forest):
    """Display the forest with colored output."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            tile = forest[(x, y)]
            if tile == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif tile == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif tile == WATER:
                bext.fg('blue')
                print(WATER, end='')
            else:
                print(EMPTY, end='')
        print()
    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()



# 1. Added WATER = 'L' as a new constant for the lake.
# 2. Modified createNewForest():
#    - Defined a rectangular "lake" in the center of the forest.
#    - Lake cells are initialized with WATER and cannot be overwritten.
# 3. Modified main():
#    - Added a check to prevent WATER cells from being changed.
#    - Fire does not spread into or across WATER cells.
# 4. Modified displayForest():
#    - Displays WATER cells in blue using bext.fg('blue').
