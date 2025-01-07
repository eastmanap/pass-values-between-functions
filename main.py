# Apollos & Isaac
# 1/7/2025
# Pairs activity 3

import random

# rand_num()
def rand_num():
    randnum = random.randint(1, 25)
    return randnum

# get_user_input()
def get_user_input():
    response = input('\nType a number between 1 and 25:')
    return int(response)

# square()

def square(num):
    result = num ** 2
    return result

answer1 = rand_num()
answer2 = get_user_input()

if answer2 > 25 or answer2 < 1:
    print('\nERROR: Invalid input, please try again.\n')
    quit()

final_answer1 = square(answer1)
final_answer2 = square(answer2)

print(f'\nYour randomly generated number was {answer1} and the square of it was {final_answer1}.')
print(f'Your inputted number was {answer2} and the square of it was {final_answer2}.\n')
