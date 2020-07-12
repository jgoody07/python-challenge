import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

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
    List_month = []

    # Loop through the data
    for row in csvreader:
        
        #The total number of months included in the dataset - total rows
        Total_month = Total_month + 1
        
        #The net total amount of "Profit/Losses" over the entire period
        Profit_loss = Profit_loss + int(row[1])
        month = row[0]
       
        #The average of the changes in "Profit/Losses" over the entire period
        Change_Profit_loss.append(int(row[1]))
        List_month.append(month)

    Change_Total=[]   
    for i in range(0, len(Change_Profit_loss)-1):
        change = Change_Profit_loss[i+1] - Change_Profit_loss[i]
        Change_Total.append(change)
    print(len(Change_Total))
    print(Total_month)
    Average_Change = sum(Change_Total)/len(Change_Total)
    print(Average_Change)

    #The greatest increase in profits (date and amount) over the entire period
    Greatest_increase = max(Change_Total)
    Greatestloc = Change_Total.index(Greatest_increase)
    print(List_month[Greatestloc + 1]) # +1 because first row does not have change
    print(Greatest_increase)
      
    #The greatest decrease in losses (date and amount) over the entire period
    Greatest_decrease = min(Change_Total)
    print(Greatest_decrease)
    Leastloc = Change_Total.index(Greatest_decrease)
    print(List_month[Leastloc + 1])

    print(f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Total_month}\n"
    f"Total: {Profit_loss}\n"
    f"Average  Change: {Average_Change}\n"
    f"Greatest Increase in Profits: {List_month[Greatestloc + 1]} ({Greatest_increase})\n"
    f"Greatest Decrease in Profits: {List_month[Leastloc + 1]} ({Greatest_decrease})")



   
