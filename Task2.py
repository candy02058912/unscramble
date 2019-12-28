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

for incoming, answering, _, duration in calls:
    try:
        phone_dict[incoming] += int(duration)
    except KeyError:
        phone_dict[incoming] = int(duration)
    finally:
        if phone_dict[incoming] > current_max_duration:
            current_max_duration = phone_dict[incoming]
            current_max_number = incoming

    try:
        phone_dict[answering] += int(duration)
    except KeyError:
        phone_dict[answering] = int(duration)
    finally:
        if phone_dict[answering] > current_max_duration:
            current_max_duration = phone_dict[answering]
            current_max_number = answering

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
    current_max_number, current_max_duration))
