#Import and read
import os
import csv
import statistics 

#Set count to 0
count = 0
#Set income total to 0
income_total = 0
#Define lists
monthly = []
month_change = []
maxx = []
minn = []
avg_change = []
greatest_increase = ['',0]
greatest_decrease = ['',9999999999999]

pybank_csv = os.path.join("","budget_data.csv")
     
#Open and read csv for total rows
with open(pybank_csv) as csvfile:
    pybank_data = csv.reader(csvfile)

    #Read header row first
    csv_header = next(pybank_data)
    #print(csv_header)
    prevline = next(pybank_data)
    count +=1
    income_total += int(prevline[1])
    # print(prevline)
    #Count months in data. Use += 1 for count = count + 1
    for row in pybank_data:
        count += 1
        income_total += int(row[1])
        month_change = int(row[1])-int(prevline[1])
        # print(month_change)

        if month_change > int(greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = row[1]

        if month_change < int(greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = row[1]
    
    avg_change = int(month_change)/int(count-1)
    
    
    # greatest_increase = max(int(month_change))
    # greatest_decrease = min(int(month_change))
        
          
#Open and read for adding 
# with open(pybank_csv, "r") as csvfile:
#     pybank_data = csv.DictReader(csvfile, delimiter=",")   

    #Add net income in column 'Profit/Losses'
    #for i in pybank_data:
        # income_total += int(row[1])

        # avg_change = [abs(monthly[row] - monthly[row+1]) 

        # print(str(income_total))
#Open and read for adding 
# with open(pybank_csv, "r") as csvfile:
#     pybank_data = csv.DictReader(csvfile, delimiter=",")
    
    #Loop through rows
    # for row in pybank_data: 
    #     monthly.append(int(row['Profit/Losses']))
        
    #Find monthly change
        # month_change = [abs(monthly[row] - monthly[row+1]) for row in range(len(monthly)-1)]

    #Find min and max
        #maxx = max(month_change) 
        #minn = min(month_change)

        #avg_change = statistics.mean(month_change)
    
    #Print the table

    print("Financial Analysis")
    print("..................")

    print("Total Months: " + str(count))
    print("Total: " + str(income_total))
    print("Average Change: " + str(avg_change))
    print("Greatest Increase: " + str(greatest_increase))
    print("Greatest Decrease: " + str(greatest_decrease))

    #   Export file as txt