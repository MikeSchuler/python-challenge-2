# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import csv
import statistics 
import collections

pypoll_file = "/Users/Mike/Documents/Python_Homework/python-challenge-2/PyPoll/Resources_election_data.csv"

count = 0
candidate_votes = {}

# The total number of votes cast
with open(pypoll_file, "r") as csvfile:
    pypoll_data = csv.DictReader(csvfile, delimiter = ",")

    for row in pypoll_data:
        count += 1
        
        if row['Candidate'] in candidate_votes.keys():
            candidate_votes[row['Candidate']] += 1
        else:
            candidate_votes[row['Candidate']] = 1

            
            
    print(candidate_votes)
    

    #print(row['Candidate'])   
    
    print(row)

    print("Total Votes: " + str(count))

# A complete list of candidates who received votes

    
    
