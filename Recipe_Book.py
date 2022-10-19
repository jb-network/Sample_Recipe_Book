from pathlib import Path

def initializing_info():
  print("Hello and welcome to my test recipe book")
  user_name = input("Please provide your name: ")
  working_directory = Path("C:\SampleRecipeBook\Recipes")

  # This could be updated to accept user provided input for the file location
  print(f"Hello {user_name}, the current recipe book location is set to: {working_directory}")
  print("Please ensure the recipe files included with this script are located there")
  return (user_name, working_directory)

# MAIN
# Set user's name and working directory.
user_name, working_directory = initializing_info()
### this is a work in progress
