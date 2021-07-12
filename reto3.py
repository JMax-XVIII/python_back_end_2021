from os import system

bill_5 = 5
bill_20 = 20
bill_50 = 50
bill_100 = 100
bill_200 = 200
bill_500 = 500

total_price = 0

menu = []
plate_price = []

complete_menu = {}

def get_menu(intro_menu, intro_plate_price):

    global complete_menu
    global menu
    global plate_price

    menu = intro_menu
    plate_price = intro_plate_price

    if len(intro_menu) != len(intro_plate_price):
        print("Menu Plates and Plate's Price do not match")
    else:
        for arranger in range(len(intro_menu)):
            complete_menu.update({intro_menu[arranger]: intro_plate_price[arranger]})

def print_menu():
    global complete_menu
    for plate in complete_menu:
        print(plate + ": " + str(complete_menu[plate]) + " €")

def check_menu(options):

    global complete_menu
    global menu
    not_in_menu = []
    error = False
    for opt in options:
        if opt not in menu:
            not_in_menu.append(opt)
    if len(not_in_menu) > 0:
        print("The Following Plates are not in the Menu: ")
        for no_menu in not_in_menu:
            print(no_menu + "\n")
            error = True
    return error

def get_total_price(command):

    global complete_menu
    global total_price
    global menu

    for plate in command:
        if plate in menu:
            total_price += complete_menu[plate]
            print(plate + ": " + str(complete_menu[plate]))
    print("Total Amount: " + str(total_price))

def pick_menu():
    global complete_menu
    total_commnad = []
    while True:
        print_menu()
        command = input("what would you like to eat?: ")
        total_commnad.append(command)
        print("do you want to order something else?\n")
        keep_ordering = input("(Yes / No)\n")
        if keep_ordering.lower()[0] == "y":
            system('cls')
            continue
        else:
            break

    if check_menu(total_commnad) is False:
        get_total_price(total_commnad)

if __name__ == "__main__":
    intro_menu = ["Chicken with Fries", "Spaghetti Meat Balls" , "Cesar Salad", "Spicy Hamburger", "Ham Sandwich", "fo", "fa"]
    intro_plate_price = [10, 13, 8, 18, 20, 10, 4]
    get_menu(intro_menu, intro_plate_price)
    pick_menu()
