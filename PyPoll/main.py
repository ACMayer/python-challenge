# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #creates counters for each candidates votes
    totalvoters=0
    Candidate1Count=0
    Candidate1 = "Charles Casper Stockham"
    Candidate2Count=0
    Candidate2 = "Diana DeGette"
    Candidate3Count=0
    Candidate3 = "Raymon Anthony Doane"

    # Read each row of data after the header and calculate candidate counts
    for row in csvreader:
        totalvoters += 1
        if row[2] ==Candidate1:  
           Candidate1Count += 1
        elif row[2]==Candidate2: 
           Candidate2Count += 1
        elif row[2]==Candidate3: 
           Candidate3Count += 1
#calculates the percentage of votes for each candidate
Candidate1Cntge = Candidate1Count/totalvoters*100
Candidate2Cntge = Candidate2Count/totalvoters*100
Candidate3Cntge =  Candidate3Count/totalvoters*100
#rounds the percentage values of votes
Can1Rp = round(Candidate1Cntge,3)
Can2Rp = round(Candidate2Cntge,3)
Can3Rp = round(Candidate3Cntge,3)

#prints results of the Election as the task is now finished with all votes counted.
print ("Election Results" )
print ("---------------------------------------------------------")
print ("Total Voters:       " + str((totalvoters-1)))
print ("---------------------------------------------------------")
print(f"{Candidate1}:  {Can1Rp}% ({Candidate1Count})")
print(f"{Candidate2}:  {Can2Rp}% ({Candidate2Count})")
print(f"{Candidate3}:  {Can3Rp}% ({Candidate3Count})")
print ("---------------------------------------------------------")
if (Candidate1Count > Candidate2Count) & (Candidate1Count > Candidate3Count):
    print(f"The Winner is {Candidate1}")
if (Candidate2Count > Candidate1Count) & (Candidate2Count > Candidate3Count):
    print(f"The Winner is {Candidate2}")
if (Candidate3Count > Candidate1Count) & (Candidate3Count > Candidate2Count):
    print(f"The Winner is {Candidate3}")
print ("---------------------------------------------------------")

#produces new text document with the following infomation on the following lines. 
lines= ['Election Results','---------------------------------------------------------','Total Voters: 369711',
        'Charles Casper Stockham:  23.048% (85213)','Diana DeGette:  73.812% (272892)','Raymon Anthony Doane:  3.139% (11606)',
         '---------------------------------------------------------','The Winner is Diana DeGette',
         '---------------------------------------------------------', ]


#Creates text file
with open ('analysis/Election Results.txt','w') as f:
    f.writelines('\n'.join(lines))
    f.close()

