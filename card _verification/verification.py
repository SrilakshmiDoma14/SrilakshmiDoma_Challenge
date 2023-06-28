import re

def is_valid_credit_card(card_number):
    # Check if the card number matches the given criteria using regular expressions
    pattern = r"^(4|5|6)\d{3}(-?\d{4}){3}$"
    consecutive_pattern = r"(\d)\1{3}"
    if re.match(pattern, card_number) and not re.search(consecutive_pattern, card_number.replace("-", "")):
        return "Valid"
    else:
        return "Invalid"

# Get the number of credit card numbers
print("How many credit cards you want to validate?")
n = int(input().strip())
credit_cards = []

# Read credit card numbers and store them in a list
print("Enter the credit card numbers, one per line:")
for _ in range(n):
    card_number = input().strip()
    credit_cards.append(card_number)

# Iterate over each credit card number
for card_number in credit_cards:
    result = is_valid_credit_card(card_number)
    print(f"credit card number: {card_number} is {result}")
