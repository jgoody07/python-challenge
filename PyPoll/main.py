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
    
    print(f"Election Results\n"
    f"--------------------------------\n"
    f"Total Votes: {total_voters}\n"
    f"---------------------------------\n")

    for x in Candidate_Votes:
        percent_votes = (Candidate_Votes.get(x)/total_voters) *100 
        print(f"{x}: ({Candidate_Votes.get(x)}), {percent_votes:.2f}% \n")

    # The winner of the election
    import operator
    winner = max(Candidate_Votes.items(), key=operator.itemgetter(1))[0]
    print(f"---------------------------------\n"
    f"Winner: {winner}\n"
    f"---------------------------------\n")

# Print to txt file
    PollAnlysis = os.path.join("Analysis", "PollAnalysis.txt")
    with open (PollAnlysis, 'w') as txtfile:
        txtfile.write(f"Election Results\n"
        f"--------------------------------\n"
        f"Total Votes: {total_voters}\n"
        f"---------------------------------\n")

        for x in Candidate_Votes:
            percent_votes = (Candidate_Votes.get(x)/total_voters) *100 
            txtfile.write(f"{x}: ({Candidate_Votes.get(x)}), {percent_votes:.2f}% \n")

        # The winner of the election
        import operator
        winner = max(Candidate_Votes.items(), key=operator.itemgetter(1))[0]
        txtfile.write(f"---------------------------------\n"
        f"Winner: {winner}\n"
        f"---------------------------------\n")