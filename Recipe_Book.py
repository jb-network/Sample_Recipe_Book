import os.path
import time
from pathlib import Path
from os import system, path

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
        print("1 - Read recipes")
        print("2 - Create a new recipe")
        print("3 - Create a new recipe category")
        print("4 - Delete recipes")
        print("5 - Delete a recipe category")
        print("6 - Exit the program")
        print(pretty_menu)
        user_menu_choice = int(input("Please pick a number from 1 to 6: "))
        if user_menu_choice in range(1, 7):
            system("cls")
            return user_menu_choice
        else:
            system("cls")
            print("\nYour selection was not valid, please pick a number from the menu")
            input("Press 'enter' to pick again")
            print(pretty_menu)
            system("cls")

def get_categories(working_directory, user_goal):
    valid_choice = False
    pretty_menu = "************************************************"
    while not valid_choice:
        print(pretty_menu)
        kv_tracker = {}
        menu_number = 1
        for items in working_directory.iterdir():
            kv_tracker[menu_number] = items
            print("{}: {}".format(menu_number, path.basename(items)))
            menu_number += 1
        user_directory_choice = int(input(f"Please select a category of recipes to {user_goal}: "))
        if user_directory_choice in range(1,menu_number):
            set_user_choice = kv_tracker.get(user_directory_choice)
            system("cls")
            return(set_user_choice)
        else:
            print(f"The number: {user_directory_choice} is not a valid choice")
            print(pretty_menu)
            input("Press enter to make another choice")
            system("cls")

def get_recipe(selected_category, user_goal):
    valid_choice = False
    pretty_menu = "************************************************"
    while not valid_choice:
        print(pretty_menu)
        kv_tracker = {}
        menu_number = 1
        for items in Path(selected_category).glob("**/*.txt"):
            kv_tracker[menu_number] = items
            print("{}: {}".format(menu_number, path.basename(items.stem)))
            menu_number += 1
        user_recipe_choice = int(input(f"Please select a recipe to {user_goal}: "))
        if user_recipe_choice in range(1,menu_number):
            set_user_recipe = kv_tracker.get(user_recipe_choice)
            system("cls")
            return(set_user_recipe)
        else:
            print(f"The number: {user_recipe_choice} is not a valid choice")
            print(pretty_menu)
            input("Press enter to make another choice")
            system("cls")

def read_recipe(working_directory):
    pretty_menu = "************************************************"
    user_goal = "read"
    selected_category = get_categories(working_directory, user_goal)
    #Need selected catergory first
    selected_recipe = get_recipe(selected_category, user_goal)
    print(pretty_menu)
    print(f"The {selected_recipe.stem} recipe is: ")
    print(selected_recipe.read_text())
    print(pretty_menu)
    input("Please press enter when you have finished reviewing the recipe")
    system("cls")

def create_new_recipe(working_directory):
    pretty_menu = "************************************************"
    user_goal = "create"
    selected_category = get_categories(working_directory, user_goal)
    valid_recipe = False
    while not valid_recipe:
        print(pretty_menu)
        print(f"You are creating a new recipe for the {os.path.basename(selected_category)} category")
        new_recipe_name = (input("Please enter a new recipe name: ") + ".txt").capitalize()
        full_path = selected_category/new_recipe_name
        if full_path.exists():
            print("The recipe name already exists in this category")
            input("Press 'Enter' to use a different name")
            system("cls")
        else:
            valid_recipe = True
            new_recipe_data = input("Please input the recipe and press 'Enter' when finished: \n")
            with open(full_path, 'w') as new_recipe:
                new_recipe.write(new_recipe_data)                
    input("Update complete, please press 'enter' to go back to the main menu")
    system("cls")

def call_functions(user_menu_choice, working_directory):
    # this is a function to call functions
    # if_else ladder  (for non 3.10 python systems)
    if user_menu_choice == 1:
        read_recipe(working_directory)
    elif user_menu_choice == 2:
       create_new_recipe(working_directory)
    elif user_menu_choice == 3:
        print("three")
        time.sleep(2)
    elif user_menu_choice == 4:
        print("four")
        time.sleep(2)
    elif user_menu_choice == 5:
        print("five")
        time.sleep(2)
    else:
        print("You selected 'Exit the program', Ending the program")

# MAIN
# Set user's name and working directory.
user_name, working_directory = initializing_info()
user_menu_choice = 0

while user_menu_choice != 6:
    user_menu_choice = display_menu(user_name, working_directory)
    function_caller = call_functions(user_menu_choice, working_directory)

### this is a work in progress
