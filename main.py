######################################################
### living costs in Ontario for a studio apartment ###
######################################################

costOfRent = "what is the rent of the place you're looking at?   "
avgHydro = 125
hourlyWage = "what is your hourly wage?     "
hoursWorked = "how many hours do you work in one week?   "
costOfInternet = "what is the cost of your internet?    "
costOfFood = "how much do you spend on food per month?     "
costOfLuxuries = "how much do you spend on luxuries (i.e. makeup, clothes, video games, electronics, etc)?      "
otherCosts = "put any other costs you factor in (in values).    "

safetyNet = "how much money per month do you want to have left over?      "

def living():
    rent = float(input(costOfRent))
    wage = float(input(hourlyWage))
    hours = int(input(hoursWorked))
    internet = float(input(costOfInternet))
    food = float(input(costOfFood))
    lux = float(input(costOfLuxuries))
    safe = float(input(safetyNet))
    other = float(input(otherCosts))

    totalSalary = hours * wage * 4
    totalCost = rent + internet + food + lux + avgHydro + other + safe

    diff = abs(totalCost - totalSalary)

    finalStatement1 = "this is not a good idea, your total salary is " +  str(totalSalary) + "$, and this is less than your total costs of living, which are " + str(totalCost) + "$. Which means that you will be " + str(diff) + "$ in the hole."
    finalStatement2 = "this is decent, because it still leaves you with enough money to live. Your total salary is " + str(totalSalary) + "$, and your total costs for the month are " + str(totalCost) + "$. Afterwards, you will be left with " + str(diff) + "$"

    if totalCost > totalSalary:
        return finalStatement1
    
    elif totalSalary >= totalCost:
        return finalStatement2

    else: print(ValueError)

x = living()
print(x)