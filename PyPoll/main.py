import csv
import os

def publish_results(voteDict):
    candidates = voteDict.keys()
    each_votes = voteDict.values()
    each_percentage = []
    each_votes_formatted = []
    candidates_formatted = []
    total_votes = sum(each_votes)
    winner = max(voteDict, key = voteDict.get)

    # calculate vote percentages and format votes
    for v in each_votes:
        each_percentage.append(f"{(v/total_votes)*100:.3f}%")
        each_votes_formatted.append(f"({v})")
    
    # format the candidate name
    for candidate in candidates:
        candidates_formatted.append(f"{candidate}:") 
    
    results = zip(candidates_formatted,each_percentage,each_votes_formatted)

    output_file = os.path.join("analysis", "output.csv")
    with open(output_file, "w", newline='\n') as datafile:
        writer = csv.writer(datafile, delimiter =" ", escapechar=' ', quoting=csv.QUOTE_NONE)
        writer.writerow(["Election Results".strip()])
        writer.writerow(["-------------------------"])
        writer.writerow([f"Total Votes: {total_votes}"])
        writer.writerow(["-------------------------"])
        writer.writerows(results)
        writer.writerow(["-------------------------"])
        writer.writerow([f"Winner: {winner}"])
        writer.writerow(["-------------------------"])

def print_results(file_path):
    with open(file_path, "r") as analysis_file:
        csvreader = csv.reader(analysis_file)
        for line in csvreader:
            print(line[0])

# Dictionary to hold votes information
votes = {}
file_path = os.path.join("Resources", "election_data.csv")
with open(file_path, "r") as poll_file:
    csvreader = csv.reader(poll_file)
    # skip the header of the csv
    next(csvreader,None)
    # loop though rows of the csv file
    for line in csvreader:
        if line[2] not in votes:
            votes[line[2]] = 1
        else:
            votes[line[2]] += 1 

publish_results(votes)
print_results(os.path.join("analysis", "output.csv"))


