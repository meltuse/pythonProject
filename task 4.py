if __name__ == '__main__':
    my_list = ('is', 'name', 'my')
    my_list = '{2} {1} {0}' .format(*my_list) .capitalize()
    print('{} {}' .format(my_list, 'Alan'))
    