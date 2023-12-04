f = open('2023/2023 D04I.txt', "r")
puzzle_input = f.readlines()

puzzle_input = ("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""")
puzzle_input =puzzle_input.split("\n")
# print (puzzle_input)

def Part_1(cards):
    winnings=[]
    newcards=[]
    winningnumbers=[]
    
    for card in cards: 
        wnpc=[]
        card=card.replace('\n','')           
        percardwinnings=0
        newcard=card.split(':')
        newcard=[newcard[0],(newcard[1].split(' | '))]
        # print(newcard)
        newcard[1]=[newcard[1][0].split(' '),newcard[1][1].split(' ')]
        while '' in newcard[1][0]:
            newcard[1][0].remove('')
        while '' in newcard[1][1]:
            newcard[1][1].remove('')
        # print(newcard)
        for i in newcard[1][1]:
            if i in newcard[1][0]:
                wnpc.append(i)
                # print(i)
                if percardwinnings==0:
                    percardwinnings=1
                else:
                    percardwinnings*=2
        winnings.append(percardwinnings)
        newcards.append(newcard)
        winningnumbers.append(wnpc)
    return (sum(winnings),newcards,winningnumbers)



def Part_2(cards,winning):
    gamequant=[]
    # print(len(cards),len(winning))
    for i in cards:
        gamequant.append(1)
    for i in range (len(cards)):
        counter=1
        for x in winning[i]:
            gamequant[i+counter]+=gamequant[i]
            counter+=1    
    return (sum(gamequant))

print ('The part 1 answer is', Part_1(puzzle_input)[0])
print ('The part 2 answer is', Part_2((Part_1(puzzle_input)[1]),Part_1(puzzle_input)[2]))
