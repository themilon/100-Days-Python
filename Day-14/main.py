
from art import logo
from art import vs
from game_data import data
import random


# Generate different data
def format_data(account):
    """Format the account data into printable format."""

    account_name = account_a["name"]
    account_description = account_a["description"]
    account_country = account_a["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print("Welcome to Higher and Lower Game")
# Display art
print(logo)

score = 0
game_should_continue = True
while game_should_continue:
    # Generate a random account from game data
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        """regenerated data"""
        account_b = random.choice(data)

    # Format the account data into printable format.
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess.

    guess = input("Who has more followers? Type 'A' or 'B' :").lower()

    # Check if user is correct.
    # Get follower count of each account.

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # Use if statement  to check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.

    if is_correct:
        score += 1
        print(f"You're Right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
# Score keeping

# Make the repeatable

# Making account at position B become the next account at position A

# Clear the screen between rounds

#
