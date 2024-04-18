import csv
import os
input_file = os.path.join("Resources","budget_data.csv")
output_file = os.path.join("Analysis", "analysis.txt")

total_months = 0
previous_net = 0
changes_monthly = []
net_change_list = []
greatest_increase= ["",0]
greatest_decrease= ["",99999999999999999999]
net_total = 0

with open(input_file) as Fin_data:
    csv_reader=csv.DictReader(Fin_data)

    for row in csv_reader:
        total_months = total_months + 1
        net_total = net_total + int(row["Profit/Losses"])

        net_change = int(row["Profit/Losses"]) - previous_net
        previous_net = int(row["Profit/Losses"])
        net_change_list = net_change_list + [net_change]
        changes_monthly = changes_monthly + [row["Date"]]


        if net_change > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = net_change

net_average = sum(net_change_list)/len(net_change_list)

output = (f"\nFinancial Analysis\n"
    f"Total months: {total_months}\n"
    f"Net total: ${net_total}\n"
    f"Average change: ${net_average}\n"
    f"Greatest increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open (output_file, "w") as txt_file:
    txt_file.write(output)

