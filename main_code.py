import random

# computer choice
computer = random.choice([1,2,3])

my_dict = {
    "stone":1,
    "paper":2,
    "scissor":3
}

print("Instructions:", my_dict)

choice = input("Enter your choice (stone/paper/scissor): ")

you = my_dict[choice]

print("You chose =", you)
print("Computer chose =", computer)

if computer == you:
    print("OHH, It's a Draw 😅")

elif computer == 1 and you == 2:
    print("YEAH!! You Won 😎")

elif computer == 1 and you == 3:
    print("OHH!! You Lose 🥲")

elif computer == 2 and you == 1:
    print("OHH!! You Lose 🥲")

elif computer == 2 and you == 3:
    print("YEAH!! You Won 😎")

elif computer == 3 and you == 1:
    print("YEAH!! You Won 😎")

elif computer == 3 and you == 2:
    print("OHH!! You Lose 🥲")