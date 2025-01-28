import re #email and password validation
import random # to generate random numbers for the guessing game
import time #timer for hard mode in the game

player_data={} #dictionary to temporarily store user's data as long as program still runs

def email_validation(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" #email structure i.e. username@domainname.domainextension
    if not re.match(pattern, email): #re.match checks if the email matches the patetrn with the regular expressions
        print("Invalid email address!Please enter a valid email, e.g. example01@gmail.co.ke")
        return False #returns email is invalid when this function is called during password setting later in the code
    return True #returns email is valid later in the code

def password_validation(password):
    if len(password) < 8: #checks length of the password
        print("Password must be at least 8 characters long.")
        return False
    if not any(char.isupper() for char in password): #checks for uppercase letter in password
        print("Password must contain at least one uppercase letter.")
        return False
    if not any(char.isdigit() for char in password): #checks for any number in password
        print("Password must contain at least one number.")
        return False
    if not any(char in "@#$%&*" for char in password): #checks for any character in password
        print("Password must contain at least one special character (@, #, $, %, &, *).")
        return False
    return True #returns the email is valid when above criterias have been met

def register_player(): #function to register player
    player= input("Enter your username: ")

    if player in player_data: #checks if player name is in the dictionary
        print("Account already exists. Please log in.")
        return
    
    while True:
        password=input("Set your password: ")
        if password_validation(password):
            break

    age= int(input("Enter your age:"))

    while True:
        email=input("Input your email address: ")
        if email_validation(email):
            break

    player_data[player]={
        "password":password,
        "age":age,
        "email":email
    }#adding the players inf to the dictionary
    print("Registration is successful")

def login_player():
    player= input("Enter your username: ")

    if player not in player_data:
        print("Username doesn't exist. Please create an account.")
        return
    
    attempts=3
    while attempts>0:
        password=input("Enter your password: ")
        if password == player_data[player]["password"]:
            print("Welcome"+ " " +player+ " " +"to the Number Guessing Game!")
            return

        attempts -=1
        print(f"Incorrect password! You have {attempts} left.")

        if attempts==0:
            print("Too many failed attempts. You can reset your password.")
        reset_password(player)#call this function to reset password
        
def reset_password(player): #function to reset password
    while True:
        new_password = input("Enter your new password: ")
        if password_validation(new_password):  # Check new password validity
            break
    player_data[player]["password"] = new_password #updates password for the player in the dictionary
    print("Password reset successful!")

def difficulty_selection(): #function used to select the difficulty mode
    my_list = ('Easy', 'Medium', 'Hard')

    user_difficulty_selected=False #User hasn't selected their choice, condition for while loop

    while not user_difficulty_selected: #looping till a VALID SELECTION is made
     for index, x in enumerate(my_list, 1):
      print(f"{index}. {x}")

     choice = int(input("Choose your difficulty mode: "))

     if 1 <= choice <= len(my_list):
      print(f"You selected: {my_list[choice - 1]}")
      user_difficulty_selected= True #User has selected a valid choice out of the three and the condition is true, ending the loop
      return my_list[choice - 1]  # Return the selected difficulty
     else:
      print("Invalid choice. Please select a valid difficulty level.")

def main(): #the main fucntion that runs when the game starts
    print("Welcome to the Number Guessing Game!")

    game_running=True
    difficulty= None #Stores the results after the 'difficulty_selection' function is called and run


    while game_running:
        option= ('Register', 'Login', 'Exit')
        for index, x in enumerate(option, 1):
            print(f"{index} . {x}")

        choice= int(input("Choose and input: "))

        if choice == 1:
            register_player()
            difficulty= difficulty_selection()
            play_game(difficulty) # Passing the difficulty from the choice to the functions that runs the difficulty levels
        elif choice == 2:
            login_player()
            difficulty= difficulty_selection()
            play_game(difficulty)
        elif choice == 3:
            confirm=input("Are you sure you want to exit?Y/N: ")
            if confirm.upper() =="Y":
                game_running= False
                print("You've exited the game.")
            else:
                continue
        else:
            print("You've entered an invalid choice! Please try again")
            continue


def play_game(difficulty):
    score=0 #setting the initial score for the game
    guess= input()

    if difficulty == 'Easy':
        max_trials= float('infinite') #sets infinite attempts
    elif difficulty == 'Medium':
        max_trials= 5
    else:
        max_trials= 3
        time_limit= 30 

    trials=0
    start_time= time.time() #Tracking time taken in easy and medium modes

    if difficulty == "Hard":
        end_time = start_time + time_limit #tracks the TT in the tracked hard mode

        while trials < max_trials:
         secret_number = random.randint(1, 10) #generating random number

         print("Guess the number (1-10): ")
         guess_time = time.time()  # Track how fast user answers
         break

    if difficulty == "Hard" and time.time() > end_time:
     print("Time's up! Game Over.")       #checks if time ran out in hard mode
    
    if guess == secret_number:
            elapsed_time = time.time() - guess_time  # Time taken for this answer
            score += 10
    else:
        print("Wrong guess!")
        score -= 10
        attempts += 1


    if elapsed_time < 5:  # Bonus for quick answers
        score += 5
            
    print("Congratulations! You guessed the number.")
    print(f"Your score is: {score} and time taken is: {guess_time}")
            
            

            # Medium Mode Hint
    if difficulty == "Medium" and trials >= 3:
                print(f"Hint: The number is {'greater' if secret_number > guess else 'less'} than {guess}.")
            
    if trials == max_trials:
                print("Game Over! You've used all attempts.")
    
    # Display total time for Easy & Medium
    if difficulty in ["Easy", "Medium"]:
        total_time = time.time() - start_time
        print(f"Total time taken: {total_time:.2f} seconds")

    print(f"Final Score: {score}")

    
