from os import listdir
from os.path import isfile, join
from random import randrange


def choose_randomly(choice_list):
    length = len(choice_list)
    return choice_list[randrange(0,length)]

if __name__ == "__main__":
    files = listdir("./Choices")
    print("What file would you like to choose from?")
    for i, file in enumerate(files):
        print(str(i + 1) + ". " + file)

    choice = int(input())
    choiceFile = ''
    if 0 < choice < len(files) + 1:
        choiceFile = "./Choices/" + files[choice - 1]
    else:
        print("That is not a valid number, goodbye")

    with open(choiceFile) as f:
        choices = [x.strip('\n') for x in f.readlines()]
    print(choose_randomly(choices))
    input("press any key to exit...")