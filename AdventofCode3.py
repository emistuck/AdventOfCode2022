inputFile = open('Day3.txt').read()
#inputFile = open('Day3Examples.txt').read()
rucksacks = inputFile.split('\n')
sumpriority = 0
groups = int(len(rucksacks)/3)

import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase):
   values[letter] = index + 1

for line in rucksacks:
    rucksack = str(line)
    compartmentsize = int(len(rucksack)/2)
    compartment1, compartment2 = line[:compartmentsize], line[compartmentsize:]

    for item in values:
        if item in compartment1 and item in compartment2:
           priority = values[item]
           sumpriority = sumpriority + priority
           print('Match! '+ item + ' Priority ' + str(priority)) 

print('Total sum of priorities: ' + str(sumpriority))

group = 0
bag = 0
sumbadge = 0

while group < groups:
    group = group + 1
    
    bag1 = rucksacks[bag]
    bag = bag + 1
    bag2 = rucksacks[bag]
    bag = bag + 1
    bag3 = rucksacks[bag]
    bag = bag + 1

    for item in values:
        if item in bag1 and item in bag2 and item in bag3:
            badge = values[item]
            sumbadge = sumbadge + badge
            print('Group Badge: ' + str(badge))

print('Sum of Badge Priorities: ' + str(sumbadge))