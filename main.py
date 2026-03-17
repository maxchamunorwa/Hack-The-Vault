from random import randint
from datetime import datetime

EASY_LEVEL_TURNS = 15
MEDIUM_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """checks answer against PIN, returns the number of turns remaining"""
    # count correct digits (ignoring position)
    correct_digits = sum(min(user_guess.count(d), actual_answer.count(d)) for d in set(user_guess))

    # count correct positions
    correct_position = 0
    for x in range(len(actual_answer)):
        if user_guess[x] == actual_answer[x]:
            correct_position += 1
    if user_guess == actual_answer:
        print(f" 🔓🔓ACCESS GRANTED ! The PIN is {actual_answer}")
        return turns

    print(f"🧠 Analysis: {correct_digits}/4 digits correct")
    print(f"📍 {correct_position}/4 digits in correct position")

    return turns - 1

# Function to set difficulty
def set_difficulty():
    level = input("Select target security level: 'low' / 'medium' / 'high'\n")
    if level == "low":
        return EASY_LEVEL_TURNS
    elif level ==  "medium":
        return MEDIUM_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Opening introductory remarks
def game():
    #Choosing a random number between 1000 and 9999
    print("🛑 UNAUTHORISED ACCESS DETECTED🛑")
    print("Target: secure Vault system")
    print("Objective: Crack the access code before lockout")
    print("Warning: Too many failed attempts will trigger system lockdown\n")
    print("Please enter the 4 digit pin ")
    answer = str(randint(1000,9999))
    print(f"Pssst, the correct pin is {answer}")

    turns = set_difficulty()

# repeat the function if they get it wrong
    guess = 0
    while guess != answer:
        print(f"⚠️ You have {turns} attempts remaining before system lockdown ⚠️")
        # let the user guess a number
        guess = (input("Please enter the 4 digit pin: "))

        # input validation
        if not guess.isdigit() or len(guess) != 4:
            print("❌ Invalid input. Enter a 4-digit PIN")
            continue # skips the rest of the loop and ask again

        turns = check_answer(guess, answer, turns)
        # Attempt logging
        with open("attempt_log.txt" , "a") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = "SUCCESS" if guess == answer else "FAIL"
            log.write(f"{timestamp} - Attempt: {guess} - {result}\n")
            print(f"Logged: {timestamp} - Attempt: {guess} - {result}")


        if turns == 0:
            print("🚫SYSTEM LOCKED🚫")
            print("🚨 Too many failed attempts. Intrusion detected🚨!")
            return
        elif guess != answer:
            print ("Incorrect, try again!")

#replay feature
while True:
    game()

    play_again = input("Retry hack? (y/n): ").lower()
    if play_again != "y":
        print("Session Terminated.")
        break

