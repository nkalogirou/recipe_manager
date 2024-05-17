# Assignment: Recipe Manager Application

## Objective:
Develop a Python program that allows users to manage their cooking recipes. The application should enable users to add new recipes, view all recipes, search for recipes by ingredient or name, and categorize recipes.

The purpose is to encourage you to think about how data can be organized, manipulated, and retrieved in a way that is useful and user-friendly.

## Requirements:
1. **Recipe Entry:**
   - Each recipe should be represented as a dictionary containing details such as name, list of ingredients, category (e.g., Dessert, Main Course, Appetizer), and cooking instructions.
   - Users can add new recipes through the console, specifying all necessary details (Provided).

2. **Viewing Recipes:**
   - Implement a feature to display a list of all recipes, including their names, categories, ingredients and cooking instructions.

3. **Searching:**
   - Allow users to search for recipes by name or ingredient. The search should be flexible, returning results that contain the search term within the recipe name or ingredient list.

4. **Categorization:**
   - Users should be able to view recipes by category. Implement a feature to filter recipes based on their assigned category.

5. **Data Persistence (Optional Advanced Feature):**
   - Implement a way to save and load the recipe data using a CSV file. This will allow the recipe collection to persist between program executions.

## Deliverables:
- Source code submitted as a `.py` file.
- Source code Documentation.
  - See how to [document python code](https://realpython.com/documenting-python-code/) in the following sections:
    - Package and Module Docstrings
    - Script Docstrings

## Usage
### Adding, listing and searching a recipe
```sh
$ python recipe_manager.py

Recipe Manager
1. Add Recipe
2. List Recipes
3. Search by Ingredient
4. Exit
Enter choice: 1
Enter recipe name: Chocolate Chip Cookies
Enter ingredients (comma-separated): flour,sugar,butter,chocolate chips,eggs,vanilla extract,baking soda,salt
Enter category: Dessert
Enter instructions: Preheat oven to 350°F (175°C). In a large bowl, cream together the butter and sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water, add to batter along with salt. Stir in flour and chocolate chips. Drop by large spoonfuls onto ungreased pans. Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.
```

Following the runtime of the previous example, *choice 2* allows us to list the available recipes.
```sh
Recipe Manager
1. Add Recipe
2. List Recipes
3. Search by Ingredient
4. Exit
Enter choice: 2
1. Chocolate Chip Cookies (Dessert)
Ingredients: ['flour', 'sugar', 'butter', 'chocolate chips', 'eggs', 'vanilla extract', 'baking soda', 'salt']
Instructions: Preheat oven to 350°F (175°C). In a large bowl, cream together the butter and sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water, add to batter along with salt. Stir in flour and chocolate chips. Drop by large spoonfuls onto ungreased pans. Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.
```

Selecting *option 3* allows us to search via ingredients. In the first example below, the output of a successful search is shown. 
```sh
Recipe Manager
1. Add Recipe
2. List Recipes
3. Search by Ingredient
4. Exit
Enter choice: 3    
Enter ingredient to search for: sugar
Recipes containing sugar:
- Chocolate Chip Cookies
```

If the ingredient does not exist in any of the added recipes the output looks as follows:
```sh
Recipe Manager
1. Add Recipe
2. List Recipes
3. Search by Ingredient
4. Exit
Enter choice: 3
Enter ingredient to search for: jasmine
No recipes found with that ingredient.
```

### Listing and Searching from an empty manager
```sh
$ python recipe_manager.py
Recipe Manager
1. Add Recipe
2. List Recipes
3. Search by Ingredient
4. Exit
Enter choice: 2
No recipes added yet.
```

```sh
$ python recipe_manager.py
Recipe Manager
1. Add Recipe
2. List Recipes
3. Search by Ingredient
4. Exit
Enter choice: 3
Enter ingredient to search for: flour
No recipes found with that ingredient.
```

## Evaluation Criteria:
- **Functionality (60%):** The application meets the specified requirements, with all features implemented and working correctly.
- **Code Quality (20%):** The code is well-organized, commented, and adheres to Python best practices. Proper use of functions is expected.
- **Documentation (10%):** The submitted documentation is clear, thorough, and reflects the application's workings and your development process.
- **Data Structure Usage (5%):** Effective use of appropriate data structures to store and manage recipes.
- **Error Handling (5%):** The program anticipates and gracefully handles potential errors, such as invalid input.
- **Optional Advanced Feature (Bonus 15%)**

## Submission Guidelines:
- Submit this repository as a compressed file through via BlackBoard.
  - Rename the repository as follows: `<Name>_<Surname>_<StudentID>_recipe_manager.tar`
   e.g., `Chris_Stylianou_s1234567_recipe_manager.tar`, assuming I am compressing using tarfile compression method. `zip` and other compression methods also acceptable.
   
## Due Date:
- Submission: 13 May 2024, 6pm

## Additional Notes:
- Working in pairs (or teams of up to 4 people) is highly encouraged. 
- For pairs and groups, the *Optional Advanced Feature* is **required**, and counts within the 60% of *Functionality*! 
- Even if working in pairs/groups, individual submissions are required.
- You are encouraged to test your application thoroughly and handle edge cases (e.g., empty inputs, incorrect data formats).
