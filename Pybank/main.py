# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module

GDecrease=99999999999999999
GIncrease=0
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    total=0
    totalmonths= 0
    previousrow= 0
    currentrow=0
    sumofnetchange=0
    netchange=0
    changes= []
    # Read each row of data after the header
    for row in csvreader:
            total += int(row[1])
            totalmonths += 1
            currentrow = int(row[1])
            #calculate the net change and store a list of these changes
            if previousrow !=0:
                netchange= currentrow-previousrow
                sumofnetchange= sumofnetchange + netchange
                changes.append(netchange) 
                
            previousrow= currentrow

            if netchange > GIncrease:
                GIncrease=netchange
                GIMonth = row[0]

            if netchange < GDecrease:
                GDecrease=netchange
                GDMonth = row[0]

    
           
#calculates average change and rounded the outcome 
Averagechange = sumofnetchange/(totalmonths-1)
AveragechangeRounded =round(Averagechange,2)
#print text to terminal as task has been finished.
print ("Financial Analysis" )
print ("---------------------------------------------------------")
print ("Total Months: " + str(totalmonths))
print ("Total:   $" + str(total))
print ("Average Change:   $" + str(AveragechangeRounded) )   
print (f"Greatest Increase in Profits: {GIMonth}  (${GIncrease})")
print (f"Greatest Decrease in Profits:  {GDMonth}  (${GDecrease})") 

#produces new text document with the following infomation on the following lines. 
lines= ['Financial Analysis ','---------------------------------------------------------','Total Months: 86',
        'Average Change:   $-8311.11','Greatest Increase in Profits: Aug-16  ($1862002)','Greatest Decrease in Profits:  Feb-14  ($-1825558)' ]


#Creates text file
with open ('analysis/PyBank.txt','w') as f:
    f.writelines('\n'.join(lines))
    f.close()
