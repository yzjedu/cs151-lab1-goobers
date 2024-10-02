# Programmers:  Laure Patera and John Elehwany
# Course:  CS151, Dr. Yalew
# Due Date: 9/18/24
# Lab Assignment: 01
# Problem Statement: Find the cost of gas for an entire road trip, using user inputs of miles that will be travelled,
# miles per gallon, and cost of gas
# Data In: miles that will be travelled, miles per gallon, and cost of gas
# Data Out: total cost of gas for a trip
# Credits: Problem and instructions used from the README.md file

# The user is asked to input the miles that will be travelled, miles per gallon of their vehicle,
# and the cost per gallon of gas
miles_travelled = int(input('How many miles will you travel?'))
miles_per_gallon = int(input('What is the miles per gallon of your vehicle?'))
gas_cost = int(input('What is the cost of a gallon of gas?'))

# inputs given are calculated to find the total cost of gas for a trip
total_gas_cost = (miles_travelled / miles_per_gallon) * gas_cost

# The total cost of gas for a trip is outputted to the user
print('The total cost of gas for your trip will be:', total_gas_cost)
