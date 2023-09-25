import csv
import sys

total_sum = 0
month_count = 0
i = 0
change_value = 0   
greatest_increase = -1 * sys.maxsize
greatest_decrease = sys.maxsize
previous_value = 0
average = 0
total_change_value = 0
change_value_count = 0
greatest_increase_date = ""
greatest_decrease_date = ""



with open("Resources/budget_data.csv", "r") as budget_data:
    for line in budget_data:
        if i == 0:
           #Don't do anything. i = 0 is the header row
           i = i + 1
           continue 
        #print(line.rstrip("/n"))
        line_array = line.split(",")
        temp_amount = int(line_array[1])
        total_sum = total_sum + temp_amount
        month_count = month_count + 1
        
        #Don't calculate change until we are at 2nd row
        if i >= 2 : 
            change_value = temp_amount - previous_value
            change_value_count = change_value_count + 1
            total_change_value = total_change_value + change_value
            
            

            if change_value > greatest_increase:
                greatest_increase = change_value
                greatest_increase_date = line_array[0]

            if change_value < greatest_decrease:
                greatest_decrease = change_value
                greatest_decrease_date = line_array[0]
            
            
        
        previous_value = temp_amount
        i = i + 1
        
average = total_change_value / change_value_count
print("Financial Analysis")
print("\n")
print("----------------------------")
print("Total Months: "+ str(month_count))
print("\n")
print("Total: $"+ str(total_sum))
print("\n")
print("Average Change: $"+ str(round(average, 2)))  
print("\n")
print("Greatest Increase in Profits " + greatest_increase_date + " ($" + str(greatest_increase) + ")")
print("\n")
print("Greatest Decrease in Profits " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")

with open("Resources/Financial_analysis.txt", 'w') as sys.stdout:
    print("Financial Analysis")
    print("\n")
    print("----------------------------")
    print("Total Months: "+ str(month_count))
    print("\n")
    print("Total: $"+ str(total_sum))
    print("\n")
    print("Average Change: $"+ str(round(average, 2)))  
    print("\n")
    print("Greatest Increase in Profits " + greatest_increase_date + " ($" + str(greatest_increase) + ")")
    print("\n")
    print("Greatest Decrease in Profits " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")



