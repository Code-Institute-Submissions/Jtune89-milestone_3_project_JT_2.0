QUIZ

The quiz is a terminal game, which runs in the CI mock terminal on Heroku

Users are required to answer questions that are put to them with a leaderboard at the end of the quiz to show how they performed against other people.  There are 5 questions in the quiz which are not the usual questions.  The quiz is also a little bit insulting if you get a question wrong but very complementary if you get a question right.

Here is the live version of my project: https://jt-quiz.herokuapp.com/ 

*I cannot get the screenshot of the "Am I responsive" to paste here*

How to play:

Players are asked to enter their name at the start of the quiz, and then they are presented with question 1.  Answering each question then results in the next question appearing until they reach the end of the quiz.

The answers are a, b, c or d.

At the end, they are presented with a leaderboard of players who played before.


Features:
Quiz features a leaderboard of people who have played beforehand.  Questions are always the same regardless of who is playing.
They are advised of the correct answer and insulted if they get it wrong.  They are complemented if they get a question right.

I have built it to accept capitalised A, B, C or D as well as variations of the written wording to avoid them being penalised when getting the right answer.

Testing:
I have run the code through the PEP8 check and some of the lines of code are showing as too long, however there is little I can do about that as the questions and answers are required to be on one line.
Tested manually within the terminal and within the heroku app and the code behaves as expected without any issues

Remaining Bugs:
PEP8 lines too long but does not affect the interaction with the game.

validator testing:
PEP8 online checker, as above

Deployment:
cloned repo
created heroku app
set the buildbacks as required
linked the Heroku app to the repo
clicked on deploy

credits:
how to build a quiz videos on youtube.
code institute love sandwiches walk through

call outs:
I went back and forth on this project and what was the right thing and finally settled on a quiz.