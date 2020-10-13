
import os
import csv
# define variables

bankcsv = os.path.join('Resources/Budgetdata.csv')
month_count = 0
netprofit = 0
firsttime = True
change_total = 0
greatest_decrease = 0
greatest_increase = 0
profit_change = 0
greatest_month_inc = ()
greatest_month_dec = ()
with open(bankcsv) as csvfile:
    
    BankData = csv.reader(csvfile, delimiter=",")
    csv_header = next(BankData)
    

    for row in BankData:
        
        # Counts the number of months (aka lines)
        month_count = month_count + 1

        #Sum of Row 1 (Profit/Loss)
        netprofit = float(row[1])

        #Avg P/L
        if not firsttime:
            profit_change = int(row[1]) - previous_month
            #Storing the difference between the month ahead and current month
            change_total = change_total + profit_change
        #Greatest Increase in Profits
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            greatest_month_inc = row[0]
        #Greatest Decrease in Profits
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_month_dec = row[0]
        #Turning off "firsttime" boolean
        firsttime = False
        #storing previous month
        previous_month = int(row[1])
        
    #Calculating avg changes in Profit/Losses
    avgchange = change_total/(month_count - 1)

    #If current change is greater than previous change then greater change = curren
   
   

    #formatting
    netprofit = "${:,.2f}".format(netprofit)
    avgchange = "${:,.2f}".format(avgchange)
    greatest_increase = "${:,.2f}".format(greatest_increase)
    greatest_decrease = "${:,.2f}".format(greatest_decrease)

    #Printing results
    print('Total Months:', month_count)
    print('Total Net Profit:',netprofit)
    print('Average Change:', avgchange)
    print('Greatest Increase:', greatest_increase, greatest_month_inc)
    print('Greatest Decrease:', greatest_decrease, greatest_month_dec)

output_path = os.path.join("Analysis", "PyBank_HW_Output.csv")

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow(['Total Months:', month_count])
    csvwriter.writerow(['Total Net Profit:',    netprofit])
    csvwriter.writerow(['Average Change:', avgchange])
    csvwriter.writerow(['Greatest Monthly Increase:', greatest_increase, greatest_month_inc])
    csvwriter.writerow(['Greatest Monthly Decrease:', greatest_decrease, greatest_month_dec])
