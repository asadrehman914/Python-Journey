purchase=float(input("Enter Purchase Amount: "))

if purchase >= 50000:
    totaldiscount=10
elif purchase>=30000:
    totaldiscount=8
elif purchase >=15000:
    totaldiscount=5
elif purchase >=10000:
    totaldiscount=3
else:
    print("Minimum Purchase is 10000 for Discount")

print("Total Purchase: ",purchase)
discount=purchase*totaldiscount/100
print("The Discount: " ,discount)
afterdiscount=purchase-discount
print("After Discount: ",afterdiscount)
tax=afterdiscount *5/100
print("Tax",tax)
final_price=afterdiscount+tax
print("Final price after tax and discount:" ,final_price)
