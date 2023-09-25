import csv
import sys

i = 0
total_votes = 0
candidate = ""
candidate_vote_count = 0
candidate_vote_count_dict = dict()
candidate = ""
highest_votes_count_name = ""
highest_votes_count = 0

with open("Resources/election_data.csv", "r") as election_data:
    for line in election_data:
        line = line.rstrip("/n")
        if i == 0:
           #Don't do anything. i = 0 is the header row
           i = i + 1
           continue 
        #print(line.rstrip("/n"))
        total_votes = total_votes + 1
        

        if i >= 2 : 
            vote_array_previous = previous_line.split(",")
            previous_candidate = vote_array_previous[2]
            previous_candidate = previous_candidate.rstrip()

            vote_array = line.split(",")
            candidate = vote_array[2]
            candidate = candidate.rstrip()
            candidate_vote_count = candidate_vote_count + 1
            if previous_candidate != candidate:
                if previous_candidate in candidate_vote_count_dict.keys():
                    temp_count = candidate_vote_count_dict[previous_candidate]
                    candidate_vote_count_dict[previous_candidate] = candidate_vote_count + temp_count
                else:
                    candidate_vote_count_dict[previous_candidate] = candidate_vote_count
                candidate_vote_count = 0

        previous_line = line
        i = i + 1   
#Last row will not be counted. So we need to add 1 to the last candidate
candidate_vote_count = candidate_vote_count + 1
if candidate in candidate_vote_count_dict.keys():
    temp_count = candidate_vote_count_dict[candidate]
    candidate_vote_count_dict[candidate] = candidate_vote_count + temp_count 
else:
    candidate_vote_count_dict[candidate] = candidate_vote_count
print("Election Results")
print("-------------------------")
print("Total Votes: "+ str(total_votes))
print("-------------------------")


for key in candidate_vote_count_dict:
    percentage = candidate_vote_count_dict[key] / total_votes * 100
    print(key + ": " + str(round(percentage, 3)) + "% (" + str(candidate_vote_count_dict[key]) + ")")
    if candidate_vote_count_dict[key] > highest_votes_count: 
        highest_votes_count = candidate_vote_count_dict[key]
        highest_votes_count_name = key
print("-------------------------")
print("Winner: " + highest_votes_count_name)
print("-------------------------")

with open("Resources/election_data.txt", 'w') as sys.stdout:

    print("Election Results")
    print("-------------------------")
    print("Total Votes: "+ str(total_votes))
    print("-------------------------")


    for key in candidate_vote_count_dict:
        percentage = candidate_vote_count_dict[key] / total_votes * 100
        print(key + ": " + str(round(percentage, 3)) + "% (" + str(candidate_vote_count_dict[key]) + ")")
        if candidate_vote_count_dict[key] > highest_votes_count: 
            highest_votes_count = candidate_vote_count_dict[key]
            highest_votes_count_name = key
    print("-------------------------")
    print("Winner: " + highest_votes_count_name)
    print("-------------------------")
