
import os
import csv
# define variables

bankcsv = os.path.join('Resources/Budgetdata.csv')
month_count = 0
#monthlyprofit = 0
netprofit = 0

with open(bankcsv) as csvfile:
    
    BankData = csv.reader(csvfile, delimiter=",")
    csv_header = next(BankData)
    line_count = 0
    

    for row in BankData:
        
        # Counts the number of months (aka lines)
        month_count = month_count + 1

        #Sum of Row 1 (Profit/Loss)
        netprofit = float(row[1])

        #previous month established
        prevmonth = int(row[1])
        
        #Storing the difference between the month ahead and current month
        monthlydiff = int(row[1]) - prevmonth
        print('monthlydiff', monthlydiff)
        print('prevmonth', prevmonth)
        #Calculating avg changes in Profit/Losses
    avgchange = monthlydiff/month_count
    prevmonth = int(row[1])
    #formatting
    netprofit = "${:,.2f}".format(netprofit)
    avgchange = "${:,.2f}".format(avgchange)

    #Printing results
    print('Total Months:', month_count)
    print('Total Net Profit:',netprofit)
    print('Average Change:', avgchange)