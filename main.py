

main_dictionary = {}


def asking_german():  # getting german word by putting english word in
    pass

def asking_english(name):
    pass


def new_word():
    pass


def dictionary_categories(category):
    if category == 1:
        print("Adding new word to your dictionary...")
        new_word()
    elif category == 2:
        print("Please enter the english word for which your looking the german word for...")
        asking_german()
    elif category == 3:
        print("Please enter the german word for which your looking the english word for...")
        asking_english()
    elif category == 4:
        print(main_dictionary)
    elif category == "exit":
        exit()
    else:
        print("Wrong input!")


if __name__ == '__main__':
    user_input = input()
    dictionary_categories(user_input)