# Assessment-1---Research-Repository
I am looking at a version of Rock Paper Scissors Lizard Spock I found online made in python (src: https://replit.com/@digitechhub/Rock-paper-scissors-lizard-spock)

The first thing done in the code is creating a random number which later equates to the computers selection.
Then the variables "user_pick" and "computer_pick" are declared and set to empty strings, to allow the value to be defined later.
A while loop is created to ask the user for their input, it will only continue to the next stage if the users input is one of the choices recognised by the code. If the user inputs something else, they will be asked the question again, until they input either "rock", "paper", "scissors", "lizard" or "spock"
The code then checks if the user input == (is the same as) the computers input. If they are the same, the game is tied, and the code outputs "Tie! Both chose " followed by the computers input.
If those conditions aren't met, the code then checks if the computers choice would beat the users choice. If that is the case, the code outputs "You lose! Computer chose (The computers choice), and you chose (Users choice)."
If those conditions are not met, the user has won, so the code outputs "You win! Computer chose (The computers choice), and you chose (Users choice)"
