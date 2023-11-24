print("Welcome to my computer quiz!!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play:)")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    score += 1
    print('Correct!')
else:
    print('Incorrect!')
answer = input("What does UPS stand for? ")
if answer.lower() == "uninterruptible power supply":
    score += 1
    print('Correct!')
else:
    print('Incorrect!')
    answer = input("What does IT stand for? ")
if answer.lower() == "information technology":
    score += 1
    print('Correct!')
else:
    print('Incorrect!')
    answer = input("What does ICT stand for? ")
if answer.lower() == "information communication technology":
    score += 1
    print('Correct!')
else:
    print('Incorrect!')
    answer = input("What does STP stand for? ")
if answer.lower() == "shielded twisted pair":
    score += 1
    print('Correct!')
else:
    print('Incorrect!')
    answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    score += 1
    print('Correct!')
else:
    print('Incorrect!')
print("You got " + str(score) + " question(s) correct!")
 
