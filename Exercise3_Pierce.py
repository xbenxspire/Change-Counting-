'''
Date: Sep 5, 2023
@author: Benjamin Pierce
This program is a change counting game.  User will enter the number of coins required to make exactly one dollar.  
If total value of coins entered is equal to one dollar, program will congratulate user for winning.
Otherwise, program will let user know whether the amount entered was more or less than one dollar.
'''
def main():
    countPennies = int(input("Enter the number of pennies:")) #user enters number of pennies
    print(f"The number of pennies you entered is: {countPennies}") #print number of pennies
    moneyPennies = countPennies*0.01 #compute how much number of currency is worth
    print(f"The dollar amount of pennies you entered is: ${moneyPennies:.2f}") #amount in dollars of pennies entered
    
    countNickels = int(input("Enter the number of nickels:")) #user enters number of nickels
    print(f"The number of nickels you entered is: {countNickels}") #print number of nickels
    moneyNickels = countNickels*0.05 #compute how much number of currency is worth
    print(f"The dollar amount of nickels you entered is: ${moneyNickels:.2f}") #amount in dollars of nickels entered

    countDimes = int(input("Enter the number of dimes:")) #user enters number of dimes
    print(f"The number of dimes you entered is: {countDimes}") #print number of dimes
    moneyDimes = countDimes*0.1 #compute how much number of currency is worth
    print(f"The dollar amount of dimes you entered is: ${moneyDimes:.2f}") #amount in dollars of dimes entered

    countQuarters = int(input("Enter the number of quarters:")) #user enters number of quarters
    print(f"The number of quarters you entered is: {countQuarters}") #print number of quarters
    moneyQuarters = countQuarters*0.25 #compute how much number of currency is worth
    print(f"The dollar amount of quarters you entered is: ${moneyQuarters:.2f}") #amount in dollars of quarters entered

    moneyDollar = moneyPennies + moneyNickels + moneyDimes + moneyQuarters  #add all change
    print(f"You have entered ${moneyDollar:.2f} worth in change.") #let user know the sum of change input

    if moneyDollar == 1: #if and elif statements
        print("Congratulations, you input exactly one dollar's worth of change!")
    elif moneyDollar < 0.50:
        print("You are still under one dollar.")
    else:
        print("You are over one dollar.")
        
if __name__ == '__main__':
    main()