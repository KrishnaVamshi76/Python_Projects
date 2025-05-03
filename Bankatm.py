print("Welcome to Krishna's bank")
bank_balance=eval(input("Please enter you bank balance\n"))
withdraw_amount=eval(input("Enter the amount to withdraw from ATM\n"))

if withdraw_amount>bank_balance:
    print("The amount can't be withdrawn \n as you have insufficient balance")
if withdraw_amount<=bank_balance:
    if withdraw_amount % 500==0:
        print("The number of notes you will get is:",int(withdraw_amount/500))
        bank_balance_after=(int(bank_balance-withdraw_amount))
        print("The Balance amount after withdrawl is:",bank_balance_after)
    else:
        print("Entered amount is not in multiples of Rs.500")