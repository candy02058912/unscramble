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
"""

phone_dict = {}
current_max_duration = 0
current_max_number = ''

for calling, answering, _, duration in calls:
    if phone_dict.get(calling):
        phone_dict[calling] += int(duration)
    else:
        phone_dict[calling] = int(duration)

    if phone_dict[calling] > current_max_duration:
        current_max_duration = phone_dict[calling]
        current_max_number = calling

    if phone_dict.get(answering):
        phone_dict[answering] += int(duration)
    else:
        phone_dict[answering] = int(duration)

    if phone_dict[answering] > current_max_duration:
        current_max_duration = phone_dict[answering]
        current_max_number = answering

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
    current_max_number, current_max_duration))
