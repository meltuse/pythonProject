def fight(somenumber):
    hp = 100
    hp -= somenumber
    print('Your current hp is {}'.format(hp))
    return hp


def game_over(your_name):
    print('Game over' + your_name)


def forward():
    print('You go forward')


def left():
    print('You go left')


def right():
    print('You go right')


if __name__ == '__main__':
    forward()
    left()
    right()
    fight(15)
    game_over(' Alan ')
