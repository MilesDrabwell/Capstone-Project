import time

import random

level = 1
strikes = 0


def refresh_page():
    return print('\n' * 100)


def countdown(n):
    for x in range(n):
        print('{} '.format(n - x), end=" ", flush=True)
        time.sleep(1)


def num_level(x):
    rand_num_str = ''
    for n in range(x):
        rand_num = random.randint(0, 9)
        rand_num_str += str(rand_num)
        print('{} '.format(rand_num), end=" ", flush=True)
        time.sleep(1)
    refresh_page()
    return rand_num_str


input('Get ready to start round 1 of the memory game.\nAnswer the numbers in the order given,\nrounds get increasingly difficult, You have 3 lives.\nPress enter to start the countdown ')

countdown(3)
refresh_page()

while strikes <= 2:
    answer = num_level(level)
    guess = input('Answer: ')
    if guess == answer:
        level += 1
        print('Correct! Next level coming up.')
        countdown(3)
        refresh_page()
        continue
    else:
        strikes += 1
        if strikes == 3:
            break
        print('Incorrect! The answer was {}\nYou have {} live(s) left'.format(
            answer, 3 - strikes))
        countdown(3)
        refresh_page()
        continue

print('Game over! The answer was {}\nYou made it to Level {}\n'.format(answer, level))


input('Now time for round 2!\nThis time after the numbers appear you need to answer the numbers in backwards order.\nPress enter to start the countdown ')
countdown(3)
refresh_page()

round_2_strikes = 0
round_2_level = 1

while round_2_strikes <= 2:
    answer = num_level(round_2_level)[::-1]
    guess = input('Answer: ')
    if guess == answer:
        round_2_level += 1
        print('Correct! Next level coming up.')
        countdown(3)
        refresh_page()
        continue
    else:
        round_2_strikes += 1
        if round_2_strikes == 3:
            break
        print('Incorrect! The answer was {}\nYou have {} live(s) left'.format(
            answer, 3 - round_2_strikes))
        countdown(3)
        refresh_page()
        continue


print('Game over!\nThe answer was {} \n'.format(answer))

print('Congratulations! You made it to Level:{} on round 1, and Level:{} on round 2.'.format(
    level, round_2_level))
