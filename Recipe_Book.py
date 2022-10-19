from pathlib import Path
from os import system

def initializing_info():
    # This function sets in the intial variables for the program and passes them to main
    print("Hello and welcome to my test recipe book")
    user_name = input("Please provide your name: ")
    system("cls")
    working_directory = Path("C:\SampleRecipeBook\Recipes")
    # This could be updated to accept user provided input for the file location
    print(f"Hello {user_name}, the current recipe book location is set to: {working_directory}")
    print("Please ensure the recipe files included with this script are located there")
    input("Press 'Enter' to enter the recipe book")
    return (user_name, working_directory)

def count_recipes(working_directory):
    # This function provides a way to count the total numbers of recipes in the book, this can be called at anytime
    total_recipes = len(list(Path(working_directory).glob("**/*.txt")))
    return total_recipes

def display_menu(user_name, working_directory):
  # This is a function to build the main menu and to capture the user's menu choice
    system("cls")
    pretty_menu = "************************************************"
    user_selection_valid = False
    while not user_selection_valid:
        print(pretty_menu)
        print(f"User: {user_name}")
        print(f"Working Directory: {working_directory}")
        print(f"Total number of recipes: {count_recipes(working_directory)}")
        print(pretty_menu)
        print("MENU")
        print(pretty_menu)
        print(1)
        print(2)
        print(3)
        print(4)
        print(5)
        print(6)
        print(pretty_menu)
        user_menu_choice = int(input("Please pick a number from 1 to 6: "))
        if user_menu_choice in range(1, 6):
            return user_menu_choice
        else:
            system("cls")
            print("\nYour selection was not valid, please pick a number from the menu")
            input("Press 'enter' to pick again")
            print(pretty_menu)
            system("cls")

# MAIN
# Set user's name and working directory.
user_name, working_directory = initializing_info()
user_menu_choice = display_menu(user_name, working_directory)

### this is a work in progress
