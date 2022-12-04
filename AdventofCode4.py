inputfile = open('Day4.txt').read()
#inputfile = open('Day4E.txt').read()
elfpairs = inputfile.split('\n')
totalfulloverlaps = 0
totaloverlaps = 0

for line in elfpairs:

    elf1,elf2 = line.split(',', 1)
    elf1a,elf1b = elf1.split('-', 1)
    elf2a,elf2b = elf2.split('-', 1)
    task1 = range(int(elf1a), int(elf1b)+1)
    task2 = range(int(elf2a), int(elf2b)+1)
    
    tasklist1 = list(task1)
    tasklist2 = list(task2)
    
    if all(element in tasklist1 for element in tasklist2) or all(element in tasklist2 for element in tasklist1):
        print('Fully contained')
        totalfulloverlaps = totalfulloverlaps + 1

    if any(element in tasklist1 for element in tasklist2) or any(element in tasklist2 for element in tasklist1):
        print('Partially contained')
        totaloverlaps = totaloverlaps + 1

print('Total full overlaps: '+ str(totalfulloverlaps))
print('Total partial overlaps: '+ str(totaloverlaps))