"""
EXP-2: The probability that it is Friday and that a student is absent is 3 %. Since there are 5
school days in a week, the probability that it is Friday is 20 %. What is the probability
that a student is absent given that today is Friday? Apply Baye‟s rule in python to get
the result
"""

# Given probabilities
P_A_and_B = 0.03  # Probability that it is Friday and a student is absent
P_B = 0.20       # Probability that it is Friday

# Apply Bayes' theorem to find P(A|B)
P_A_given_B = P_A_and_B / P_B

print(f"The probability that a student is absent given that today is Friday is {P_A_given_B:.2f}")
    