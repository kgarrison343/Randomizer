from random import randrange


def choose_randomly(choice_list: str):
    length = len(choice_list)
    return choice_list[randrange(0,length)]