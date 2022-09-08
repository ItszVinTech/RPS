import random
# 1 is rock 2 is paper 3 is scissor

name = input("Enter your name: ")

print(f"Hi {name} lets play a guess rps")

win = True

wins = 0
loss = 0

for i in range(5):
    selected = random.randint(1,3)
    guess = int(input("(1) Rock\n(2) Paper\n(3) Scissor\nYour Choice: "))

    if selected == 1:
        sn = "rock"
    elif selected == 2:
        sn = "paper"
    else:
        sn = "scissor"

    if guess == 1:
        gn = "rock"
    elif guess == 2:
        gn = "paper"
    else:
        gn = "scissor"
    
    if guess == selected:
        print("Draw, Try Again!")
        print("You Picked " + gn + " Computer Picked " + sn)
    if guess == 1 and selected == 2:
        win = False
        print("You Picked " + gn + " Computer Picked " + sn)
    if guess == 1 and selected == 3:
        win = True
        wins = wins + 1
        print("You Picked " + gn + " Computer Picked " + sn)
    if guess == 2 and selected == 1:
        win = True
        wins = wins + 1
        print("You Picked " + gn + " Computer Picked " + sn)
    if guess == 2 and selected == 3:
        win = False
        print("You Picked " + gn + " Computer Picked " + sn)
    if guess == 3 and selected == 1:
        win = False
        print("You Picked " + gn + " Computer Picked " + sn)
    if guess == 3 and selected == 2:
        win = True
        wins = wins + 1
        print("You Picked " + gn + " Computer Picked " + sn)
    print(f"Won {wins}/{i+1} games")
