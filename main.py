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

safetyNet = "how much money per month do you want to have left over?      "

def living():
    rent = int(input(costOfRent))
    wage = int(input(hourlyWage))
    hours = int(input(hoursWorked))
    internet = int(input(costOfInternet))
    food = int(input(costOfFood))
    lux = int(input(costOfLuxuries))
    safe = int(input(safetyNet))

    totalSalary = hours * wage * 4 + safe
    totalCost = rent + internet + food + lux + avgHydro

    