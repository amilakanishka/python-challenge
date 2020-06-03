import csv
from pathlib import Path

#  Constants
CONST_RESOURCES_PATH = "../PyBank/Resources/budget_data.csv"
# --------------------------

# Variables
total_months = 0
total = 0.0 
first_profit_loss = 0.0
last_profit_loss = 0.0
current_profit_loss = 0.0
average_profit = 0.0
change_profit = 0.0
greatest_increase = 0.0
greatest_increase_month = ""
greatest_decrease_month = ""
greatest_decrease = 0.0
# --------------------------

# current module path
base_path = Path(__file__).parent
# resource csv file path 
file_path = (base_path /  CONST_RESOURCES_PATH).resolve()

file = open(file_path,"r")
reader = csv.reader(file)
# skip the header of the csv
next(reader,None)

# loop though the csv file each line
for line in reader:
    current_profit_loss = float(line[1])
    total += current_profit_loss
    total_months +=1
    change_profit = current_profit_loss - last_profit_loss
    if(greatest_increase < change_profit):
        greatest_increase = change_profit
        greatest_increase_month = line[0]

    if(greatest_decrease > change_profit):
        greatest_decrease = change_profit
        greatest_decrease_month = line[0]

    if(total_months ==1):
        first_profit_loss = current_profit_loss

    # Just before leaving the loop update last_profit_loss
    last_profit_loss = current_profit_loss

average_profit  = round((last_profit_loss - first_profit_loss)/(total_months - 1),2)
print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {total_months}")
print("Total : $" + "{:.0f}".format(total))
print(f"Average Change : {average_profit }")
print(f"Greatest Increase in Profits: {greatest_increase_month} " + "($"+"{:.0f}".format(greatest_increase)+")")   
print(f"Greatest Decrease in Profits: {greatest_decrease_month} " + "($"+"{:.0f}".format(greatest_decrease)+")")  