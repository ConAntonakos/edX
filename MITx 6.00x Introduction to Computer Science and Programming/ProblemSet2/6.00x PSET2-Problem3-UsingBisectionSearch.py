# MITx: 6.00x
# Problem 3: Using Bisection Search to Make the Program Faster

balance = 999999
annualInterestRate = 0.18

updatedBalance = balance
monthlyInterestRate = (annualInterestRate) / 12
epsilon = 0.01
numGuesses = 0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12
ans = (upperBound + lowerBound)/2.0

while abs(0 - updatedBalance) >= epsilon:
    print('low = ' + str(lowerBound) + ' high = ' + str(upperBound) + ' ans = ' + str(ans))
    updatedBalance = balance
    numGuesses += 1
    for i in range(0, 12):
        updatedBalance = round(((updatedBalance - ans) * (1 + monthlyInterestRate)), 2)
    if  updatedBalance >= 0:
        lowerBound = ans
    else:
        upperBound = ans
    ans = (upperBound + lowerBound)/2.0
print('numGuesses = ' + str(numGuesses))
print("Lowest Payment: " + str(round(ans, 2)))
