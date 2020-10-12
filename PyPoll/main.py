import os
import csv
# point to Election data csv
poll_csv = os.path.join("Resources", "03-python_HW_Instructions_PyPoll_Resources_election_data.csv")

vote_count = 0
vote = 0
#create null dictionary
candidlist = {}

#Open CSV
with open(poll_csv) as csvfile:
    electiondata = csv.reader(csvfile, delimiter=',')
    csv_header = next(electiondata)
    print(f"CSV Header: {csv_header}")

    for row in electiondata:
        vote_count = vote_count + 1
        candidate = row[2]
        if candidate not in candidlist:
            candidlist.update({candidate : 1})
        else:
            candidlist[candidate] += 1
    print(candidlist)

    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {vote_count}")
    print("-----------------------")

    #Find percentage of votes
    CandidateName = ""
    winner = 0
    for candidate in candidlist:
        print(f"{candidate}: {(candidlist[candidate]/vote_count)*100:.3f}%({candidlist[candidate]})")
        #print(candidate)
        #vote_percent = (candidlist[candidate]/vote_count) *100
        #vote_percent = "{:0.3f}%".format(vote_percent)
        #print(vote_percent)
        #candidate with most votes wins.
        if candidlist[candidate] > winner:
            winner = candidlist[candidate]
            CandidateName = candidate
    print("-----------------------")
    print(f'Winner:{CandidateName}' + 'with votes totalling ' + str(winner))

    #output into file

output_path = os.path.join("Analysis", "PyPoll_HW_Output.csv")

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow([f"Total Votes: {vote_count}"])
    for candidate in candidlist:
        csvfile.write(f"{candidate}:{(candidlist[candidate]/vote_count)*100:.3f}%({candidlist[candidate]})\n")
        csvfile.write("---------------------------\n")
    csvfile.write(f"Winner: {CandidateName}\n")



