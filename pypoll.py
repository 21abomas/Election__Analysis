#  The data we need to retrieve.
#1. The total number of votes cast
# 2. A Complete list of candidates who received votes
# 3. The percentage of votes each candidate - won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#import csv 
#print(dir(csv))

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
 # Print each row in the CSV file.
    headers = next(file_reader)
print(headers)

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")

# Write some data to the file.
outfile.write("counties in the election\n--------------------\nArapahoe\n Denver\n Jefferson")
# Close the file
outfile.close()
