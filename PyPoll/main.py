import os
import csv

election_data = os.path.join("Resources","election_data.csv")

# Creating a list to capture the election data
t_votes = 0
candidates = []
no_votes = []
percent_votes = [] 


with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        t_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            no_votes.append(1)
        else:
            index = candidates.index(row[2])
            no_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in no_votes:
        percentage = (votes/t_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # The winner
    winner = max(no_votes)
    index = no_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying the election results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(t_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(no_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting the election results to text format
output = open("Election_Results.txt", "w")

line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(t_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(no_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))