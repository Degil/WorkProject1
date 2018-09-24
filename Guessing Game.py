import random

class Game:
    answer = random.randint(1,100)
    guess = int(input('Pick a number between 1 - 100: '))
    tries = 1
    while tries < 3:
        tries = tries + 1
        if answer == guess:
            print("CONGRATULATION")
            # break
        elif guess < answer:
            print('GO HIGHER ' + 'here\'s a hint... %s' % answer)

            guess = int(input('Pick a number between 1 - 100: '))
            print(tries)
            # break
        elif guess > answer:
            print('Think Smaller... ' + 'here\'s a hint... %s' % answer)
            guess = int(input('Pick a number between 1 - 100: '))
            print(tries)

            # break





print(Game.answer)