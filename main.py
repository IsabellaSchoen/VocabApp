

main_dictionary = {}


def asking_german():  # getting german word by putting english word in
    put_word = input()
    print(main_dictionary.get(put_word))

def asking_english(name):
    pass


def new_word():
    print("English Word:")
    new_key = input()
    print("German Word:")
    new_value = input()
    main_dictionary.update({new_key: new_value})


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

def start_dictionary():
    print("1: Adding new word to dictionary\n"
          "2: Searching german word\n"
          "3: Searching english word\n"
          "4: Showing the whole dictionary\n"
          "5: Exit\n"
          )
    print("Please enter your input: ")
    user_input = int(input())
    dictionary_categories(user_input)


if __name__ == '__main__':
    start_dictionary()