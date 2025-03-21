
print("Welcome to the Quizy")
playing = input("Do you want to play the quiz? ")

# Asking the player to play the Quiz
if playing.lower() == "yes":
    print("Let's play the quiz!")
else:
    print("The game is over!")
    exit()

score = 0

# Question 1
answer = input("What does GPU stand for? ")
if answer.strip().lower() == "graphics processing unit": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")

# Question 2
answer = input("What is the highest peak in the world? ")
if answer.strip().lower() == "mount everest": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")

# Question 3
answer = input("What does WiFi stand for? ")
if answer.strip().lower() == "wireless fidelity": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")

# Question 4
answer = input("What does ALU stand for? ")
if answer.strip().lower() == "arithmetic logic unit": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")

# Question 5
answer = input("What is the shape of an egg? ")
if answer.strip().lower() == "oval": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")

# Question 6
answer = input("Which is the longest river in the world? ")
if answer.strip().lower() == "nile": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")

# Qsn 7
answer = input("Which is the largest landlock country in the world? ")
if answer.strip().lower() == "kazakhstan": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")

# Qsn 8
answer = input("What is the another name for skull ? ")
if answer.strip().lower() == "cranial": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")

# Qsn 9
answer = input("Which country is known as sick man of europe? ")
if answer.strip().lower() == "turkey": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")

# Qsn 10
answer = input("What is the recent name of Twitter(x)? ")
if answer.strip().lower() == "Harry potter": 
    print("That's correct!")
    score += 1
else:
    print("SORRY WRONG ANSWER!")


# Final score
print("You got " + str(score) + " correct out of 10.")
print("You got " + str((score / 10) * 100) + "% correct.")