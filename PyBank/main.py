import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resource', 'budget_data.csv')

# Read in the CSV file
with open(budget_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip over the header data
    next(csvreader)

    #set Variables to zero
    Total_month = 0
    Profit_loss = 0
    Change_Profit_loss = []

    # Loop through the data
    for row in csvreader:
        
        #The total number of months included in the dataset - total rows
        Total_month = Total_month + 1

        #The net total amount of "Profit/Losses" over the entire period
        Profit_loss = Profit_loss + row[1]

        #The average of the changes in "Profit/Losses" over the entire period
        Change_Profit_loss.apend(int(row[1])) 
        
    For i in range(0, len(Change_Profit_loss)):
        Change_Profit_loss[i+1] - Change_Profit_loss[i]
        Change_Profit_loss_Total = (Change_Profit_loss[i+1] - Change_Profit_loss[i])
#The greatest increase in profits (date and amount) over the entire period
If statement 
If my second value is greater than first value 

#The greatest decrease in losses (date and amount) over the entire period