# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
# Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what 
# Brandon usually does to calculate his Rental Property ROI.

# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will 
# calculate the Return on Investment(ROI) for a rental property.

# Calculating Numbers on a Rental Property (Four square method):
# First square --> (Income):
#  - rental income = $$$$
#  - laundry = 0
#  - storage shed = 0
#  - miscellanous = 0
#  - duplex (property income)
#  - Total income monthly = $$$$$ (assuming only rental income) --> (+)

# Second square --> (Expenses):
#  - Tax = $$$
#  - insurance = $$$
#  - utilities = 0
#     - electric
#     - water
#     - gas 
# - home owners association = 0
# - lawn/snow = 0
# - vacancy = $$$
# - repairs (similar to cap ex since they are both fixing) = $$$
# - capital expenditures (similar to repairs) = $$$
# - property management = $$$
# - morgage = $$$
# - Total monthly expenses = $$$$$ ---> (-)

# Third square --> (Cash Flow):
# - take income and subtract expenses from it --> (Total monthly cashflow = income - expenses)

# Fourth square --> (Cash on Cash ROI):
# (When you buy a property) 
# - Down payment = $$$$
# - closing costs = $$$$
# - repairs = $$$$
# - miscellanous = 0 
# - Total investment: sum of all 
# Take monthly cash flow * 12 = $$$$$ <-- annual cash flow
# Take annual cash flow / total investment = % <-- cash on cash ROI is a percentage 



class calculate():
    def __init__(self, income, expenses, cash_flow1):
        self.income = income
        self.expenses = expenses
        self.cash_flow1 = cash_flow1

    def income_calc(self):
        rental_income = input("Please enter how much your rental income is: ")
        print(f"This is your monthly income: ${rental_income}")
        return rental_income

    def expenses_calc(self):
        enter_tax = int(input("Please enter your monthly tax amount: "))
        while enter_tax <= 0:
            print("This is not an acceptable amount, please try again")
            enter_tax = int(input("Please enter your monthly tax amount: "))
        print(f'Thank you, your tax amount is ${enter_tax}')

        enter_insurance = input("Please enter how much you pay for insurance monthly: ")
        while int(enter_insurance) <= 0:
            print("This is not an acceptable amount, please try again")
            enter_insurance = int(input("Please enter how much you pay for insurance monthly: "))
        print(f'Thank you, your monthly insurance amount is: ${enter_insurance}')
            
        enter_utilities = int(input("Please enter your monthly utilities amount (including electricity, water, gas): "))
        print(f'Thank you, your monthly utilities amount is: ${enter_utilities}')

        enter_hoa = int(input("Please enter monthly amount for home owners association: "))
        print(f'Thank you, your monthly hoa amount is: ${enter_hoa}')

        enter_lawn = int(input("Please enter monthly payment for lawn repairs: "))
        print(f'Thank you, your monthly lawn repair amount is: ${enter_lawn}')

        enter_vacancy = int(input("Please enter your monthly vacancy amount: "))
        while enter_vacancy <= 0:
            print("This is not an acceptable amount, please try again")
            enter_vacancy = int(input("Please enter your monthly vacancy amount: "))
        print(f'Thank you, your monthly vacancy amount is: ${enter_vacancy}')

        enter_repairs = int(input("Please enter your monthly repairs cost: "))
        while enter_repairs <= 0:
            print("This is not an acceptable amount, please try again")
            enter_repairs = int(input("Please enter your monthly repairs cost: "))
        print(f'Thank you, your monthly repair amount is: ${enter_repairs}')

        enter_capital_expenditures = int(input("Please enter your monthly capital expenditures: "))
        while enter_capital_expenditures <= 0:
            print("This is not an acceptable amount, please try again")
            enter_capital_expenditures = int(input("Please enter your monthly capital expenditures amount: "))
        print(f'Thank you, your monthly capital expenditure amount is: ${enter_capital_expenditures}')
        
        enter_property_management = int(input("Please enter your monthly property management cost: "))
        while enter_property_management <= 0:
            print("This is not an acceptable amount, please try again")
            enter_property_management = int(input("Please enter your monthly property management cost: "))
        print(f'Thank you, your monthly property management amount is: ${enter_property_management}')

        enter_morgage = int(input("Please enter your monthly morgage amount: "))
        while enter_morgage <= 0:
            print("This is not an acceptable amount, please try again")
            enter_morgage = int(input("Please enter your monthly morgage amount: "))
        print(f'Thank you, your monthly morgage amount is: ${enter_morgage}')

        total_monthly_expenses = (int(enter_tax) + int(enter_insurance) + int(enter_utilities) + int(enter_hoa) + int(enter_lawn) + int(enter_vacancy) + int(enter_repairs) + int(enter_capital_expenditures) + int(enter_property_management) + int(enter_morgage))
        print(f'Your total monthly expenses is: ${total_monthly_expenses}')
        return total_monthly_expenses



    def cash_flow(self, rental_income, total_monthly_expenses):
        difference_of_income_expenses = int(rental_income) - int(total_monthly_expenses)
        print(f'This is your monthly cash flow: ${difference_of_income_expenses}')
        return difference_of_income_expenses


    def investments(self, difference_of_income_expenses):
        down_payment = int(input("Please enter how much down payment you put down: "))
        while down_payment <= 0:
            print("This is not an acceptable amount, please try again")
            down_payment = int(input("Please enter how much down payment you put down: "))
        print(f'Thank you, your down payment amount is: ${down_payment}')

        closing_costs = int(input("Please enter amount of closing cost here: "))
        while closing_costs <= 0:
            print("This is not an acceptable amount, please try again")
            closing_costs = int(input("Please enter amount of closing cost here: "))
        print(f'Thank you, your closing costs has been recorded: ${closing_costs}')

        repair = int(input("Please enter amount of repair cost here: "))
        while repair <= 0:
            print("This is not an acceptable amount, please try again")
            repair = int(input("Please enter amount of repair cost here: "))
        print(f'Thank you, your repair amount has been recorded: ${repair}')

        mis = int(input("Please write down how much you pay for miscellanous things: "))
        print(f'This is how much you paid for mis things: ${mis}')

        total_investment = int(down_payment) + int(closing_costs) + int(repair) + int(mis)
        print(f'Your total investment amount is: ${total_investment}')

        annual_die = int(difference_of_income_expenses) * 12
        print(f'This is your annual cash flow: ${annual_die}')

        ROI = (annual_die / total_investment) * 100
        rounding_ROI = round(ROI, 3)
        print(f'Here is your ROI percentage: {rounding_ROI} %')


# Call function
def ROI():
    money = calculate(0, 0, 0)
    x = money.income_calc()
    y = money.expenses_calc()
    z = money.cash_flow(x, y)
    money.investments(z)
ROI()