###############################
### living costs in Ontario ###
###############################

costOfRent = "what is the rent of the place you're looking at?   "
avgHydro = 125
hourlyWage = "what is your hourly wage?     "
hoursWorked = "how many hours do you work in one week?   "
costOfInternet = "what is the cost of your internet?    "
phonePlan = "how much do you pay each month for a mobile phone?      "
costOfFood = "how much do you spend on food per month?     "
costOfLuxuries = "how much do you spend on luxuries (i.e. makeup, clothes, video games, electronics, etc)?      "
otherCosts = "put any other costs you factor in (in values).    "

safetyNet = "how much money per month do you want to have left over?      "

def living():
    rent = float(input(costOfRent))
    wage = float(input(hourlyWage))
    hours = int(input(hoursWorked))
    internet = float(input(costOfInternet))
    cell = float(input(phonePlan))
    food = float(input(costOfFood))
    lux = float(input(costOfLuxuries))
    safe = float(input(safetyNet))
    other = float(input(otherCosts))

    totalSalary = hours * wage * 4
    totalCost = rent + internet + cell + food + lux + avgHydro + other

    diff = abs(totalCost - totalSalary)
    safeIncluded = abs(diff - safe)

    finalStatement1 = "this is not a good idea, your total salary is " +  str(totalSalary) + "$, and this is less than your total costs of living, which are " + str(totalCost) + "$. Which means that you will be " + str(diff) + "$ in the hole."
    finalStatement2 = "this is decent, because it still leaves you with enough money to live. Your total salary is " + str(totalSalary) + "$, and your total costs for the month are " + str(totalCost) + "$. Afterwards, you will be left with " + str(diff) + "$"
    finalStatement3 = "your safety net (how much you want left over each month) is either too high, or you need to cut down on spending. Your remaining balance is only " + str(safeIncluded) + "$, which is less than your safety net of " + str(safe) + "$"

    if totalCost > totalSalary:
        return finalStatement1
    
    elif totalCost < totalSalary and safeIncluded > safe:
        return finalStatement2

    elif totalCost < totalSalary and safeIncluded < safe:
        return finalStatement3 

    else: print(ValueError)

x = living()
print(x)

