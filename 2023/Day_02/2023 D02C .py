f = open('2023/2023 D02I.txt', "r")
puzzle_input = f.readlines()

#puzzle_input = ("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""")

#print (puzzle_input)
#puzzle_input =puzzle_input.split("\n")

def Part_1(games,red_total,green_total,blue_total):
    valuedict={
        'red':red_total,
        'red\n':red_total,
        'blue':blue_total,
        'blue\n':blue_total,
        'green':green_total,
        'green\n':green_total
    }
    gameslist=[]
    possible=[]
    for i in games:
        thisgame=i.split(':')
        thisgamelist=[]
        thisgamelist.append(int((thisgame[0].split(' '))[1]))
        rounds=thisgame[1].split(';')
        roundslist=[]
        possibletest=True
        for x in rounds:
            eachround=x.split(',')
            eachroundlist=[]
            for y in eachround:
                eachroundlist.append([int(y.split(' ')[1]),y.split(' ')[2]])
            
                if int(y.split(' ')[1])> valuedict[y.split(' ')[2]]:
                    possibletest=False

            roundslist.append(eachroundlist)
        if possibletest:
            possible.append(int((thisgame[0].split(' '))[1]))
        roundslist.append(possibletest)


        thisgamelist.append(roundslist)
        gameslist.append(thisgamelist)


    return(gameslist,possible)  

def Part_2(games):
    power=0
    valuedict={
        'red':'red',
        'red\n':'red',
        'blue':'blue',
        'blue\n':'blue',
        'green':'green',
        'green\n':'green'
    }
    gameslist=[]
    for i in games:
        thisgame=i.split(':')
        thisgamelist=[]
        thisgamelist.append(int((thisgame[0].split(' '))[1]))
        rounds=thisgame[1].split(';')
        roundslist=[]
        possibletest=True
        red=0
        blue=0
        green=0
        for x in rounds:
            eachround=x.split(',')
            eachroundlist=[]
            for y in eachround:
                eachroundlist.append([int(y.split(' ')[1]),y.split(' ')[2]])
            
                if valuedict[y.split(' ')[2]] == 'red':
                    if int(y.split(' ')[1]) >= red:
                        red = int(y.split(' ')[1])
                elif valuedict[y.split(' ')[2]] == 'green':
                    if int(y.split(' ')[1]) >= green:
                        green = int(y.split(' ')[1])
                elif valuedict[y.split(' ')[2]] == 'blue':
                    if int(y.split(' ')[1]) >= blue:
                        blue = int(y.split(' ')[1])

            roundslist.append(eachroundlist)


        thisgamelist.append((roundslist,red,green,blue,red*green*blue))
        power+=(red*green*blue)
        gameslist.append(thisgamelist)


    return(gameslist,power)  

        
    




print ('The part 1 answer is', sum(Part_1(puzzle_input,12,13,14)[1]))
print ('The part 2 answer is', Part_2(puzzle_input)[1])
