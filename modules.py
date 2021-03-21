from random import randint


def input_numbers():

    first_number = int(input('Skriv i första siffran: '))
    second_number = int(input('Skriv i andra siffran: '))

    print()
    print(f"Delbart med {first_number} och {second_number}:")
    print()
    for i in divide_numbers(first_number, second_number):
        print(i, end=" ")
    print()


def divide_numbers(first_number, second_number):
    division_numbers_list = []

    for i in range(1, 1001):
        if i % first_number == 0 and i % second_number == 0:
            division_numbers_list.append(i)

    return division_numbers_list


def game_numbers():
    random_number = randint(1, 100)

    print("Försöka att gissa numret mellan 1-100.")

    guess_number = int(input())

    guesses_total = 1

    while guess_number != random_number:

        if random_number > guess_number:
            print("För lågt, gissa igen.")
        else:
            print("För högt, gissa igen.")

        try:
            guess_number = int(input())
        except ValueError:
            print("Skriv en endast in giltiga nummer2")

        guesses_total += 1

    print(
        f"Du gissade rätt på talet {random_number}! Det tog {guesses_total} försök.")
