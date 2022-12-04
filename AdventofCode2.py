
strategy = open('Day2.txt').read()
strategybygame = strategy.split('\n')
win = 6
draw = 3
loss = 0

#Strategy 1
score = 0

for item in strategybygame:
    opp = item[0]
    me = item[2]
    
    if me == 'X':
        choice = 1
        if opp == 'A':
            result = draw
            score = score + choice + result
        elif opp == 'B':
            result = loss
            score = score + choice + result
        else:
            result = win
            score = score + choice + result

    elif me == 'Y':
        choice = 2
        if opp == 'B':
            result = draw
            score = score + choice + result
        elif opp == 'C':
            result = loss
            score = score + choice + result
        else:
            result = win
            score = score + choice + result

    elif me == 'Z':
        choice = 3
        if opp == 'C':
            result = draw
            score = score + choice + result
        elif opp == 'A':
            result = loss
            score = score + choice + result
        else:
            result = win
            score = score + choice + result

print('Score is: '+ str(score))

#Strategy 2
score = 0

for item in strategybygame:
    opp = item[0]
    me = item[2]
    
    if me == 'X': # need to lose
        if opp == 'A':
            choice = 3
            result = loss
            score = score + choice + result
        elif opp == 'B':
            choice = 1
            result = loss
            score = score + choice + result
        else:
            choice = 2
            result = loss
            score = score + choice + result

    elif me == 'Y': # need to draw
        if opp == 'B':
            choice = 2
            result = draw
            score = score + choice + result
        elif opp == 'C':
            choice = 3
            result = draw
            score = score + choice + result
        else:
            choice = 1
            result = draw
            score = score + choice + result

    elif me == 'Z': # need to win
        if opp == 'C':
            choice = 1
            result = win
            score = score + choice + result
        elif opp == 'A':
            choice = 2
            result = win
            score = score + choice + result
        else:
            choice = 3
            result = win
            score = score + choice + result

print('Real Score is: '+ str(score))