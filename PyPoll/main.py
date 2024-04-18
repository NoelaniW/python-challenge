import csv
import os

#set path for importing and exporting csv and txt
input_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis","analysis.txt")

#defined variables
total_votes = 0
votes_for_cand = {}
candidates = []
winning_cand = ""
winning_vote = 0

#read csv file
with open(input_file) as election_data:
    csv_reader=csv.DictReader(election_data)

#loop to calculate total votes, candidate names
    for row in csv_reader:
        total_votes = total_votes + 1
        candidates_name = row["Candidate"]
        
        if candidates_name not in candidates:
            candidates.append(candidates_name)
            votes = votes_for_cand[candidates_name] = 0

        votes_for_cand[candidates_name] = votes_for_cand[candidates_name] + 1

#printed final total and exported as a text file
with open(output_file, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"Total votes: {total_votes}\n"
            )

    print(election_results)

    txt_file.write(election_results)

#loop to calculate candidates and their percentage of votes and winner
    for candidate in votes_for_cand:
        votes = votes_for_cand.get(candidate)
        vote_percent = float(votes)/float(total_votes) * 100

        if votes > winning_vote:
            winning_vote = votes
            winning_cand = candidate
#printed vote percentage with 3 decimal places and exported file as text
        voter_selection = f"{candidate}: {vote_percent:.3f}% ({votes})\n"
        print(voter_selection)

        txt_file.write(voter_selection)

    winners_summary = (f"Winner: {winning_cand}\n")
                   
    print(winners_summary)

    txt_file.write(winners_summary)