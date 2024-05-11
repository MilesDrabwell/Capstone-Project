import time

import random

level = 1


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


input('Get ready to start round 1 of the memory game.\nAnswer the numbers in the order given,\nrounds get increasingly difficult.\nPress enter to start the countdown ')

countdown(3)
refresh_page()

while level >= 0:
    answer = num_level(level)
    guess = input('Answer: ')
    if guess == answer:
        level += 1
        print('Correct! Next level coming up.')
        countdown(3)
        refresh_page()
        continue
    else:
        print('Game over!\nThe answer was {} \nYou made it to Level {}\n'.format(
            answer, level))
        break

input('Now time for round 2!\nThis time after the numbers appear you need to answer the numbers in backwards order.\nPress enter to start the countdown ')
countdown(3)
refresh_page()

round_2_level = 1

while round_2_level >= 0:
    answer = num_level(round_2_level)[::-1]
    guess = input('Answer: ')
    if guess == answer:
        round_2_level += 1
        print('Correct! Next level coming up.')
        countdown(3)
        refresh_page()
        continue
    else:
        print('Game over!\nThe answer was {} \nYou made it to Level {}\n'.format(
            answer, round_2_level))
        break

print('Congratulations! You made it to Level:{} on round 1, and Level:{} on round 2.'.format(
    level, round_2_level))
