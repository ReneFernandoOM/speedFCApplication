# speedFCApplication
Python test for speedFC job application.

## Credit
Implement a program that determines whether a provided credit card number is valid according to Luhn’s algorithm.

## Implementation Details
Write a program that prompts the user for a credit card number and then by using Luhn Algorithm, reports (via print) whether it is a valid American Express, MasterCard, or Visa card number.
So that we can automate some tests of your code, we ask that your program’s last line of output be AMEX and print() or MASTERCARD and print() or VISA and print() or INVALID and print(), nothing more, nothing less.

For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).
Here are a few card numbers that PayPal recommends for testing:
https://developer.paypal.com/docs/classic/payflow/payflow-pro/payflow-pro-testing/#credit-card-numbers-for-testing

Hint: American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers and all American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we won’t concern ourselves with for this problem); and all Visa numbers start with 4.

## Usage
Your program should behave per the example below. Assume that the underlined text is what some user has typed:

    $ python credit.py
    Number: 378282246310005
    AMEX

## Testing
    $ python credit.py
    Number: 3782-822-463-10005
    Number: foo
    Number: 378282246310005
    AMEX

    $ python credit.py
    Number: 6176292929
    INVALID



