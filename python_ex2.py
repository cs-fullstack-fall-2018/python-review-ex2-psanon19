import os
os.system("clear")

import random
randomNumber = random.randint(0,20)

def main():
    attempts = 0
    while True:
        guess = int(input("\nGuess the number 0-10! "))
        attempts +=1
        if guess!=randomNumber:
            print("\nNumber of Attempts was: ", attempts, "\nAww, try agian...")
            continue
        elif guess==randomNumber:
            print("\nNumber of Attempts was: ", attempts, "\nYou did it!")
            break
        else:
            print("\nYou, uhh...did something unexpected")
            continue

if __name__ == '__main__':
    main()

    # guess = int(input("Guess the number 0-10! "))
    # while guess!=randomNumber:
    #     attempts = 0
    #     guess = int(input("Guess the number 0-10! "))
    #     for attemptCount in range(attempts):
    #         if guess!=randomNumber:
    #             attempts = attemptCount+1
    #             print("\n", attempts, ".","Aww, try agian...")
    #             continue
    #         elif guess==randomNumber:
    #             attempts = attemptCount+1
    #             print("\n", attempts, ".","You did it!")
    #             break
    #         else:
    #             print("\nYou, uhh...did something unexpected")
    #             continue
