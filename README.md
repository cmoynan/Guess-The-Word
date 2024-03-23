GUESS THE WORD!!!! 

Guess the word is a Python terminal game, which runs in the code institutes mock terminal on Heroku. Users have to try and guess the word that is hidden by guessing a letter. Each time an incorrect guess is logged the user loses an attempt and the user has 6 attempts per word and if they run out of attempts, they lose the round, and it takes away from the final score which is out of 10. 

![image](https://github.com/cmoynan/Guess-The-Word/assets/150179658/259b064c-b15d-43f7-8709-d5d3040bbd1d)

How To Play :

The game begins with an introduction to the game and how it is played. Users are welcomed to the game and provided with the instruction on how to play and they can begin the game right away by guessing a letter. The user is also given the hint that each word is a fruit and how many words there will be in the game. There are lines indicating the length of the word also to also help the users. 

![image](https://github.com/cmoynan/Guess-The-Word/assets/150179658/13c45e40-90cb-47dd-9da2-2defcd601078)

The user then types a letter, and presses return and if the guess is correct the letter will be added to the blank spaces, and they will be prompted to guess again. 

![image](https://github.com/cmoynan/Guess-The-Word/assets/150179658/b1849cf1-cc78-43f4-927e-6eadb7981ef4)

If the user enters an incorrect guess, it tells them the guess is incorrect and also reduces the attempts left. 

![image](https://github.com/cmoynan/Guess-The-Word/assets/150179658/05247f98-1f7d-4906-8966-1db232f076cf)


If the user guesses all the letters correctly it will give them a congratulations message and move onto the next question. 

![image](https://github.com/cmoynan/Guess-The-Word/assets/150179658/10cbf815-7e55-40e4-9540-e6932796a9bd)


 If the user runs out of attempts it will register an incorrect guess and inform the user of what the word was and then move onto the next word. 

![image](https://github.com/cmoynan/Guess-The-Word/assets/150179658/7689c201-5d52-40ca-b772-9a590d1a5c6f)
 
 Once the game is finished it will tell the user how many answers they got correct and end the game .

 ![image](https://github.com/cmoynan/Guess-The-Word/assets/150179658/50687cc9-45fc-4e8d-98a2-6c58cb2aac00)


 Features :

The words are randomised and never repeated in the same game 

Input validation and error checks. If a user put in anything other than a letter or outs in more than 1 letter they will be prompted with an error 

![image](https://github.com/cmoynan/Guess-The-Word/assets/150179658/dfce42c9-5152-430d-bbe4-336a9c3bb4b3)

The game keeps score and when the user finishes the game, they get their score out of 10 

Colorama package added to give the terminal some color to make the game more user friendly and easier on the eye 

Future Features 

Leaderboard 

Amount of time it takes a user to complete the game will be recorded and used for the leaderboard 

Testing :

I have tested this project by doing the following 

Passed the code through Pep8 linter and made sure no errors showed 

![image](https://github.com/cmoynan/Guess-The-Word/assets/150179658/61a55355-5325-4334-914b-b5fc736edd75)


Tested validation by inputting incorrect characters into terminal to make sure validation works and cannot be bypassed 

Tested in my Gitpod terminal and Heroku deployed app 

Bugs:

No option to restart the game once it has finished. I attempted numerous ways of doing this but was either getting syntax errors or the restart function was not working and breaking my code entirely and ended up being too much hassle due to time constraints. The code works when removing other required code.This bug persists but i have left the code in. 

Colorama being added was also not working but is now. Fixed by installing from the terminal rather than importing from my workspace

When running through the CI Python linter I had around 40 errors of whitespace and some lines of code too long. Fixed in the CI python terminal and copied code back from this into my workspace 

 

Deployment:

Created a new Heroku app 

Set the Buildpacks to python and Nodejs in that order 

Added port 8000 to the config vars 

Linked the Github repo to the Heroku app 

https://github.com/cmoynan/Guess-The-Word.git 

Deployed the app by clicking deploy branch in Heroku 

The live app website is https://guesstheword89-bbd1e8207f7c.herokuapp.com/ 
