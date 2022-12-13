input_file = open('Day7.txt').read().split('\n')
#input_file = open('Day7E.txt').read().split('\n')
#input_file = open('Day7E2.txt').read().split('\n')

DIRECTORY_PATH = ['/']
directories = {}
#pathtodict = {}
listoffiles = []
listoffilesizes = []
listofpaths = {}
listofpaths[0] = '/'
DIR_NUM = 0
CURRENT_DIR = []
UPPER_DIRECTORY = '/'
directories['/'] = {}

for line in input_file:

    if line == '$ cd ..': #go up a directory
        if len(DIRECTORY_PATH) == 1:
            DIRECTORY_PATH = ['/']
            UPPER_DIRECTORY = '/'
            dirname = '/'
        else:
            del DIRECTORY_PATH[-1]
            dirname = DIRECTORY_PATH[-1]
            UPPER_DIRECTORY = DIRECTORY_PATH[-1]
            

    elif line == '$ cd /': #go back to home (/)
        DIRECTORY_PATH = ['/']
        UPPER_DIRECTORY = '/'

    elif line.startswith('$ cd '): #go to directory ____
        dirname = line.replace('$ cd ', '')
        DIRECTORY_PATH.append(dirname)
        UPPER_DIRECTORY = DIRECTORY_PATH[-1]

    elif line == '$ ls': #starts a list
        UPPER_DIRECTORY = DIRECTORY_PATH[-1]

    elif line.startswith('dir'): #is a directory
        dirname = line.replace('dir ','')

        DIRECTORY_PATH.append(dirname)
        if str(DIRECTORY_PATH) not in listofpaths:
            DIR_NUM = DIR_NUM + 1
            listofpaths[DIR_NUM] = DIRECTORY_PATH.copy()
        del DIRECTORY_PATH[-1]

        if len(DIRECTORY_PATH) == 1:
            if dirname not in directories[UPPER_DIRECTORY]: #and dirname != UPPER_DIRECTORY
                directories[UPPER_DIRECTORY][dirname] = {}
            
        elif len(DIRECTORY_PATH) == 2:
            if dirname not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][dirname] = {}

        elif len(DIRECTORY_PATH) == 3:
            if dirname not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][dirname] = {}

        elif len(DIRECTORY_PATH) == 4:
            if dirname not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][dirname] = {}

        elif len(DIRECTORY_PATH) == 5:
            if dirname not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][dirname] = {}

        elif len(DIRECTORY_PATH) == 6:
            if dirname not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][dirname] = {}

        elif len(DIRECTORY_PATH) == 7:
            if dirname not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][dirname] = {}

        elif len(DIRECTORY_PATH) == 8:
            if dirname not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][DIRECTORY_PATH[7]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][DIRECTORY_PATH[7]][dirname] = {}

        elif len(DIRECTORY_PATH) == 9:
            if dirname not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][DIRECTORY_PATH[7]][DIRECTORY_PATH[8]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][DIRECTORY_PATH[7]][DIRECTORY_PATH[8]][dirname] = {}   

        
        else:
            print('We must go deeper! ~dirs path lenth: ' + str(len(DIRECTORY_PATH)))

    else: #is a file
        size, file = line.split(' ')
        file = '(f)' + file
        size = int(size)

        if len(DIRECTORY_PATH) == 1:
            if file not in directories[UPPER_DIRECTORY]:
                directories[UPPER_DIRECTORY][file] = size
        
        elif len(DIRECTORY_PATH) == 2:
            if file not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][file] = size

        elif len(DIRECTORY_PATH) == 3:
            if file not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][file] = size

        elif len(DIRECTORY_PATH) == 4:
            if file not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][file] = size

        elif len(DIRECTORY_PATH) == 5:
            if file not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][file] = size

        elif len(DIRECTORY_PATH) == 6:
            if file not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][file] = size

        elif len(DIRECTORY_PATH) == 7:
            if file not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][file] = size

        elif len(DIRECTORY_PATH) == 8:
            if file not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][DIRECTORY_PATH[7]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][DIRECTORY_PATH[7]][file] = size

        elif len(DIRECTORY_PATH) == 9:
            if file not in directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][DIRECTORY_PATH[7]][DIRECTORY_PATH[8]]:
                directories[DIRECTORY_PATH[0]][DIRECTORY_PATH[1]][DIRECTORY_PATH[2]][DIRECTORY_PATH[3]][DIRECTORY_PATH[4]][DIRECTORY_PATH[5]][DIRECTORY_PATH[6]][DIRECTORY_PATH[7]][DIRECTORY_PATH[8]][file] = size
        
        else:
            print('We must go deeper! ~files path lenth: ' + str(len(DIRECTORY_PATH)))


dirsizes = {}

for keya in directories:
    a = keya
    dirnamea = str(a)

    if isinstance(directories[a], dict):
        if dirnamea not in dirsizes:
            dirsizes[dirnamea] = 0

        for keyb in directories[a]:
            b = keyb
            dirnameb = str(a) + '/' + str(b)

            if isinstance(directories[a][b], dict):
                if dirnameb not in dirsizes:
                    dirsizes[dirnameb] = 0

                for keyc in directories[a][b]:
                    c = keyc
                    dirnamec = str(a) + '/' + str(b) + '/' + str(c)

                    if isinstance(directories[a][b][c], dict):
                        if dirnamec not in dirsizes:
                            dirsizes[dirnamec] = 0

                        for keyd in directories[a][b][c]:
                            d = keyd
                            dirnamed = str(a) + '/' + str(b) + '/' + str(c) + '/' + str(d)

                            if isinstance(directories[a][b][c][d], dict):
                                if dirnamed not in dirsizes:
                                    dirsizes[dirnamed] = 0

                                for keye in directories[a][b][c][d]:
                                    e = keye
                                    dirnamee = str(a) + '/' + str(b) + '/' + str(c) + '/' + str(d) + '/' + str(e)

                                    if isinstance(directories[a][b][c][d][e], dict):
                                        if dirnamee not in dirsizes:
                                            dirsizes[dirnamee] = 0

                                        for keyf in directories[a][b][c][d][e]:
                                            f = keyf
                                            dirnamef = str(a) + '/' + str(b) + '/' + str(c) + '/' + str(d) + '/' + str(e) + '/' + str(f)

                                            if isinstance(directories[a][b][c][d][e][f], dict):
                                                if dirnamef not in dirsizes:
                                                    dirsizes[dirnamef] = 0

                                                for keyg in directories[a][b][c][d][e][f]:
                                                    g = keyg
                                                    dirnameg = str(a) + '/' + str(b) + '/' + str(c) + '/' + str(d) + '/' + str(e) + '/' + str(f) + '/' + str(g)

                                                    if isinstance(directories[a][b][c][d][e][f][g], dict):
                                                        if dirnameg not in dirsizes:
                                                            dirsizes[dirnameg] = 0

                                                        for keyh in directories[a][b][c][d][e][f][g]:
                                                            h = keyh
                                                            dirnameh = str(a) + '/' + str(b) + '/' + str(c) + '/' + str(d) + '/' + str(e) + '/' + str(f) + '/' + str(g)+ '/'  + str(h)

                                                            if isinstance(directories[a][b][c][d][e][f][g][h], dict):
                                                                if dirnameh not in dirsizes:
                                                                    dirsizes[dirnameh] = 0

                                                                for keyi in directories[a][b][c][d][e][f][g][h]:
                                                                    i = keyi
                                                                    dirnamei = str(a) + '/' + str(b) + '/' + str(c) + '/' + str(d) + '/' + str(e) + '/' + str(f) + '/' + str(g) + '/' + str(h) + '/'  + str(i)

                                                                    if isinstance(directories[a][b][c][d][e][f][g][h][i], dict):
                                                                        if dirnamei not in dirsizes:
                                                                            dirsizes[dirnamei] = 0

                                                                        for keyj in directories[a][b][c][d][e][f][g][h][i]:
                                                                            j = keyj
                                                                            dirnamej = str(a) + '/' + str(b) + '/' + str(c) + '/' + str(d) + '/' + str(e) + '/' + str(f) + '/' + str(g) + '/'  + str(h) + '/'  + str(i) + '/'  + str(j)

                                                                            if isinstance(directories[a][b][c][d][e][f][g][h][i][j], dict):
                                                                                print('Deeper needed')

                                                                            else:
                                                                                filesize = directories[a][b][c][d][e][f][g][h][i][j]
                                                                                dirsizes[dirnamei] = dirsizes[dirnamei] + filesize
                                                                                #and add to higher dirs
                                                                                dirsizes[dirnamea] = dirsizes[dirnamea] + filesize
                                                                                dirsizes[dirnameb] = dirsizes[dirnameb] + filesize
                                                                                dirsizes[dirnamec] = dirsizes[dirnamec] + filesize
                                                                                dirsizes[dirnamed] = dirsizes[dirnamed] + filesize
                                                                                dirsizes[dirnamee] = dirsizes[dirnamee] + filesize
                                                                                dirsizes[dirnamef] = dirsizes[dirnamef] + filesize
                                                                                dirsizes[dirnameg] = dirsizes[dirnameg] + filesize
                                                                                dirsizes[dirnameh] = dirsizes[dirnameh] + filesize

                                                                    else:
                                                                        filesize = directories[a][b][c][d][e][f][g][h][i]
                                                                        dirsizes[dirnameh] = dirsizes[dirnameh] + filesize
                                                                        #and add to higher dirs
                                                                        dirsizes[dirnamea] = dirsizes[dirnamea] + filesize
                                                                        dirsizes[dirnameb] = dirsizes[dirnameb] + filesize
                                                                        dirsizes[dirnamec] = dirsizes[dirnamec] + filesize
                                                                        dirsizes[dirnamed] = dirsizes[dirnamed] + filesize
                                                                        dirsizes[dirnamee] = dirsizes[dirnamee] + filesize
                                                                        dirsizes[dirnamef] = dirsizes[dirnamef] + filesize
                                                                        dirsizes[dirnameg] = dirsizes[dirnameg] + filesize

                                                            else:
                                                                filesize = directories[a][b][c][d][e][f][g][h]
                                                                dirsizes[dirnameg] = dirsizes[dirnameg] + filesize
                                                                #and add to higher dirs
                                                                dirsizes[dirnamea] = dirsizes[dirnamea] + filesize
                                                                dirsizes[dirnameb] = dirsizes[dirnameb] + filesize
                                                                dirsizes[dirnamec] = dirsizes[dirnamec] + filesize
                                                                dirsizes[dirnamed] = dirsizes[dirnamed] + filesize
                                                                dirsizes[dirnamee] = dirsizes[dirnamee] + filesize
                                                                dirsizes[dirnamef] = dirsizes[dirnamef] + filesize

                                                    else:
                                                        filesize = directories[a][b][c][d][e][f][g]
                                                        dirsizes[dirnamef] = dirsizes[dirnamef] + filesize
                                                        #and add to higher dirs
                                                        dirsizes[dirnamea] = dirsizes[dirnamea] + filesize
                                                        dirsizes[dirnameb] = dirsizes[dirnameb] + filesize
                                                        dirsizes[dirnamec] = dirsizes[dirnamec] + filesize
                                                        dirsizes[dirnamed] = dirsizes[dirnamed] + filesize
                                                        dirsizes[dirnamee] = dirsizes[dirnamee] + filesize

                                            else:
                                                filesize = directories[a][b][c][d][e][f]
                                                dirsizes[dirnamee] = dirsizes[dirnamee] + filesize
                                                #and add to higher dirs
                                                dirsizes[dirnamea] = dirsizes[dirnamea] + filesize
                                                dirsizes[dirnameb] = dirsizes[dirnameb] + filesize
                                                dirsizes[dirnamec] = dirsizes[dirnamec] + filesize
                                                dirsizes[dirnamed] = dirsizes[dirnamed] + filesize

                                    else:
                                        filesize = directories[a][b][c][d][e]
                                        dirsizes[dirnamed] = dirsizes[dirnamed] + filesize
                                        #and add to higher dirs
                                        dirsizes[dirnamea] = dirsizes[dirnamea] + filesize
                                        dirsizes[dirnameb] = dirsizes[dirnameb] + filesize
                                        dirsizes[dirnamec] = dirsizes[dirnamec] + filesize


                            else:
                                filesize = directories[a][b][c][d]
                                dirsizes[dirnamec] = dirsizes[dirnamec] + filesize
                                #and add to higher dirs
                                dirsizes[dirnamea] = dirsizes[dirnamea] + filesize
                                dirsizes[dirnameb] = dirsizes[dirnameb] + filesize

                    else:
                        filesize = directories[a][b][c]
                        dirsizes[dirnameb] = dirsizes[dirnameb] + filesize
                        #and add to higher dirs
                        dirsizes[dirnamea] = dirsizes[dirnamea] + filesize

            else:
                filesize = directories[a][b]
                dirsizes[dirnamea] = dirsizes[dirnamea] + filesize

    else:
        print('How did we end up here... same level as "/"')

sumoflargedirs = 0
for key in dirsizes:
    if dirsizes[key] <= 100000:
        sumoflargedirs = sumoflargedirs + dirsizes[key]

print('Total is: ' + str(sumoflargedirs))
#print(directories)

totspace = 70000000
usedspace = dirsizes['/']
freespace = totspace - usedspace
reqspace = 30000000
spacetofree = reqspace - freespace
print(str(spacetofree))
filetodel = '/'

for key in dirsizes:
    if dirsizes[key] > spacetofree and dirsizes[key] < dirsizes[filetodel]:
        filetodel = key
print(dirsizes[filetodel]) 