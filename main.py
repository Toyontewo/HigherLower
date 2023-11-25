import random
from data import data
from art import vs
score = 0


def format_data(account):
    """ Takes the account data and returns a printable format """
    account_name = account["name"]
    account_decs = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_decs} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """TAKE THE USER GUESS AND FOLLOWER COUNTS AND RETURNS IF THEY GOT IT RIGHT."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
account_b = random.choice(data)

game_continue = True
# Make the game repeatable
while game_continue:
    # Generate random accounts from the game data

    # Making the account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess

    guess = input("Who has more followers? 'A' or 'B'?: ").lower()
    # Check if user is correct

    # # Get follower count of each account

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # # Use if statement to check if the user is correct
    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}")
    else:
        game_continue = False
        print(f"Sorry, That's wrong. Final score is {score}")
# Give user feedback on their guess

# Score keeping


# Clear the screen between rounds
