name = input("Type your name: ")
print(f"Hello, {name}! welcome to the adventure game!")


answer = input("You wake up in a dark forest. You can go left or right . Which way do you want to go? (Left/Right)").lower()

if answer == "left":
    answer = input("You came across a river. Do you want swim or walk arount it? (Swin/Walk)").lower()
    if answer == "swim":
        print("You swam across and were eaten by a crocodile.")
    elif answer == "walk":
        print("You walked around and found a treasure chest! You win!")
    else:
        print("Invalid input.")        
elif answer == "right":
    answer = input("You came across a mountain. Do you want to climb it or go around it? (Climb/Go around)").lower()
    if answer == 'climb':
        print("You climbed the mountain and found a beautiful view! You win!")
    elif answer == "go around":
        print("You went around and got lost in the forest. You lose.")
    else:
        print("Invalid input.")        
else:
    print("Invalid input.")   

print(f"Thank you for playing, {name}!")
