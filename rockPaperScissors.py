import random 
#create random number
random_number = random.randint(0,4)

#declare variables
computer_pick = ''
user_pick = ''

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
while (user_pick != 'rock' and 
       user_pick != 'paper' and 
       user_pick != 'scissors' and 
       user_pick != 'lizard' and 
       user_pick != 'spock'):
    #Make user input lowercase
  user_pick = input('rock, paper, scissors, lizard or spock? ').lower()

#if user and computer choose the same choice
if computer_pick == user_pick:
    print('Tie! Both chose ' + computer_pick + '.')
#if computer wins
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
    #print message with the users and computers choice
  print('You lose! Computer chose ' + computer_pick + ', and you chose ' + user_pick + '.')

#if player wins
else:
    #print message with the users and computers choice
  print('You win! Computer chose ' + computer_pick + ', and you chose ' + user_pick + '.') 
