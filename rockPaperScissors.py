import random 
#create random number
random_number = random.randint(0,4)

#declare variables
computer_pick = ''
user_guess = ''

#Select Computers Choice Based On The Random Number Generated
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

# set up while loop for valid input
while (user_guess != 'rock' and 
       user_guess != 'paper' and 
       user_guess != 'scissors' and 
       user_guess != 'lizard' and 
       user_guess != 'spock'):
    #Make user input lowercase
  user_guess = input('rock, paper, scissors, lizard or spock? ').lower()

#if user and computer choose the same choice
if computer_pick == user_guess:
    print('Tie! Both chose ' + computer_pick + ', click run to play again.')
#if computer wins
elif ((computer_pick == 'scissors' and user_guess == 'paper') or 
      (computer_pick == 'paper' and user_guess == 'rock') or 
      (computer_pick == 'rock' and user_guess == 'lizard') or
      (computer_pick == 'lizard' and user_guess == 'spock') or
      (computer_pick == 'spock' and user_guess == 'scissors') or
      (computer_pick == 'scissors' and user_guess == 'lizard') or
      (computer_pick == 'lizard' and user_guess == 'paper') or
      (computer_pick == 'paper' and user_guess == 'spock') or
      (computer_pick == 'spock' and user_guess == 'rock') or
      (computer_pick == 'rock' and user_guess == 'scissors')):
    #print message with the users and computers choice
  print('You lose! Computer chose ' + computer_pick + ', and you chose ' + user_guess + '.')

#if player wins
else:
    #print message with the users and computers choice
  print('You win! Computer chose ' + computer_pick + ', and you chose ' + user_guess + '.') 
