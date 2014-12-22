from os import listdir
from random import randrange


def choose_randomly(choice_list):
    length = len(choice_list)
    return choice_list[randrange(0,length)]


def main():
    files = listdir("./Choices")
    print("What file would you like to choose from?")
    for i, file in enumerate(files):
        print(str(i + 1) + ". " + file)

    choice = int(input())
    choice_file = ''
    if 0 < choice < len(files) + 1:
        choice_file = "./Choices/" + files[choice - 1]
    else:
        print("That is not a valid number, goodbye")

    with open(choice_file) as f:
        choices = [x.strip('\n') for x in f.readlines()]
    print(choose_randomly(choices))
    choice = input("q to exit, any other to choose again\n")
    return choice == 'q' or choice == 'Q'

if __name__ == "__main__":
    done = False
    while not done:
        done = main()