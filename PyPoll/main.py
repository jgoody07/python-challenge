import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(election_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip over the header data
    next(csvreader)
   
    # set Variables to zero
    total_voters = 0
    
    # Lists to store data
    candidates = []
    # dictonary
    Candidate_Votes = {}

    # Loop through the data
    for row in csvreader:

        # The total number of votes cast - total rows
        total_voters = total_voters + 1
                
        # A complete list of candidates who received votes
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)

    # The total number of votes and percentage of votes each candidate won
            Candidate_Votes[candidate_name] = 0
        Candidate_Votes[candidate_name] = Candidate_Votes[candidate_name] + 1
    print(candidates)
    for x, y in Candidate_Votes.items():
        print(x, y)
        percent_votes = (y / total_voters) *100 
        print(percent_votes)

    # The winner of the election
    import operator
    winner = max(Candidate_Votes.items(), key=operator.itemgetter(1))[0]
    print(winner)

    print(f"Election Results\n"
    f"--------------------------------\n"
    f"Total Votes: {total_voters}\n"
    f"---------------------------------\n"
    f"{x, y}, {percent_votes}\n"
    f"---------------------------------\n"
    f"Winner: {winner}\n"
    f"---------------------------------\n")

