import art
# TODO-1: Ask the user for input
bidders={}
print(art.logo)
end=0
def winner(bidders):
    bid_of_winner=0
    name_of_winner=""
    for bidder in bidders:
        if bidders[bidder] > bid_of_winner:
            bid_of_winner=bidders[bidder]
            name_of_winner=bidder
        elif bidders[bidder]<bid_of_winner:
            bid_of_winner=bid_of_winner

    print(f"The winner is {name_of_winner} with a bid of ${bid_of_winner}")


while not end:
    name=input("What is your name?: ")
    money=int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bidders[name]=money
    # TODO-3: Whether if new bids need to be added
    new_bidder = str(input("Are there any other bidders? Type 'yes or 'no'.")).lower()
    if new_bidder == "yes":
        print("\n"*20)
        end=0
    elif new_bidder == "no":
        winner(bidders)
        end=1

    # TODO-4: Compare bids in dictionary


