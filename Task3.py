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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

codes=[]
bangalore_to_bangalore = 0
total_bangalore_calls = []

def GetCode(number):
    if number[0] == "(":
        fixed_line_code = []
        i = 0
        while number.strip()[i] != ")":
            if number[i] != "(":
                fixed_line_code.append(number[i])
            i += 1
            
        fixed_line_code = "".join(fixed_line_code)
        return fixed_line_code
    if " " in number:
        mobile_prefix = number[0:4]
        if mobile_prefix[0] == "7" or mobile_prefix[0] == "8" or mobile_prefix[0] == "9":
            return mobile_prefix
        else:
            return None
    if number[0:3] == "140":
        return "140"
    return None

for call in calls:
    callerCode = GetCode(call[0])
    answerCode = GetCode(call[1])
    if callerCode.startswith("080") and answerCode not in codes and answerCode != None:
        codes.append(answerCode)
    if callerCode == "080" and answerCode == "080":
      bangalore_to_bangalore = bangalore_to_bangalore + 1
codes.sort()

"""
Run Time Analysis
**********************
O(n) - One loop through all calls. Other loops are small in comparison to the length of call list.

"""




print("The numbers called by people in Bangalore have codes:")
for code in codes:
    print(code)

for call in calls:
    for code in codes:
        if code == "080":
            code = "(080)"
            if call[0].startswith(code):
                total_bangalore_calls.append(call)
print("**************************")
print("{} percent of calls from fixed lines in Bangalore are calls".format(round(bangalore_to_bangalore/len(total_bangalore_calls) * 100, 2)) +
" to other fixed lines in Bangalore.")