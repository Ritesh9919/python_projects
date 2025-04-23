
print("Welcome to the my computer quiz game!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit() 


print("Okay! Let's play!")
score = 0

# Question 1
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Currect!")
    score += 1
else:
    print("Incorrect!")


# Question 2
answer = input("what does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Currect!")
    score += 1
else:
    print("Incorrect!")  



# Question 3
answer = input("what does CSS stand for? ")
if answer.lower() == "cascading stylesheet unit":
    print("Currect!")
    score += 1
else:
    print("Incorrect!")    


print(f"you got {score} questions correct!")
print(f"You got {(score / 3) * 100}%")
print("Thanks for playing")      



