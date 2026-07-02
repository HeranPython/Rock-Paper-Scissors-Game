import random

while True:
    a = random.choice(["r","p","s"])
    choice = input("choose(r/p/s): ").lower()
    if choice not in ["r", "p", "s"]:
        print("Please enter only r, p, or s.")
        continue
    print("Computer chose:", a)
    if a == choice:
        print("It's a tie!")
    elif(a == "r" and choice == "p")or \
        (a == "r" and choice == "s")or \
        (a == "p" and choice == "s"):
        print("you won!")
    else:
        print("you lost!")
    again = input("Play again? (y/n): ").lower()
    if again == "n":
        print("Thanks for playing!")
        break
 
        
       
        













        
