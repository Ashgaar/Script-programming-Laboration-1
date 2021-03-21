from modules import input_numbers, game_numbers


def menu_graphic():
    print("[1] Delbarhet")
    print("[2] Gissa numret")
    print("[3] Avsluta")


def menu():
    menu_graphic()
    choice_menu = int(input())

    while choice_menu != 3:
        if choice_menu == 1:
            print()
            input_numbers()
        elif choice_menu == 2:
            print()
            game_numbers()
        else:
            print()
            print("Fel val försök igen. Skriv endast in giltiga nummer. (1-3)")

        print()
        menu_graphic()
        choice_menu = int(input())


menu()
