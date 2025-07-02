'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination.
'''


def main():
    
    amount_due = 50
    
    
    
    #Keep looping until the full amount is paid.
    while amount_due > 0:
        
        #Show how much money is still owed.
        print(f"Amount Due: {amount_due}")
        
        coins = int(input("Insert Coin: "))
        
        if coins in [25,10,5]: #Only accept valid coins: 25, 10, or 5.
            
            amount_due -= coins #Subtract the value of the coin from the remaining amount.

    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")
    #Once paid (or overpaid), display the change owed using abs() in case it's negative.
        
main()