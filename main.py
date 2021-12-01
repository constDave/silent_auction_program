from replit import clear
from art import logo

print(logo)
print("Welcome to the silent auction.")

continue_bid = True
bids = []
winning_bid = 0

def auction():
  bid = {}
  #call in global or it will reset to 0 every time auction is called
  global winning_bid

  bidders_name = input("What is your name? ")
  bid_amount = int(input("What is your bid? $"))
  bid[bidders_name] = bid_amount
  bids.append(bid)
  
  additional_bidders = input("Are there more bidders? Type 'yes' or 'no'. ").lower()

  if additional_bidders == "yes":
    clear()
    auction()
  else:
    clear()
    #call in continue_bid and set to false to stop the program and print result
    global continue_bid
    continue_bid = False
    for bid in bids:
      for key in bid:
        if bid[key] > winning_bid:
          winning_bid = bid[key]
          winner_name = key
    print(f"The winner is {winner_name} with a bid of ${winning_bid}")

while continue_bid:
  auction()