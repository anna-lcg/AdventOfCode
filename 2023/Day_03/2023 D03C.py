f = open('2023/2023 D03I.txt', "r")
puzzle_input = f.readlines()

# puzzle_input = ("""467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""")
# puzzle_input =puzzle_input.split("\n")

#print (puzzle_input)


digitsanddecimals=['1','2','3','4','5','6','7','8','9','0','.','\n']
digits=['1','2','3','4','5','6','7','8','9','0']
def Part_1(engine):
    indicators=[]
    options=[]
    for i in range(len(engine)):
        for x in range(len(engine[i])):
            if engine[i][x] not in digitsanddecimals:
                indicators.append((i,x,engine[i][x]))
    for i in indicators:
        testcaseA = [(i[0]-1,i[1]-1),(i[0]-1,i[1]),(i[0]-1,i[1]+1),(i[0],i[1]+1),(i[0]+1,i[1]+1),(i[0]+1,i[1]),(i[0]+1,i[1]-1),(i[0],i[1]-1)]
        testcase=testcaseA[:]
        for x in testcaseA:
            if x[1]>=len(engine[i[0]]) or x[0]>=len(engine) or x[1]<0 or x[0]<0:
                testcase.remove(x)
        # print(i,testcase)
        for x in testcase:
            # print(x)
            if engine[x[0]][x[1]] in digits:
                options.append(x)
    options = list(set(options))
    options.sort()
    options2=[]
    for i in options:
        if i[1]> 0 and engine[i[0]][i[1]-1] in digits:
            options2.append((i[0],i[1]-1))
        options2.append(i)
        if i[1]<len(engine[i[0]]) and engine[i[0]][i[1]+1] in digits:
            options2.append((i[0],i[1]+1))
    options2 = list(set(options2))
    options2.sort()
    options3=[]
    for i in options2:
        if i[1]> 0 and engine[i[0]][i[1]-1] in digits:
            options3.append((i[0],i[1]-1))
        options3.append(i)
        if i[1]<len(engine[i[0]]) and engine[i[0]][i[1]+1] in digits:
            options3.append((i[0],i[1]+1))
    options3 = list(set(options3))
    options3.sort()
    thisone=''
    engineparts=[]
    for i in range(len(options3)-1):
        thisone+=engine[options3[i][0]][options3[i][1]]
        if options3[i][0]==options3[i+1][0] and options3[i][1]+1 == options3[i+1][1]:
            fillvalue=True
            if i==len(options3)-2:
                # print(thisone,options3[i])
                thisone+=engine[options3[i+1][0]][options3[i+1][1]]
                # print(thisone,options3[i])
                engineparts.append(int(thisone))
                thisone=[]
        else:
            # print(thisone,options3[i])
            engineparts.append(int(thisone))
            thisone=''
    # engineparts=[]
    # for i in range(len(numbers)):
    #     line=numbers[i][0][0]
    #     enginepart=''
    #     for x in numbers[i]:
    #         enginepart+=engine[x[0]][x[1]]
    #     engineparts.append(int(enginepart))  
    for i in engineparts:
        if i>=1000:
            print('i greater than 1000', i)
    # print (len(engineparts))
    # engineparts=list(set(engineparts))
    # engineparts.sort()
    # print (len(engineparts))

    return(sum(engineparts))


def Part_2(engine):
    indicators=[]
    perindicatoroptions=[]
    for i in range(len(engine)):
        for x in range(len(engine[i])):
            if engine[i][x] =='*':
                indicators.append((i,x))
    for star in indicators:
        options=[]
        testcaseA = [(star[0]-1,star[1]-1),(star[0]-1,star[1]),(star[0]-1,star[1]+1),(star[0],star[1]+1),(star[0]+1,star[1]+1),(star[0]+1,star[1]),(star[0]+1,star[1]-1),(star[0],star[1]-1)]
        testcase=testcaseA[:]
        for x in testcaseA:
            if x[1]>=len(engine[star[0]]) or x[0]>=len(engine) or x[1]<0 or x[0]<0:
                testcase.remove(x)
        # print(star,testcase)
        for x in testcase:
            # print(x)
            if engine[x[0]][x[1]] in digits:
                options.append(x)
        # print(star,options)
        options2=[]
        for i in options:
            options2.append(i)
            if i[1]> 0 and engine[i[0]][i[1]-1] in digits:
                options2.append((i[0],i[1]-1))
            # options2.append(i)
            if i[1]<len(engine[i[0]]) and engine[i[0]][i[1]+1] in digits:
                options2.append((i[0],i[1]+1))
        options2 = list(set(options2))
        options2.sort()
        # print(star,options2)
        options3=[]
        for i in options2:
            options3.append(i)
            if i[1]> 0 and engine[i[0]][i[1]-1] in digits:
                options3.append((i[0],i[1]-1))
            # options3.append(i)
            if i[1]<len(engine[i[0]]) and engine[i[0]][i[1]+1] in digits:
                options3.append((i[0],i[1]+1))
        options3 = list(set(options3))
        options3.sort()
        # print('star,options3',star,options3)
        thisone=''
        engineparts=[]
        for i in range(len(options3)):
            thisone+=engine[options3[i][0]][options3[i][1]]
            if i !=len(options3)-1:
                if options3[i][0]==options3[i+1][0] and options3[i][1]+1 == options3[i+1][1]:
                    fillvalue=True
                    if i==len(options3)-2:
                        # print(thisone,options3[i])
                        thisone+=engine[options3[i+1][0]][options3[i+1][1]]
                        # print(star,thisone,options3[i])
                        engineparts.append(int(thisone))
                        thisone=[]
                else:
                    # print(star,thisone,options3[i])
                    engineparts.append(int(thisone))
                    thisone=''
            if i== len(options3)-1:
                if options3[i][0]!=options3[i-1][0] or options3[i][1]-1 != options3[i-1][1]:
                    engineparts.append(int(engine[options3[i][0]][options3[i][1]]))
        # print((star,engineparts))
        perindicatoroptions.append((star,engineparts))
     
        engineparts=[]
    gearratio=[]
    # print(perindicatoroptions)
    for i in perindicatoroptions:
        # print(i)
        if len(i[1])==2:
            # print(i[1][0]*i[1][1])
            gearratio.append(i[1][0]*i[1][1])
        # else:
            # print(i)

    return(sum(gearratio))

print ('The part 1 answer is', Part_1(puzzle_input))
print ('The part 2 answer is', Part_2(puzzle_input))

#wrong answer - too low - 87285287
#wrong answer - too low - 118485
#correct answer - 87287096
