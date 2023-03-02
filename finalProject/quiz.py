# Mantej Lamba
# ITP 116 Final Project
# A quiz that tests your knowledge about USC!

# importing the correct libraries to use
import pathlib
import random
import string
from string import ascii_lowercase
# importing the tomli library to read from the .toml file
import tomli as tomllib

#giving access to the .toml file, stating that it is in the same directory as our quiz.py file
pathQuestions = pathlib.Path(__file__).parent / "questions.toml"

# our main quiz function that creates and runs the quiz
def quiz():
    # creating our questions
    questionsOutput = makeQuestions( pathQuestions, 5 )
    # variable for the number of correct questions
    correct = 0

    # iterating over both the indices and elements of the questionsOutput using enumerate
    for number, quiz in enumerate(questionsOutput, 1):
        # printing the question number
        print("\n" + str(number) + ".")
        # incrementing the number of correct answers
        correct = correct + questions(quiz)

    # congratulations method with the number of correct values
    print("\n Congratulations! You scored " + str(correct) + "/" + str(number) + "!")

# function to pick out correct answer, print question/answer choices, get answer from user, check answer validity
def getAnswer(question, others, hint = None):
    # printing the question
    print(question)
    # combining the letters and other answer options with zip
    others = zip(ascii_lowercase, others)
    # storing the letter/answers in a dictionary
    otherOptions = dict(others)
    # if hint exists (to avoid showing hint on home screen)
    if hint:
        # then we add to other options the hint option to choose from
        otherOptions["e"] = "Hint?"

    # iterating through otherOptions.item()
    for title, alternative in otherOptions.items():
        # printing out the other choices that the user can choose from
        print(title + ") "  + alternative)

    # while loop to validate answers
    while True:
        # getting the answer choice from user
        answer = input("\nChoice? ")
        # splitting the answer to get rid of any extra spaces
        answers = answer.split()

        # handling hints
        if "e" in answer:
            # printing out the hint
            print("\nHINT: " + hint)
            # continuing to prevent our function from ending right here and showing the answer right away
            continue

        # handling invalid answer
        check = answer
        # checking if check is in any of the otherOptions (validating that the user input is a true option)
        if any( check not in otherOptions for check in answers ):
            # if not then we ask the user for another input
            print( check + " is not a valid option. Please choose again."  )
            # continuing to prevent our function from having an invalid answer
            continue

        # iterating through answers
        for answer in answers:
            # returning the user's answer
            return [otherOptions[answer]]

# function to ask user the questions and check answers
def questions(question):
    # getting the right answer for the question
    rightAnswer = question["answers"]
    # getting all the options that the user can choose from
    otherOptions = question["answers"] + question["alternatives"]
    # reordering the answers so they don't appear in the same order every time
    orderedOptions = random.sample(otherOptions, len(otherOptions))
    # getting the final answers user getAnswer of the question to display
    finalAnswers = getAnswer( question["question"], orderedOptions, question.get("hint"))

    # checking if the user had the right annswer
    if (finalAnswers == rightAnswer):
        # if it does then print correct
        print("\nCorrect!!")
    else:
        # if not then show message and display correct answer by accessing the rightAnswer
        print("\nUnfortunately, that’s not right. The answer is: " + str(rightAnswer[0]))

    # printing the explanations for the question
    print("\nExplanation: \n" + question['explanation'])

    # returning 1 or 0 to show the function calling this function whether the answer was right or wrong
    if (finalAnswers == rightAnswer):
        return 1
    else:
        return 0

# function to read the questions and display
def makeQuestions(path, numQ):
    # using loads to read TOML from a text string
    title = tomllib.loads(path.read_text())
    # picking out each topic and storing it in a new temp dictionary
    titleInfo = { questiontitle["label"]: questiontitle["questions"] for questiontitle in title.values() }
    # asking the user what topic they would like to learn about a
    labels = getAnswer("What specific part of USC would you like to learn about?", sorted(titleInfo), )[0]
    # picking out the questions related to the topic
    questions = titleInfo[labels]
    # reordering up the questions to show them in a different order every time
    return random.sample(questions, 5)

# main function
if __name__ == "__main__":
    # welcome message
    print ("Time to test your USC knowledge!\n")
    # calling quiz function
    quiz()