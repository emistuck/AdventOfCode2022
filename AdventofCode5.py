inputfile = open('Day5.txt').read().split('\n')
#inputfile = open('Day5E.txt').read().split('\n')
i = 0
s = 0
data = True
instructions = False
S1,S2,S3,S4,S5,S6,S7,S8,S9 = [],[],[],[],[],[],[],[],[]

for line in inputfile:
    if line.startswith(' 1'):
        s = line[-2]
        s = int(s)
        break

#stacks = dict.fromkeys((range(s)))

#listofstacks = []
#for i in range(s):
#    listofstacks.append("S"+str(i+1))
#listoflists = []
#for i in range(s):
#    listoflists.append([])
#stacks = dict(zip(listofstacks, listoflists))

#stacks = {}  
#for x in range(1,s+1):  
#    stacks["S"+str(x)] = []
#stacks = list(stacks.keys())

for line in inputfile:
    
    if line.startswith(' 1   2'):
        data = False
    elif line.startswith('move'):
        instructions = True
    elif data == True:   
        crates = line.replace('    ', '#.')
        crates = crates.replace(' ', '.')
        crates = crates.replace('#', '')
        crates = crates.replace('[', '')
        crates = crates.replace(']', '')

        crates = crates.split('.')
        print(crates)
         
        if s >= 1:
            if crates[0] != '': S1.insert(0,crates[0])
        if s >= 2:
            if crates[1] != '': S2.insert(0,crates[1])
        if s >= 3:
            if crates[2] != '': S3.insert(0,crates[2])
        if s >= 4:
            if crates[3] != '': S4.insert(0,crates[3])
        if s >= 5:
            if crates[4] != '': S5.insert(0,crates[4])
        if s >= 6:
            if crates[5] != '': S6.insert(0,crates[5])
        if s >= 7:
            if crates[6] != '': S7.insert(0,crates[6])
        if s >= 8:
            if crates[7] != '': S8.insert(0,crates[7])
        if s >= 9:
            if crates[8] != '': S9.insert(0,crates[8])

    if instructions == True:
        instruction = line.replace('move ','')
        instruction = instruction.replace(' from ','.')
        instruction = instruction.replace(' to ','.')
        number,start,end = instruction.split('.')
        number = int(number)
        start = int(start)
        end = int(end)
        
        i=0
        while i < number:
            if end == 1:
                if start == 1: S1.append(S1.pop())
                elif start == 2: S1.append(S2.pop())
                elif start == 3: S1.append(S3.pop())
                elif start == 4: S1.append(S4.pop())
                elif start == 5: S1.append(S5.pop())
                elif start == 6: S1.append(S6.pop())
                elif start == 7: S1.append(S7.pop())
                elif start == 8: S1.append(S8.pop())
                elif start == 9: S1.append(S9.pop())
            elif end == 2:
                if start == 1: S2.append(S1.pop())
                elif start == 2: S2.append(S2.pop())
                elif start == 3: S2.append(S3.pop())
                elif start == 4: S2.append(S4.pop())
                elif start == 5: S2.append(S5.pop())
                elif start == 6: S2.append(S6.pop())
                elif start == 7: S2.append(S7.pop())
                elif start == 8: S2.append(S8.pop())
                elif start == 9: S2.append(S9.pop())
            elif end == 3:
                if start == 1: S3.append(S1.pop())
                elif start == 2: S3.append(S2.pop())
                elif start == 3: S3.append(S3.pop())
                elif start == 4: S3.append(S4.pop())
                elif start == 5: S3.append(S5.pop())
                elif start == 6: S3.append(S6.pop())
                elif start == 7: S3.append(S7.pop())
                elif start == 8: S3.append(S8.pop())
                elif start == 9: S3.append(S9.pop())
            elif end == 4:
                if start == 1: S4.append(S1.pop())
                elif start == 2: S4.append(S2.pop())
                elif start == 3: S4.append(S3.pop())
                elif start == 4: S4.append(S4.pop())
                elif start == 5: S4.append(S5.pop())
                elif start == 6: S4.append(S6.pop())
                elif start == 7: S4.append(S7.pop())
                elif start == 8: S4.append(S8.pop())
                elif start == 9: S4.append(S9.pop())
            elif end == 5:
                if start == 1: S5.append(S1.pop())
                elif start == 2: S5.append(S2.pop())
                elif start == 3: S5.append(S3.pop())
                elif start == 4: S5.append(S4.pop())
                elif start == 5: S5.append(S5.pop())
                elif start == 6: S5.append(S6.pop())
                elif start == 7: S5.append(S7.pop())
                elif start == 8: S5.append(S8.pop())
                elif start == 9: S5.append(S9.pop())
            elif end == 6:
                if start == 1: S6.append(S1.pop())
                elif start == 2: S6.append(S2.pop())
                elif start == 3: S6.append(S3.pop())
                elif start == 4: S6.append(S4.pop())
                elif start == 5: S6.append(S5.pop())
                elif start == 6: S6.append(S6.pop())
                elif start == 7: S6.append(S7.pop())
                elif start == 8: S6.append(S8.pop())
                elif start == 9: S6.append(S9.pop())
            elif end == 7:
                if start == 1: S7.append(S1.pop())
                elif start == 2: S7.append(S2.pop())
                elif start == 3: S7.append(S3.pop())
                elif start == 4: S7.append(S4.pop())
                elif start == 5: S7.append(S5.pop())
                elif start == 6: S7.append(S6.pop())
                elif start == 7: S7.append(S7.pop())
                elif start == 8: S7.append(S8.pop())
                elif start == 9: S7.append(S9.pop())
            elif end == 8:
                if start == 1: S8.append(S1.pop())
                elif start == 2: S8.append(S2.pop())
                elif start == 3: S8.append(S3.pop())
                elif start == 4: S8.append(S4.pop())
                elif start == 5: S8.append(S5.pop())
                elif start == 6: S8.append(S6.pop())
                elif start == 7: S8.append(S7.pop())
                elif start == 8: S8.append(S8.pop())
                elif start == 9: S8.append(S9.pop())
            elif end == 9:
                if start == 1: S9.append(S1.pop())
                elif start == 2: S9.append(S2.pop())
                elif start == 3: S9.append(S3.pop())
                elif start == 4: S9.append(S4.pop())
                elif start == 5: S9.append(S5.pop())
                elif start == 6: S9.append(S6.pop())
                elif start == 7: S9.append(S7.pop())
                elif start == 8: S9.append(S8.pop())
                elif start == 9: S9.append(S9.pop())



            i = i + 1
if s == 3:
    topboxes = str(S1[-1]) + str(S2[-1]) + str(S3[-1])           
if s == 9:
    topboxes = str(S1[-1]) + str(S2[-1]) + str(S3[-1]) + str(S4[-1]) + str(S5[-1]) + str(S6[-1]) + str(S7[-1]) + str(S8[-1]) + str(S9[-1])
print('Topboxes are: ' + topboxes)    