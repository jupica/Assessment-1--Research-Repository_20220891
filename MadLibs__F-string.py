# MADLIBS - MAGIC COMPUTERS

print('\n\nWelcome to MAGIC COMPUTERS madlibs GAME\n')

print("Please enter the following: \n")

noun = input("Noun: ")
plural_noun1 = input("Plural Noun: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
adjective1 = input("Adjective: ")
adjective2 = input("Adjective: ")
plural_noun2 = input("Plural Noun: ")
adjective3 = input("Adjective: ")

print("\nThe madlib after inserting the words you gave: \n")

madlib = f"Today, every student has a computer small enough to fit into his '{noun}'. \
He can solve any math problem by simply pushing the computer's little '{plural_noun1}'. \
Computers can add, multiply, divide and '{verb1}'. They can also '{verb2}' better than a human. \
Some computers are '{adjective1}'. Others have a/an '{adjective2}' screen that shows all kinds \
of '{plural_noun2}' and '{adjective3}' fingers."

print(madlib)
