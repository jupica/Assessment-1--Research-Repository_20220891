# MADLIBS - MAGIC COMPUTERS

# prints message welcoming user to the game, telling the user what the game is.
print('Welcome to MAGIC COMPUTERS madlibs GAME')
# prints message to console giving the user instructions
print("Please enter the following: ")

# Prompts the user to input words following the guidelines, each word is then stored in a seperate variable
noun = input("Noun: ")
plural_noun1 = input("Plural Noun: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
adjective1 = input("Adjective: ")
adjective2 = input("Adjective: ")
plural_noun2 = input("Plural Noun: ")
adjective3 = input("Adjective: ")

# prints message to console
print("The madlib after inserting the words you gave: ")

# defines the "madlib" string variable, placing each variable from above into the sentence.
# the variable is made with an "f-string", a method of concatenation.
madlib = f"Today, every student has a computer small enough to fit into his {noun}. \
He can solve any math problem by simply pushing the computer's little {plural_noun1}. \
Computers can add, multiply, divide and {verb1}. They can also {verb2} better than a human. \
Some computers are {adjective1}. Others have a/an {adjective2} screen that shows all kinds \
of {plural_noun2} and {adjective3} fingers."

# prints the "madlib" variable to the console.
print(madlib)
