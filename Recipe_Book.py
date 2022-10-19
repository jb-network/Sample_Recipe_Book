from pathlib import Path

def initializing_info():
  # This function sets in the intial variables for the program and passes them to main
  print("Hello and welcome to my test recipe book")
  user_name = input("Please provide your name: ")
  working_directory = Path("C:\SampleRecipeBook\Recipes")
  # This could be updated to accept user provided input for the file location
  print(f"Hello {user_name}, the current recipe book location is set to: {working_directory}")
  print("Please ensure the recipe files included with this script are located there")
  return (user_name, working_directory)

def count_recipes(working_directory):
    #This function provides a way to count the total numbers of recipes in the book, this can be called at anytime
    total_recipes = len(list(Path(working_directory).glob("**/*.txt")))
    return total_recipes

# MAIN
# Set user's name and working directory.
user_name, working_directory = initializing_info()
print(f"the total rec: {count_recipes(working_directory)}")
### this is a work in progress
