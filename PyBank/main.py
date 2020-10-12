import os
import csv

bank_csv = os.path.join('Resources', 'Budget_data.csv')

with open(bank_csv) as csvfile:
    
    csvreader = csv.reader(bank_csv, delimiter=",")
    csv_header = next(csvreader)
    print(csvreader)

    for row in csvreader:
        print(row[0])


#total_months =
#net_total = 
#avg_chage = 
#greatest_increase = 
#greatest_decrease = 