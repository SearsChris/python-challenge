
import os
import csv
# define variables

bankcsv = os.path.join('Resources/Budgetdata.csv')
month_count = 0
#monthlyprofit = 0
netprofit = 0
firsttime = True
change_total = 0

with open(bankcsv) as csvfile:
    
    BankData = csv.reader(csvfile, delimiter=",")
    csv_header = next(BankData)
    line_count = 0
    

    for row in BankData:
        
        # Counts the number of months (aka lines)
        month_count = month_count + 1

        #Sum of Row 1 (Profit/Loss)
        netprofit = float(row[1])

        #Avg P/L
        if not firsttime:
            profit_change = int(row[1]) - previous_month
            change_total = change_total + profit_change
        
        firsttime = False
        previous_month = int(row[1])

    avgchange = change_total/(month_count - 1)

        #Storing the difference between the month ahead and current month
        #print('monthlydiff', monthlydiff)
        #print('prevmonth', prevmonth)
        #Calculating avg changes in Profit/Losses
    #formatting
    netprofit = "${:,.2f}".format(netprofit)
    avgchange = "${:,.2f}".format(avgchange)

    #Printing results
    print('Total Months:', month_count)
    print('Total Net Profit:',netprofit)
    print('Average Change:', avgchange)