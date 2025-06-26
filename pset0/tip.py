def main():
    #Ask the user how much the meal cost and convert it to a float 
    dollars = dollars_to_float(input('How much was the meal?: ')) 
    #Ask the user how much percentage they want to tip and convert it to a float
    percent = percent_to_float(input('What percentage would you like to tip?: '))
    #Calculate the tip by multiplying the meal cost by the tip percentage
    tip = dollars * percent
    #Print on display the calculated tip amount, formatted to a 2 decimal
    print(f"Leave ${tip: .2f}")


#Function to convert dollars string to float and removing the symbol "$"
def dollars_to_float(d):
    return float(d.replace("$", ""))


#Function to convert the percent str to float and convert int to decimal like "15%" to "0.15" by diving between 100
def percent_to_float(p):
    return float(p.replace("%","")) / 100


#Call de main function to run the program
main()