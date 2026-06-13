print("Welcome to my computer Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! lets play")
score = 0

answer = input("What does cpu stands for? ")
if answer.lower() == "central processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does gpu stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ram stands for? ")
if answer.lower() == "random access memory":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does psu stands for? ")
if answer.lower() == "power supply":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions Correct!")
print(f"You got {score/4 * 100}% ")



