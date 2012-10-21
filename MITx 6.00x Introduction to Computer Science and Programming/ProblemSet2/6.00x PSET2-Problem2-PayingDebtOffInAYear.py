#Calculate the minimum fixed monthly payment needed to pay ... within 12 months

#annualInterestRate = 0.2
#balance = 4773

payment = 0
updatedBalance = balance
monthlyInterestRate = annualInterestRate/12

while (updatedBalance >= 0):
    updatedBalance = balance
    payment += 10
    for i in range(0, 12):
        updatedBalance = round(((updatedBalance - payment) * (1 + monthlyInterestRate)), 2)
    
    #print ("Balance: " + str(updatedBalance))

print("Lowest Payment: " + str(payment))
