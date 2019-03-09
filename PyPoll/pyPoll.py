import os
import csv
import numpy
#importing file
budget_data = os.path.join(os.path.expanduser('~'),"desktop","data analytics bootcamp","python","election_data.csv")
#locating csv file

#store data as list
voters = []
candidates = []


with open(budget_data, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
#creating csv reader 
    print(csvreader)

    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    headers = csv_header.split (',')
    print('headers split up:' , headers)


    for row in csvreader:
        voters.append(row[0])
        candidates.append(row[2])

#total voters
total_voters = len(voters)
#candidate vote calculations     
Khan_votes = (candidates.count("Khan"))
Correy_votes = (candidates.count("Correy"))
Li_votes = (candidates.count("Li"))
OTooley_votes = (candidates.count("O'Tooley"))
# winner


print("Election Results")
print("-----------------------------------------------")
print("The total number of votes cast:", total_voters)
print("-----------------------------------------------")
print("Khan:", round((Khan_votes / total_voters) * 100, 3))
print("Correy:", round((Correy_votes / total_voters) * 100, 3))
print("Li:", round((Li_votes / total_voters) * 100, 3))
print("O'Tooley:", round((OTooley_votes / total_voters) * 100, 3))
print("-----------------------------------------------")
print("Winner", "Khan, congraulations")

file = open("output_pyPoll.txt", "w")
file.write("Election Results")
file.write("-----------------------------------------------")
file.write("The total number of votes cast: 3521001")
file.write("-----------------------------------------------")
file.write("Khan: 63.00%")
file.write("Correy: 20.00%")
file.write("Li: 14.00%")
file.write("O'Tooley: 3.00%")
file.write("-----------------------------------------------")
file.write("Winner: Khan")
file.close()