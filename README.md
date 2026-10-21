# CS2-GABE-Liam-Miguel

# Travel Fare Calculator

## Description
A Python program that calculates the total travel fare based on the distance traveled and the number of passengers, using a fixed rate of PHP 14 per kilometer per passenger.

## Version 1 - Original Code Without Input Validation

  * Input: Requests the passenger's name, travel distance in kilometers, and number of passengers.

  * Process: Multiplies the distance by the fare rate and the number of passengers.

  * Output: Displays the passenger's name and the total fare in Philippine pesos.

  * Validation: Does not check for invalid inputs.

## Version 2 - Code With Input Validation

  * Input: Requests the passenger's name, travel distance in kilometers, and number of passengers.

  * Process: Checks the inputs for validity before calculating the total fare using distance * FARE_RATE * passengers.

  * Output: Displays the passenger's name and total fare. Error messages appear when invalid inputs are entered.

## Validation Rules:

  * Passenger name: Must not be empty.

  * Distance: Must be a number greater than zero.

  * Number of passengers: Must be a positive whole number.
