from unicodedata import name
from art import logo
print(logo)

print("Welcome to the private bidding auction")

bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
while not bidding_finished:
    name = input("Please enter your name? :")
    price = int(input("Bid amount :$"))
    bids[name] = price

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    else:
        print("Enter another Bid")
