
import os
import csv
# define variables

bankcsv = 'Resources/Budgetdata.csv'
month_count = 0
netprofit = 0
with open(bankcsv) as csvfile:
    
    BankData = csv.reader(csvfile, delimiter=",")
    csv_header = next(BankData)
    print(BankData)

    for row in BankData:
        month_count = float(month_count + 1)
        netprofit = float(row[1])
        average = netprofit/month_count
        #netprofit = "${:,.2f}".format(netprofit)
        #average = "${:,.2f}".format(average)
    print('Total Months:', month_count)
    print('Total Net Profit:',netprofit)
    print('Aberage Change:', '$',average)
   # print('Total Profits:', netprofit)



    #total_months = str(len(BankData))
    #print(BankData)
#net_total = 
#avg_chage = 
#greatest_increase = 
#greatest_decrease = 