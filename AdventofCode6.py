inputfile = open('Day6.txt').read()
chars = {0:'', 1:'', 2:'', 3:''}
messagechars = {i:'' for i in range(14)}

i = 0
j = 0
processed = 0
packetfound = False
messagefound = False

for character in inputfile:
    processed = processed + 1
    chars[i] = character
    messagechars[j] = character
    
    if chars[0] != '' and chars[1] != '' and chars[2] != '' and chars[3] != '' and packetfound == False:
        
        refchars = {}

        for key, value in chars.items():
            refchars.setdefault(value, set()).add(key)
            result = [key for key, values in refchars.items() if len(values) > 1]
            
        if result == []:
            print('Packet Marker Found. Number of chars processed: ' + str(processed))
            packetfound = True
    

    if '' not in chars.values() and messagefound == False:
        
        refchars = {}

        for key, value in messagechars.items():
            refchars.setdefault(value, set()).add(key)
            result = [key for key, values in refchars.items() if len(values) > 1]
            
        if result == []:
            print('Message Marker Found. Number of chars processed: ' + str(processed))
            messagefound = True


    if i == 3:
        i = 0
    else:
        i = i + 1

    if j == 13:
        j = 0
    else:
        j = j + 1