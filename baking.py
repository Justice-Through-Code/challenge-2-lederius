
# Let's get cooking!

ingredient_1 = 'milk'
ingredient_2 = 'eggs'
ingredient_3 = 'flour'
ingredient_4 = 'sugar'


def print_ingredients():  # Ways to work with strings/printing
    # Those are the right ingredients, aren't they? Let's print them out a few different ways to check

    # 1.1 Using one print statement, print out the ingredients as 4 separate strings

    # 1.2 Using one print statement, use string concatenation to print the ingredients
    # as a single string (make sure to add a space between each ingredient!)

    # 1.3 Using one print statement, use an f-string to print the ingredients
    # as a single string (make sure to add a space between each ingredient!)


def confirm_ingredients():  # String methods
    # 2.1 Save the f-string you wrote above into a variable called `ingredients`.
    
    # Aha, that's the issue! We need to use butter, not milk.
    # 2.2 In a print statement, use one of the string methods from class to replace 'milk' with 'butter'

    # Hmm, when we use a string method in a print statement, does it change the string in our variable?
    # 2.3 Use a string method to count the number of times that 'milk' appears in our string.

    # 2.4 Let's print out our `ingredients` variable again just to be sure.

    # 'milk' is still in there! To save our changes to the string, we'll need to update the variable.
    # 2.5 Update our `ingredients` variable using the replace method, the same way we printed it out in step 2.2
    
    # 2.6 Print `ingredients` to make sure the change stuck this time.

    # 2.7 That looks better. Let's make it official: use another string method to 
    # print the string in the `ingredients` variable in all-caps now that it's right.


def favorite_bake():  # User Input/Type conversion
    # The beauty of these ingredients is that you can make tons with them. 
    # Let's get some user input to decide what to bake!

    # 3.1 Create a variable called `baked_good`, that saves the user's input to the question:
    # What is your favorite baked good?

    # 3.2 Create a second variable called `frequency` that asks the user:
    # Roughly how many times a month do you eat <baked_good>s? <-- use your `baked_good` variable in an f-string here

    # When the user inputs a number, what data type is it saved as?
    # 3.3 Print out the _type_ of the `frequency` variable to check.

    # 3.4 Uncomment the print statements below, and get them to run WITHOUT changing the content--
    # HINTS: 
    # What's missing from the first print statement to allow us to use a variable inside a string?
    # Use `type conversion` to fix the second one
    
    # print('Ooooh, {baked_good}s are delicious!')
    # print(f'We recommend you eat {baked_good}s at least {frequency * 2} times a month!')
