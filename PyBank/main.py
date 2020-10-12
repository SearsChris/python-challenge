
import os
import csv
# define variables

bankcsv = os.path.join('Resources/Budgetdata.csv')
month_count = 0
monthlyprofit = 0
netprofit = 0

with open(bankcsv) as csvfile:
    
    BankData = csv.reader(csvfile, delimiter=",")
    csv_header = next(BankData)
    line_count = 0

    for row in BankData:
        #print(row[0], row[1])
        #line_count += 1
        month_count = month_count + 1
        change = row[1]
        #netprofit = float(row[1])
        for change in row:
             int(row[1]) - int(row[1])
        #netprofit = "${:,.2f}".format(netprofit)
        #average = "${:,.2f}".format(average)
        #print(change)
        #line_count += 1
        avgchange = int(change)/int(month_count)
    print('Total Months:', month_count)
    #print('Total Net Profit:',netprofit)
    #print('Average Change:', '$',average)
    #print('Total Profits:', netprofit)
print('Average Change:', avgchange)