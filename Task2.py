"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
dx
"""

"""
Run Time Analysis
**********************
O(n) - One loop through entries
"""

unique_list = []
duration_dicts = []
def add_unique_numbers(entries):
    for entry in entries:
        if entry[0] not in unique_list:
            unique_list.append(entry[0])
        if entry[1] not in unique_list:
            unique_list.append(entry[1]) 
"""
Run Time Analysis
**********************
O(n^3) - Above is Same as Task1
"""

add_unique_numbers(calls)

for number in unique_list:
    duration_dicts.append({
        "number": number,
        "duration": 0
    })
"""
Run Time Analysis
**********************
O(n) - One loop through entries
"""

for call in calls:
    for duration_dict in duration_dicts:
        if duration_dict["number"] == call[0]:
            duration_dict["duration"] += int(call[3])
        if duration_dict["number"] == call[1]:
            duration_dict["duration"] += int(call[3])
"""
Run Time Analysis
**********************
O(n^2)
"""

largest_number = ""
largest_duration = 0


for duration_dict in duration_dicts:
    if duration_dict["duration"] > largest_duration:
        largest_duration = duration_dict["duration"]
        largest_number = duration_dict["number"]
"""
Run Time Analysis
**********************
O(n) - One loop
"""

print("{} spent the longest time, {} seconds, on the phone during September 2016."
.format(largest_number, largest_duration))


"""
Overall Run Time Analysis
**********************
O(n^3)
"""