# Assessment-1---Research-Repository
<hr>
I am looking at a version of Rock Paper Scissors Lizard Spock I found online made in python (src: https://replit.com/@digitechhub/Rock-paper-scissors-lizard-spock)

The first thing done in the code is creating a random number which later equates to the computers selection.<br>
Then the variables "user_pick" and "computer_pick" are declared and set to empty strings, to allow the value to be defined later.<br>
A while loop is created to ask the user for their input, it will only continue to the next stage if the users input is one of the choices recognised by the code. If the user inputs something else, they will be asked the question again, until they input either "rock", "paper", "scissors", "lizard" or "spock"<br>
The code then checks if the user input == (is the same as) the computers input. If they are the same, the game is tied, and the code outputs "Tie! Both chose " followed by the computers input.<br>
If those conditions aren't met, the code then checks if the computers choice would beat the users choice. If that is the case, the code outputs "You lose! Computer chose (The computers choice), and you chose (Users choice)."<br>
If those conditions are not met, the user has won, so the code outputs "You win! Computer chose (The computers choice), and you chose (Users choice)"<br>

<hr>

I am also looking at methods of string formating/concatenation<br>
I am comparing F-strings and C-style (%s)

For F-strings, I found a game of "Mad Libs", made in python, which uses F-strings. (src: https://github.com/JoelVStan/madlibs/blob/main/Madlibs-Project/madlibs1.py)

An "F-String" is used to allow the coder to inject the variable into the string using {var name}.<br>
I personally find this method easier to read, as you can see where each variable is being placed into the string.<br>


For C-style (%s), I found another game of "Mad Libs", made in python, which uses C-style. (src: https://replit.com/@pole55/Python-Mad-Libs?v=1#main.py)

In a string, the "%s" is a placeholder for where a variable will be placed into the string later.<br>
At the end of the string, a "%" says what to inject into the placeholders
<hr>


