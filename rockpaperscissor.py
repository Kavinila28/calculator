import random

user_score = 0
comp_score = 0

while True:
    user = input("rock, paper, or scissors ? ").lower()
    comp = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", comp)

    if user == comp:
        print("Tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        comp_score += 1

    print(f"Score - You: {user_score}, Computer: {comp_score}")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
