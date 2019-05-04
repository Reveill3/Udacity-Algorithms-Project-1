"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_list = []

def add_unique_numbers(entries):
    for entry in entries:
        if entry[0] not in unique_list:
            unique_list.append(entry[0])
        if entry[1] not in unique_list:
            unique_list.append(entry[1])

add_unique_numbers(calls)
add_unique_numbers(texts)

"""
Run Time Analysis
**********************
O(n^3) - Worst case is that it would have to loop through all the entries 3 times if they were all unique numbers.
"""

print("There are {} different telephone numbers in the records.".format(len(unique_list)))

