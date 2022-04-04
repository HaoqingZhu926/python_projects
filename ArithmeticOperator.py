purchasePrice = round(float(input("what is the purchase price?")),2)
amountPaid = round(float(input("what is the amount paid?")),2)
taxes = round((purchasePrice * 0.13),2)
totalBill = round((purchasePrice + taxes),2)
change = round((amountPaid - totalBill),2)


myBill= open("billofsale.txt","w")
purchasePrice = str(purchasePrice)
taxes = str(taxes)
totalBill = str(totalBill)
change = str(change)
myBill.write("the purchase price is: " + purchasePrice + "\n" + "the HST is: " + taxes + "\n" + "the total bill is: " + totalBill + "\n" + "the change is: " + change + "\n")
myBill.close()


change = float(change)
fives = str(int(change/5))
toonies = str(int(change%5/2))
loonies = str(int(change%5%2/1))
quarters = str(int(change%5%2%1/0.25))
dimes = str(int(change%5%2%1%0.25/0.1))
nickels = str(int(change%5%2%1%0.25%0.1/0.05))
pennies = str(int(change%5%2%1%0.25%0.1%0.05/0.01))


myChange = open("billofsale.txt","a")
myChange.write("\nthe number of 5 dollar bills are:"+fives+"\nthe number of toonies are:"+toonies+"\nthe number of loonies are:"+loonies+"\nthe number of quarters are:"+quarters+"\nthe number of dimes are:"+dimes+"\nthe number of nickels are:"+nickels+"\nthe number of pennies are:"+pennies)
myChange.close()


myFile = open("billofsale.txt","r")
readFile = myFile.read()
print(readFile)
myFile.close()
