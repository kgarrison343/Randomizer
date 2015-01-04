from RandomChoice import choose_randomly
from os import listdir


def list_files(files: list):
    print("What file would you like to choose from?")
    for i, file in enumerate(files):
        print(str(i + 1) + ". " + file)


def main():
    files = listdir("./Choices")
    list_files(files)
    choice = int(input())
    choice_file = ''
    if 0 < choice < len(files) + 1:
        choice_file = "./Choices/" + files[choice - 1]
    else:
        print("That is not a valid number, try again")

    with open(choice_file) as f:
        choices = [x.strip('\n') for x in f.readlines()]
    print(choose_randomly(choices))
    choice = input("q to exit, any other to choose again\n")
    return choice == 'q' or choice == 'Q'

if __name__ == "__main__":
    done = False
    while not done:
        done = main()