bill=int((input("Enter the billed Amount:")))
tip=int((input("How much do want to tip, select 10, 12 15 percent:")))
total_amount= float(bill * (tip/100))
print(round(total_amount,2))
split=int(input("between how many members do you want to split"))
total_amount_with_split= (total_amount+bill)/split
print(round(total_amount_with_split,2))