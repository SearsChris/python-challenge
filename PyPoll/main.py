import os
import csv
# point to Election data csv
poll_csv = os.path.join("Resources", "03-python_HW_Instructions_PyPoll_Resources_election_data.csv")

vote_count = 0
vote = 0
#create null dictionary
candidlist = {}

with open(poll_csv) as csvfile:
    electiondata = csv.reader(csvfile, delimiter=',')
    csv_header = next(electiondata)
    for row in electiondata:
        vote_count = vote_count + 1
        candidate = row[2]
        if candidate not in candidlist:
            candidlist.update({candidate : 1})
        else:
            candidlist[candidate] += 1
    print(candidlist)
    CandidateName = ""
    winner = 0
    for candidate in candidlist:
        print(candidate)
        vote_percent = (candidlist[candidate]/vote_count) *100
        print({:.3vote_percent)
        #candidate with most votes wins.
        if candidlist[candidate] > winner:
            winner = candidlist[candidate]
            CandidateName = candidate
    print(CandidateName + str(winner))


