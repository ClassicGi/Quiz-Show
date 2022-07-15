# Show the Fun Title
print(r"""      _  _  _  _                      _                          _  _  _  _  _  _                                     
    _(_)(_)(_)(_)_                   (_)                        (_)(_)(_)(_)(_)(_)                                    
   (_)          (_) _         _    _  _     _  _  _  _                (_)    _  _      _  _   _  _    _  _  _  _      
   (_)          (_)(_)       (_)  (_)(_)   (_)(_)(_)(_)               (_)   (_)(_)    (_)(_)_(_)(_)  (_)(_)(_)(_)_    
   (_)     _    (_)(_)       (_)     (_)         _ (_)                (_)      (_)   (_)   (_)   (_)(_) _  _  _ (_)   
   (_)    (_) _ (_)(_)       (_)     (_)      _ (_)                   (_)      (_)   (_)   (_)   (_)(_)(_)(_)(_)(_)   
   (_)_  _  _(_) _ (_)_  _  _(_)_  _ (_) _  _(_)  _  _                (_)    _ (_) _ (_)   (_)   (_)(_)_  _  _  _     
     (_)(_)(_)  (_)  (_)(_)(_) (_)(_)(_)(_)(_)(_)(_)(_)               (_)   (_)(_)(_)(_)   (_)   (_)  (_)(_)(_)(_)    
                                                                                                                      
""")

# Display description of how to play the quiz game
print("Welcome to Quiz Time! You will answer a few True or False questions. Please ONLY enter the letter T or F when it's your turn to answer. Have fun!")
print()

# Display Question 1
print("Q1. Electrons move faster than the speed of light.")
print()

# Prompt user to enter T or F
questionOne = input("Please enter 'T' for true or 'F' for false:  ")
print()

# Create a loop if question it is true or not
while questionOne not in "False":
  questionOne = input("Please enter 'T' for true or 'F' for false:  ")
else:
  pass
print()

# Display question 2
print("Q2. Light travels in a straight line.")
print()

# Prompt user to enter T or F
questionTwo = input("Please enter 'T' for true or 'F' for false: ")
print()

# Create a loop if question it is true or not
while questionTwo not in "True":
  questionTwo = input("Please enter 'T' for true or 'F' for false:  ")
else:
  pass
print()

# Display question 3
print("Q3. The Atlantic Ocean is the biggest ocean on Earth.")
print()

# Prompt user to enter T or F
questionThree = input("Please enter 'T' for true or 'F' for false: ")
print()

# Create a loop if question it is true or not
while questionThree not in "False":
  questionThree = input("Please enter 'T' for true or 'F' for false:  ")
else:
  pass
print()

# Display question 4
print("The total length of the Great Wall of China adds up to 13,171 miles.")
print()

# Prompt user to enter T or F
questionFour = input("Please enter 'T' for true or 'F' for false: ")
print()

# Create a loop if question it is true or not
while questionFour in "False":
  questionFour = input("Please enter 'T' for true or 'F' for false:  ")
else:
  pass
print()

# Create the tuples to hold the questions and answers
questions = ('Q1. Electrons move faster than the speed of light.', 'Q2. Light travels in a straight line.', 'Q3. The Atlantic Ocean is the biggest ocean on Earth.', 'Q4. The total length of the Great Wall of China adds up to 13,171 miles.')
answers = ('F', 'T', 'F', 'T')



for index in range(len(questions)):
  print(f"Question {index+1}")
  print(f"index: {index}")
  print(f"Prompt: {questions[index]}")
  print(f"Answer: {answers[index]}")
  print()

# create a variable to keep track of how many questions the user has enter correct
totalQuestions = 4
userAnswer = 0
for answer in answers:
  if userAnswer != answers[1]:
    userAnswer += 1

# Display total number of correct answers
print(f"You got {userAnswer} out of {totalQuestions} correct! Thanks for playing!")
print()