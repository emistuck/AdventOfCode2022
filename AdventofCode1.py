
caloriesinput = open('Day1.txt')
calories = caloriesinput.read()
calorieslist = calories.replace('\n', ',')
calorieslist = calorieslist.replace(',,', ',0,')
calorieslist = calorieslist.replace(',','\n')
calorieslist = calorieslist.split()
calorieslist = list(map(int,calorieslist))
mostcalories = 0
secondmostcalories = 0
thirdmostcalories = 0
placeinlist = 0
sumcurrent = 0
numbercalories = len(calorieslist)

while(placeinlist < numbercalories):
    if calorieslist[placeinlist] > 0:
        sumcurrent = sumcurrent+calorieslist[placeinlist]
        
    else:
        if sumcurrent > mostcalories:
            thirdmostcalories = secondmostcalories
            secondmostcalories = mostcalories
            mostcalories = sumcurrent
            sumcurrent=0
        elif sumcurrent > secondmostcalories:
            thirdmostcalories = secondmostcalories
            secondmostcalories = sumcurrent
            sumcurrent = 0
        elif sumcurrent > thirdmostcalories:
            thirdmostcalories = sumcurrent
            sumcurrent = 0
        else:
            sumcurrent = 0

    placeinlist = placeinlist + 1

topthreecalories = mostcalories + secondmostcalories + thirdmostcalories    
print("Most Calories = ",mostcalories)
print("Second Most Calories = ",secondmostcalories)
print("Third Most Calories = ",thirdmostcalories)
print("Top Three sum of Calories = ",topthreecalories)