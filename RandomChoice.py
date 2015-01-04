from random import randrange


def choose_randomly(choice_list: list):
    length = len(choice_list)
    return choice_list[randrange(0,length)]