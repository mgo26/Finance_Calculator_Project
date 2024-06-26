import math
# project to help people calculate amounts of interest earned or bond to pay

#--Functions--

def investment():
    investment_return = 0
    investment_deposit = int(input("Enter amount being deposited: "))
    investment_interest = int(input("Enter interest rate: "))
    investment_years = int(input("Enter number of years you plan to invest: "))
    
    # user must choose between simple and compound interest
    while True:
        interest_type = input("Please enter whether you would like 'simple' or compound' interest: ")

        if interest_type == "simple":
            investment_return += investment_deposit * (1 + (investment_interest/100 * investment_years))
            print(f"Your investment return will be: {investment_return - investment_deposit}")
            break
        elif interest_type == "compound":
          investment_return += investment_deposit * math.pow((1 + investment_interest/100), investment_years)
          print(f"Your investment return will be: {investment_return - investment_deposit}")
        else:
            print("Error")
            

def bond():
    monthly_repayments = 0
    house_value = int(input("Please enter the current value of the house: "))
    bond_interest = int(input("Please enter the interest rate: "))
    months_to_repay = int(input("Please enter the number of months you intend to pay back your bond in: "))
    monthly_interest = (bond_interest / 100) / 12
    monthly_repayments += ((monthly_interest * house_value)) / (1 - (1 + monthly_interest) ** (-months_to_repay))
    print(f"Your monthly repayments are: {math.ceil(monthly_repayments)}")


def cost_of_living():
    cost_of_living = 0
    weekly_shop = int(input('Please enter the current cost of your weekly shop: '))
    inflation_rate = 1+ (int(input('Please enter the current rate of inflation: ')) / 100)
    new_shop_cost = weekly_shop * inflation_rate
    print(f'Your new weekly shop cost adjusted for inflation is {new_shop_cost}')






#--Main program--

# user inputs whether they have an investment or a bond
print('Please select the calculation you would like to make:\n')
print("Investment\t\tTo calculate the amount of interest you'll earn on your investment")
print("Bond\t\t\tTo calculate the amount you'll have to pay on a home loan")
print('Inflation calculator \tTo calculate the increased cost of your weekly shop')


# user decides on investment or bond
user_choice = input("Enter either 'Investment', 'Bond' or 'Inflation' from the menu above to proceed: ")

# user chooses investment 
if user_choice.lower() == "investment":
    investment()
# user chooses bond       
elif user_choice.lower() == "bond":
   bond()
elif user_choice.lower() == 'inflation':
    cost_of_living()
else:
    print("You have not input either 'investment' or 'bond', please try again.")


