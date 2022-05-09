import re

def is_card_number_valid(card_number: str) -> bool:
    """
    Function that validates if the card_number provided is valid via
    the "Luhn algorithm". 
    Based on https://en.wikipedia.org/wiki/Luhn_algorithm
    Args:
        card_number: str | card number to verify
    Returns:
        bool | wheter the card number provided is valid or not
    """
    check_digit = int(card_number[-1])
    results = []
    is_second = True
    # loops in reverse order, from last to first. 
    for i in range(len(card_number) - 2, -1, -1):
        number = int(card_number[i])
        
        if is_second:
            number *= 2

        if number >= 10:
            number = sum(int(digit) for digit in str(number))

        results.append(number)
        is_second = not is_second

    return check_digit == 10 - (sum(results) % 10)


def get_card_type(card_number: str) -> str:
    """
    Function that obtains the credit card type. 
    Args: 
        card_number: str | card number 
    Returns:
        str | card type
    """
    card_regexs = {
        'AMEX': '^3[47][0-9]{13}$',
        'MASTERCARD': '^5[1-5][0-9]{14}$',
        'VISA': '^4[0-9]{12}(?:[0-9]{3})?$'
    }

    for card_type, regex in card_regexs.items():
        r = re.search(regex, card_number)
        if r:
            return card_type
    return 'INVALID'

# Until the user provides a numeric input, it will keep asking for a number
while True:
    card_number = input('Number: ')
    if card_number.isnumeric():
        break

is_valid = is_card_number_valid(card_number)

if is_valid:
    card_type = get_card_type(card_number)
    print(card_type)
else:
    print('INVALID')
    
    