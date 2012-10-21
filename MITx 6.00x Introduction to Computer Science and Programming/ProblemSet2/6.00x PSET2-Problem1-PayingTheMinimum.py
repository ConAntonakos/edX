total_paid = 0

monthlyInterestRate = annualInterestRate/12
    
for i in range(1, 13):
   
        
    minMonthlyPayment = monthlyPaymentRate*balance
        
    interestToPay = (balance - minMonthlyPayment)*monthlyInterestRate
                 
    balance = balance - minMonthlyPayment + interestToPay
        
    total_paid = total_paid + minMonthlyPayment
        
    print ("Month: " + str(i))
    print ("Minimum monthly payment: " + str(round(minMonthlyPayment, 2)))
    print ("Remaining balance: " + str(round(balance, 2)))
print ("Total paid: " +str(round(total_paid, 2)))
print ("Remaining balance: " + str(round(balance, 2)))
           
