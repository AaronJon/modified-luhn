# Proposed Modified Luhn Algorithm

The main change in the modified Luhn method is the substitution of modulo (5) for modulo (10) in the computations, and the doubling of digits is changed to multiplication by 5. This change was made in order to strengthen the algorithm's security and make it harder for potential fraudsters to get around it. Since the use of modulo (5) allows for more distinct combinations than modulo (10), this alteration also expands the range of potential card numbers (10). As a result, this adjustment improves the algorithm's general efficiency and efficacy.


## The difference

There are a few significant distinctions between the modified Luhn algorithm and the normal approach to consider:
* The mathematical computations needed to determine a card number's validity are different in the new method, to start. 
* The improved technique multiplies every other digit by 5 rather than doubling every other digit and adding the digits of the resultant integers. 
* Additionally, the improved technique switches from using modulo 10 to modulo 5 instead.

The fundamental Luhn algorithm is used by a wide range of industries, including banks, telephones, and credit card companies. It is also used in many government-issued identification cards, including social security numbers. On the other hand, the educational system largely will make use of the modified Luhn algorithm. It is intended to stop the creation of fake certificates by providing distinctive identification numbers and storing certificates on smart cards. The original Luhn algorithm has wider use, but the modified Luhn technique will be used in a specific sector.

## The Implementation

The modified Luhn algorithm is used to verify a given card's identification number, using a modified checksum formula. The parameter number is a sequence of digits, the element at index zero represents the left-most digit, and the right-most digit is the last element in the array. The method is Valid and should return the String "VALID" if the array number represents a valid sequence according to the algorithm, and "INVALID" if the sequence is not valid.

The algorithm verifies the card by following these steps:

    Step 1: Adding the value of each second digit to the total, starting with the rightmost digit.

    Step 2: If combining the numbers yields a two-digit number higher than 9, add the product's digits (for instance, 12: 1 + 2 = 3, 15: 1 + 5 = 6), to obtain a single-digit number.

    Step 3: Before doing the card number verification, prefix it with "419."

    Step 4: Next, calculate the total number of digits.

    Step 5: The number is valid according to the Modified Luhn method if the total modulo 5 equals 0 (if the total ends in zero); otherwise, the number is invalid.
