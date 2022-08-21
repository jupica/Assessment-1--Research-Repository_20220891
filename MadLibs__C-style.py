"""Python Mad Libs"""
"""Mad Libs require a short story with blank spaces (asking for different types of words). Words from the player will fill in those blanks."""

# prints "Here we go!" into console
print("Here we go!")
# prints an empty message into console, resulting in a break, for readability reasons
print()

# Input prompts ask the user to fill in some questions, saving the users input in seperate variables for each question
name = input("Enter a name: ")
adjective1 = input("Write an adjective: ")
adjective2 = input("One more, please: ")
adjective3 = input("And the last one: ")
verb = input("Input a verb: ")
noun1 = input("and a noun: ")
noun2 = input("and one more noun, please: ")
# prints an empty message into console, resulting in a break, for readability reasons
print()

# prints a message to the console prompting the user to continue
print("This is where the story can get really fun!")
# prints a message to the console, reminding the user what to do
print("Input one of each of the following, please")

# prints an empty message into console, resulting in a break, for readability reasons
print()
# displays prompts asking them to continue inputing values for each input prompt, and stores the users input in seperate variables
animal = input("An animal: ")
food = input("A food: ")
fruit = input("A fruit: ")
superhero = input("A superhero: ")
country = input("A country: ")
dessert = input("A dessert: ")
year = input("A year: ")

# defines the variable "STORY", which will be printed out. Each "%s" will be replaced with the value of a variable defined by the users input above
STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

# prints an empty message into console, resulting in a break, for readability reasons
print()
# prints the "STORY", replacing the first "%s" with the value of the variable "name", the second "%s" with the value for "adjective1", etc
print(STORY % (name, adjective1, adjective2, animal, food, verb, noun1, fruit, adjective3, name, superhero, name, country, name, dessert, name, year, noun2))
