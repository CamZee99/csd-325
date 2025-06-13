import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (CHO) or odd (HAN) number.

*** NOTE: If you roll a 2 or a 7, you get a 10 mon bonus! ***
''')

purse = 5000
while True:  # Main game loop.
    # Change input prompt to initials and colon (CZ:)
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('CZ: ')  # Changed prompt here
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('CZ: ').upper()  # Changed prompt here
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    total = dice1 + dice2

    # If the total is 2 or 7, add 10 mon bonus to purse and notify player
    if total == 2 or total == 7:
        print(f'Bonus! The total is {total} - you get a 10 mon bonus!')
        purse += 10  # Added bonus to purse

    rollIsOdd = (total % 2 != 0)
    if rollIsOdd:
        correctBet = 'HAN'
    else:
        correctBet = 'CHO'

    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        # Changed house fee from 10% to 12%
        house_fee = pot * 12 // 100
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee
    else:
        purse -= pot
        print('You lost!')

    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
