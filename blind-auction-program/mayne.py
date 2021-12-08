# Note that when i wrote this code, it runs perfectly fine. If you run this code and it doesn't work, i offer the bug to you as a challenge. FIX IT!!
print("This is a blind auction program")
print("You're making a bid for a diamond encrusted human skull")

bids = {}
finished_bidding = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"David": 123, "Kelvin", 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}!")


while not finished_bidding:
    name = input("Type in your name please: ")
    price = int(input("What's your bid price: $"))
    bids[name] = price
    other_bidders = input("Are there other bidders?: Type 'yes' or 'no'.")
    if other_bidders == "no":
        finished_bidding = True
        highest_bidder(bids)
    elif other_bidders == "yes":
        print("")
