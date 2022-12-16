input_file = open('Day8.txt').read().split('\n')
#input_file = open('Day8E.txt').read().split('\n')

forest = {}
linenum = 0
visibletrees = 0

for line in input_file:
    forest[linenum] = list(line)
    linenum = linenum + 1

print('Forest size is:' + str(len(forest)) + ' x ' + (str(len(forest[0]))))

for i in forest:
    j = 0
    while j < len(forest[i]):
        if i == 0 or i == (len(forest)-1) or j == 0 or j == (len(forest[i])-1):
            visibletrees = visibletrees + 1

        elif (i > 0 and i < len(forest)) and (j > 0 and j < len(forest[i])):
            VisibleLHS = False
            VisibleRHS = False
            VisibleTopside = False
            VisibleBottomside = False

            #LHS tree shorter check
            x = 0
            LHSshortertree = 0
            while x < j:
                if forest[i][x] < forest[i][j]:
                    LHSshortertree = LHSshortertree + 1
                x = x + 1    
            if LHSshortertree == j: VisibleLHS = True

            #RHS tree shorter check
            x = j + 1
            RHSshortertree = 0
            while x < len(forest[0]):
                if forest[i][x] < forest[i][j]:
                    RHSshortertree = RHSshortertree + 1
                    treestocheck = len(forest[j]) - (j + 1)
                x = x + 1
            if RHSshortertree == treestocheck: VisibleRHS = True

            #Topside tree shorter check
            x = 0
            Topsideshortertree = 0
            while x < i:
                if forest[x][j] < forest[i][j]:
                    Topsideshortertree = Topsideshortertree + 1
                x = x + 1  
            if Topsideshortertree == i: VisibleTopside = True

            #Bottomside tree shorter check
            x = i + 1
            Bottomsideshortertree = 0
            while x < len(forest):
                if forest[x][j] < forest[i][j]:
                    Bottomsideshortertree = Bottomsideshortertree + 1
                    bottomtreestocheck = len(forest) - (i + 1)
                x = x + 1  
            if Bottomsideshortertree == bottomtreestocheck: VisibleBottomside = True

            #If visible from any direction
            if VisibleLHS or VisibleRHS or VisibleTopside or VisibleBottomside:
                visibletrees = visibletrees + 1

        j = j + 1

print('Visible Trees: ' + str(visibletrees))

currentbest = 0
for i in forest:
    j = 0
    while j < len(forest[i]):
        treesright = 0
        treesleft = 0
        treesabove = 0
        treesbelow = 0

        if i == 0 or i == (len(forest)-1) or j == 0 or j == (len(forest[i])-1):
            scenicscore = 0

        else: # do all checks
            #check right
            x = j + 1
            notblocked = True
            while x < len(forest[0]) and notblocked:
                if int(forest[i][x]) >= int(forest[i][j]):
                    treesright = treesright + 1
                    notblocked = False
                elif int(forest[i][x]) < int(forest[i][j]):
                    treesright = treesright + 1
                
                x = x + 1   
            #check left
            x = j - 1
            notblocked = True
            while x >= 0 and notblocked:
                if int(forest[i][x]) >= int(forest[i][j]):
                    treesleft = treesleft + 1
                    notblocked = False
                elif int(forest[i][x]) < int(forest[i][j]):
                    treesleft = treesleft + 1
                x = x - 1  
            #check above
            x = i - 1
            notblocked = True
            while x >= 0 and notblocked:
                if int(forest[x][j]) >= int(forest[i][j]):
                    treesabove = treesabove + 1
                    notblocked = False
                elif int(forest[x][j]) < int(forest[i][j]):
                    treesabove = treesabove + 1
                
                x = x - 1
            #check below
            x = i + 1
            notblocked = True
            while x < len(forest) and notblocked:
                if int(forest[x][j]) >= int(forest[i][j]):
                    treesbelow = treesbelow + 1
                    notblocked = False
                elif int(forest[x][j]) < int(forest[i][j]):
                    treesbelow = treesbelow + 1
                
                x = x + 1
            scenicscore = treesabove * treesbelow * treesleft * treesright

        
        if scenicscore > currentbest:
            currentbest = scenicscore

        j = j + 1

print('Best Scenic Score: ' + str(currentbest))