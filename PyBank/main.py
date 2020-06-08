import csv
import os

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

file_path = os.path.join("Resources", "budget_data.csv")
with open(file_path, "r") as bank_file:
    csvreader = csv.reader(bank_file)
    # store the header and move the reader to data in csv
    header = next(csvreader,None)
    if header[0] == 'Date' and header[1] == 'Profit/Losses':
        # loop though rows of the csv file
        for line in csvreader:
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

results = ("Financial Analysis",
            "----------------------------",
            f"Total Months : {total_months}",
            "Total : $" + "{:.0f}".format(total),
            f"Average Change : {average_profit }",
            f"Greatest Increase in Profits: {greatest_increase_month} " + "($"+"{:.0f}".format(greatest_increase)+")",
            f"Greatest Decrease in Profits: {greatest_decrease_month} " + "($"+"{:.0f}".format(greatest_decrease)+")")

#  print results
for row in results:
    print(row) 

# publish the analysis to output.csv
output_file = os.path.join("analysis", "output.csv")
with open(output_file, "w", newline='\n') as datafile:
    writer = csv.writer(datafile, delimiter =" ", escapechar=' ', quoting=csv.QUOTE_NONE)
    writer.writerows(results)