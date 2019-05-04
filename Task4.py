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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

receivedCalls = []
sentTexts = []
receivedTexts = []
telemarketers = []

for call in calls:
    if call[1] not in receivedCalls:
        receivedCalls.append(call[1])

for text in texts:
    if text[0] not in sentTexts:
        sentTexts.append(text[0])
    if text[1] not in receivedTexts:
        receivedTexts.append(text[0])

for call in calls:
    if (call[0] not in receivedCalls and 
    call[0] not in sentTexts and 
    call[0] not in receivedTexts and 
    call[0] not in telemarketers):
        telemarketers.append(call[0])

telemarketers.sort()

print("These numbers could be telemarketers:")
for marketer in telemarketers:
    print(marketer)

"""
Run Time Analysis
**********************
O(n^3) - Three loops through lists of length n

"""