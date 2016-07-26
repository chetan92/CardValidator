# Card-Validator

Card-Validator is a Python 2 or 3 module which can validate, generate and determine the format of  card numbers using the Luhn algorithm.

## Getting Started

To install Card-Validator in your environment you may use pip command:-

    pip install Card-Validator

You may also upgrade to the latest version using :-
    
    pip install --upgrade Card-Validator
    
To import the module add the following to your python file:

#### Luhn (Generator and Validator)
    from cardvalidator import luhn
#### Formatter
    from cardvalidator import formatter

### Validator
The validator can be used to validate  cards and calculate the Luhn check digit for a given number.

#### Validate
To validate a  card number:

    luhn.is_valid(number)

`number` is a string or integer which is the  card number.

To calculate the Luhn check digit for a particular number:

    luhn.calculate_check_digit(number)

Again, `number` is a string or integer. For this method, however, it is a partial  card number. This method will return the check digit, which is the last digit of the card number, as an integer.

### Generator
To generate a valid  card number:

    luhn.generate(length)

This method will return a valid  card number as a string.

### Formatter
To check whether a number matches the format of a specified type of card use the following methods:

    formatter.is_visa(number)

This method will return a boolean value based on the card type match.

To generate the possible card type (s) for given card number :

    formatter.get_format(number)
    
This method will return the list of card types if the card number match with any card format.
    
The following card number formats can be detected:

+ visa
+ visa electron
+ mastercard
+ amex (american express)
+ maestro
+ discover
+ JCB
+ DinersClub
+ CARTEBANCAIRE
+ SOLO
+ UNIONPAY
+ rupay
+ dankort
+ HIPERCARD
+ interpayment
+ LASER
+ Bancontact MisterCash (bcmc)
+ switch
+ VPAY
+ elo
+ korean local card
+ carte blanche
+ bcglobal

A card number can be checked to be in one of these formats by using the method `formatter.is_format(number)`, where format is the format you are checking.

Each of these method will return `True` or `False` depending on whether the given number
`n` matches the format tested. As with the Validator and Generator, `n` can be
either a string or an integer.

To check if the number matches any of the formats you can use the method `formatter.get_format(number)` which will return a list of all the formats that the number complies with. If the number is determined to not be any of the above formats then an empty list will be returned.
