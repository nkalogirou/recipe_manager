# Optional Python Assignment 
#
# Nikos Kalogirou - 20231063
# Rafael Chadjicharalambous - 20221298

# importing the csv
import csv
csv_file_path = "Recipes.csv"

# load recipes function
def load_recipes():
    recipes = [] # making an array of recipes
    try:
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)  # Using DictReader to read rows as dictionaries (used GPT for this one)
            for row in reader:
                recipes.append(row) # Append each row to the recipes list
    except FileNotFoundError:
        pass # If the file is not found, do nothing (recipes list remains empty) (GPT)
    return recipes

# save function to save recipes to the CSV file
def save_recipes(recipes):
    try:
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['name', 'ingredients', 'category', 'instructions']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader() # Write the header row with field names (GPT)
            for recipe in recipes:
                writer.writerow(recipe) # Write each recipe as a row in the CSV file (GPT)
    except IOError:
        print("Error: Could not save recipes to CSV.")

# add function to add new recipes
def add_recipe(recipes, name, ingredients, category, instructions):
    new_recipe = {
        'name': name,
        'ingredients': ingredients,
        'category': category,
        'instructions': instructions
    }
    recipes.append(new_recipe) # Add the new recipe to the recipes list
    save_recipes(recipes) # Save the recipes list in the CSV file
    print("Recipe added successfully.\n")

# function to list all recipes
def list_recipes(recipes):
    if recipes:
        for index in range(len(recipes)):
            # Print each recipe with its ingredients, category and instructions
            print(index+1,":", recipes[index]['name'])
            print("Ingredients: ", recipes[index]['ingredients'])
            print("Category: ", recipes[index]['category'])
            print("Instructions: ", recipes[index]['instructions'])
            print() 
    else:
        print("\nNo recipes yet.")

# function to search for recipes by ingredient
def search_by_ingredient(recipes, ingredient):
    isSearch = False # boolean variable to track if any recipes are found
    print("Searching Recipes containing",ingredient,":")
    for index in range(len(recipes)):
        if ingredient in recipes[index]['ingredients']:
            isSearch = True  # make the boolean true
            print(recipes[index]['name']) # Print the name of recipes containing the ingredient
              
    if isSearch == False:
            print("No recipes found with that ingredient.") 

# function to list recipes by category
def list_category(recipes, category):
    isCategories = False # boolean variable to track if any recipesa are found
    for index in range(len(recipes)):
        if recipes[index]['category'] == category:
            isCategories = True # make the boolean true
            print(recipes[index]['name']) # Print the name of recipes in the category given       
    
    if isCategories == False:
        print("No recipes found in this category.")    

# main function to manage recipe operations
def main():
    recipes = load_recipes() # load existing recipes from the CSV file

    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. List Recipes")
        print("3. Search by Ingredient")
        print("4. List Recipes by Category")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            # Get the recipe's details from user's inputs
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            category = input("Enter category: ")
            instructions = input("Enter instructions: ")
            # Add the new recipe
            add_recipe(recipes, name, ingredients, category, instructions)
        elif choice == "2":
            # List all recipes
            list_recipes(recipes)
        elif choice == "3":
            # Search recipes by ingredient
            ingredient = input("Enter ingredient to search for: ")
            search_by_ingredient(recipes, ingredient)
        elif choice == "4":
            # Search recipes by category
            category = input("Please provide category: ")
            list_category(recipes,category)
        elif choice == "5":
            # Save recipes and exit
            save_recipes(recipes)
            print("Exiting Recipe Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
