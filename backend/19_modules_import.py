# Hands-on Component: Using math and random Modules

# Let's create a small program that simulates rolling a pair of dice and calculates the sum.

# Step 1: Import the random module.

# Step 2: Define a function called roll_dice that takes no arguments.

# Step 3: Inside roll_dice, use random.randint(1, 6) twice to simulate rolling two six-sided dice. Store the results in variables, say die1 and die2.

# Step 4: Calculate the sum of die1 and die2.

# Step 5: Return the values of die1, die2, and their sum.

# Step 6: Call the roll_dice function and unpack the returned values into three variables: roll1, roll2, and total_sum.

# Step 7: Print the results in a user-friendly format.

# Step 8: (Optional) Use the math module to calculate the probability of rolling a specific sum (e.g., 7) with two dice. The total number of outcomes is 36 (6 faces * 6 faces). The number of ways to roll a 7 is 6 (1+6, 2+5, 3+4, 4+3, 5+2, 6+1). Calculate probability as (favorable outcomes) / (total outcomes).


import random
import math

# Step 2-5: Define the function to roll dice
def roll_dice():
    # Step 3: Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    # Step 4: Calculate the sum
    total_sum = die1 + die2
    # Step 5: Return all values
    return die1, die2, total_sum

# Step 6: Call the function and unpack values
roll1, roll2, total_sum = roll_dice()

# Step 7: Print the results
print(f"You rolled a {roll1} and a {roll2}.")
print(f"Total sum: {total_sum}")

# Step 8: Calculate probability of rolling a 7

# Total possible outcomes when rolling two 6-sided dice
total_outcomes = 6 * 6

# Favorable outcomes for rolling a sum of 7
favorable_outcomes_for_7 = 6 # (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)

# Calculate probability using math.pow for clarity, though not strictly needed here
probability_of_7 = favorable_outcomes_for_7 / total_outcomes

print(f"The theoretical probability of rolling a sum of 7 is: {probability_of_7:.4f}")
print(f"(Which is {favorable_outcomes_for_7}/{total_outcomes})")


