import os
import csv

# Creating an object from the CSV file
budget_data = os.path.join("Resources/budget_data.csv")

t_months = 0
t_pl = 0
value = 0
change = 0
dates = []
profits = []

# Reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Reading the header row
    csv_header = next(csvreader)

    # Reading the first row for proper tracking of changes made
    first_row = next(csvreader)
    t_months += 1
    t_pl += int(first_row[1])
    value = int(first_row[1])
    
    # Going through each row of data after the header & first row 
    for row in csvreader:

        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, and add to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        # Total number of months
        t_months += 1

        # Total net amount of "Profit/Losses over entire period"
        t_pl = t_pl + int(row[1])

    # Greatest profits increase
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Greatest profits decrease 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Avg "Profit/Losses changes over the entire period"
    avg_change = sum(profits)/len(profits)
    

# Info display
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {str(t_months)}")
print(f"Total: ${str(t_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

# Exporting the info dispaly to text format
output = open("Financial_Analysis.txt", "w")

line1 = "Financial Analysis"
line2 = "----------------------------------"
line3 = str(f"Total Months: {str(t_months)}")
line4 = str(f"Total: ${str(t_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))