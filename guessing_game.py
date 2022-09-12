"""
Project 1 - Number Guessing Game
--------------------------------
"""

def start_game():
    
    import random
    
    from statistics import median, mode, mean
    
    number_of_attempts = []
    high_score = 0
    
    player = input(f"\nWelcome to Kristen's **FANTASTIC** Number Guessing Game!\nWhat is your name?   ")
    
    print(f"\nHi {player}!\n\nIn this game, you will try to guess a random number between 0 and 100. Let's go!\n")
    
    while True:
        solution = random.randint (0,100)
        guess_count = 0
        guess = ""
            
        while guess != solution:
            try:
                guess = int(input(f"What is your guess?  "))
            except ValueError:
                print(f"I'm sorry...we only accept integers. Please try again.")
                continue
            if guess > 100 or guess < 0:
                print(f"Please only enter numbers between 0 and 100.")
            elif guess < solution:
                print(f"It's higher. Try again.")
            elif guess > solution:
                print (f"It's lower. Try again.")
            guess_count += 1
        
        if guess_count == 1:
            print(f"\n****You got it! It took you {guess_count} guess.****")
        else:
            print(f"\n****You got it! It took you {guess_count} guesses.****")  
        
        if high_score == 0:
            high_score = guess_count
        elif guess_count < min(number_of_attempts):
            print(f"-*!*-You've gotten a new high score of {guess_count}!-*!*-")
        else:
            print(f"The high score is {high_score}. Better luck next time!")
        
        number_of_attempts.append(guess_count)  
        
        guess_mean = round(mean(number_of_attempts))
        guess_median = int(median(number_of_attempts))
        guess_mode = mode(number_of_attempts)
        
        print(f"\nHere are your game statistics: \n   Average number of guesses (Mean): {guess_mean} \n   Mid-range score (Median): {guess_median}")
        
        if len(number_of_attempts) != len(set(number_of_attempts)):
            print(f"   Most common score (Mode): {guess_mode}")
        else:
            print(f"   There is no Most Common Answer (Mode).")
        play_again = input(f"\nDo you want to play again? (y/n)   ")
        if play_again.lower() == "n":
            break

    print(f'''Thanks for playing, {player}!''')
    
start_game()
