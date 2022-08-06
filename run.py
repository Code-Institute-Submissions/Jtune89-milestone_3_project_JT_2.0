import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Quiz Results')


# Welcome message to Quiz
print("Welcome to the most AMAZING quiz that ever was or will be \n")

#user_information
input ("What is your name? \nName: ")
print ("\nWelcome (name) & good luck!  Lets start with question 1:")
score = 0

# QUESTION 1
question1 = input ("\n What is the capital of India? \n a. New Delhi \n b. Mumbai \n c. Jaipur \n d. Kolkata \n Answer: ")
if question1 == "a" or question1 == "New Delhi" or question1 == "A" or question1 == "new delhi":
    score += 1
    print ("\nCorrect! Someone is very clever!!")
    print ("Score:", score)
    print ("\n")
else:
    print ("\nIncorrect! The answer is New Delhi, you silly moo!")
    print ("Score: ", score)
    print ("\n")

# QUESTION 2
question2 = input ("\n Where on the human body is the occipital lobe? \n a. Eyes \n b. Heart \n c. Brain \n d. Foot \n Answer: ")
if question2 == "c" or question2 == "Brain" or question2 == "C" or question2 == "brain":
    score += 1
    print ("\nCorrect! You should be a doctor (or are you already?)!!")
    print ("Score:", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Brain, open a book you silly sausage!")
    print ("Score: ", score)
    print ("\n")

# QUESTION 3
question3 = input ("\n Where in the world would you find Chichen-Itza? \n a. USA \n b. Mexico \n c. Argentina \n d. Honduras \n Answer: ")
if question3 == "b" or question3 == "Mexico" or question3 == "B" or question3 == "mexico":
    score += 1
    print ("\nCorrect! You snazzy globetrotter!!")
    print ("Score:", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Mexico, go do some travelling!")
    print ("Score: ", score)
    print ("\n")
