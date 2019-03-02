import sys

#Here we will use branches to seperate a simple "true/flase" scenario.
rentalCode = input('(B)udget, (D)aily, or (W)eekly rental?\n')
if rentalCode == 'B' or rentalCode == 'D':
    rentalPeriod = int(input('Number of Days Rented:\n'))
else:
    rentalPeriod = int(input('Number of Weeks Rented:\n'))
#If "B" or "D" we'll incur a charge in a number of days, if "W", weeks.
##Note conversion of user input to data type "int" to define usage as number.
daysRented = rentalPeriod

budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00	

#Another branch using IF/ELIF, as we move beyond a T/F scenario and now have 3 distinct calculations that could take place.
if rentalCode == 'B':
    baseCharge = daysRented * budget_charge
elif rentalCode == 'D':
    baseCharge = daysRented * daily_charge
elif rentalCode == 'W':
    baseCharge = daysRented * weekly_charge

#Below we'll define the two fields as "input", and format it for the user asking "Starting Odometer Reading:?
##The \n denotes the users input to the field.
odoStart=input("Starting Odometer Reading:\n")
odoEnd=input("Ending Odometer Reading:\n")

#Now we need to convert the odometer figures into "int" format to denote a number usable in calculations.
totalMiles = int(odoEnd) - int(odoStart)

#Using IF branch type for rental code "B"
if rentalCode == 'B':
    mileCharge = 0.25 * totalMiles

#Using IF/ELSE branch type for rental codes "D" and "W" as there are 2 possible scenarios that change output.
if rentalCode == "D":
	averageDayMiles = totalMiles/rentalPeriod
	if averageDayMiles > 100:
		extraMiles = averageDayMiles - 100
	else:
		extraMiles = 0
	mileCharge = extraMiles * 0.25
	
if rentalCode == "W":
	averageWeekMiles = totalMiles/rentalPeriod
	if averageWeekMiles > 900:
		mileCharge = 100 * rentalPeriod
	else:
		mileCharge = 0
	
#Now we'll print the output. We denote the standard text that appears before the output, which is converted to a "str" type.
##Note usage of "{:,.2f}" when printing "Amount Due:" to output a figure returning 2 decimal points. 
amtDue = baseCharge + mileCharge
print('Rental Summary')
print('Rental Code: '+str(rentalCode))
print('Rental Period: '+str(rentalPeriod))
print('Starting Odometer: '+str(odoStart))
print('Ending Odometer: '+str(odoEnd))
print('Miles Driven: '+str(totalMiles))
print('Amount Due: '+'${:,.2f}'.format(amtDue))