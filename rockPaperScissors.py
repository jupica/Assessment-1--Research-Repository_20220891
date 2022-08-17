import random 
#create a random number stored in a variable "random_number"
random_number = random.randint(0,4)

#declare variables
computer_pick = ''
user_pick = ''

#Select Computers Choice Based On The Random Number Generated, and assign the value to "computer_pick"
if random_number == 0:
    computer_pick = 'rock'
elif random_number == 1:
    computer_pick = 'paper'
elif random_number == 2:
    computer_pick = 'scissors'
elif random_number == 3:
    computer_pick = 'lizard'
elif random_number == 4:
    computer_pick = 'spock'

# set up while loop for valid input. runs while "user_pick" is NOT rock paper scissors... etc
while (user_pick != 'rock' and 
       user_pick != 'paper' and 
       user_pick != 'scissors' and 
       user_pick != 'lizard' and 
       user_pick != 'spock'):
    #Asks user for input, then makes the input lowercase, and assigns it to the variable "user_pick"
  user_pick = input('rock, paper, scissors, lizard or spock? ').lower()

#If Statement to check if the variables "computer_pick" and "user_pick" contain the same value
if computer_pick == user_pick:
    #If the conditions are met, the following print statement will be displayed in the console, showing the option chosen by both computer and user
    print('Tie! Both chose ' + computer_pick + '.')
#If the above statement is NOT true, check if the computer wins by comparing the value of "computer_pick" and "user_pick"
elif ((computer_pick == 'scissors' and user_pick == 'paper') or 
      (computer_pick == 'paper' and user_pick == 'rock') or 
      (computer_pick == 'rock' and user_pick == 'lizard') or
      (computer_pick == 'lizard' and user_pick == 'spock') or
      (computer_pick == 'spock' and user_pick == 'scissors') or
      (computer_pick == 'scissors' and user_pick == 'lizard') or
      (computer_pick == 'lizard' and user_pick == 'paper') or
      (computer_pick == 'paper' and user_pick == 'spock') or
      (computer_pick == 'spock' and user_pick == 'rock') or
      (computer_pick == 'rock' and user_pick == 'scissors')):
    #Output message into console saying the computer won, and telling the user the options the computer and user picked
  print('You lose! Computer chose ' + computer_pick + ', and you chose ' + user_pick + '.')

#If the above statements are not true, the user must have won
else:
    #Prints message to console telling the user that they won, and displays the choices picked by user and computer
  print('You win! Computer chose ' + computer_pick + ', and you chose ' + user_pick + '.') 
