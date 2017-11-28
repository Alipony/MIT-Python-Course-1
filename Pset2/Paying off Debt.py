balance = 3926
annualInterestRate = 0.2

#guessnum = 0
min = 0
max = balance
paymentRate = round((max+min)/2,2)
tolrance = 0.01
month = 12

def yearsim (balance):
    '''Given positive balance as int
    returns balance at the end of a year'''
    for m in range(month):
        monIntrest = annualInterestRate / 12.0
        monUnpaid = balance - paymentRate
        balance = (monUnpaid + monIntrest * monUnpaid)
    return balance

while abs(yearsim(balance)) >= tolrance:
    #guessnum += 1
    if yearsim(balance) < 0:
        max = paymentRate
    else:
        min = paymentRate
    paymentRate = (max+min)/2
    print(paymentRate)

#print(guessnum)
print("Lowest Payment: " + str(round(paymentRate,2)))