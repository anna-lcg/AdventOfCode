f = open('2021/2021 D01I.txt', "r")
puzzle_input = f.readlines()

#input=("""199
#200
#208
#210
#200
#207
#240
#269
#260
#263""")

#depths=input.split("\n")
def Part_1(depths):
    differences=[]
    increase=0
    depthsoffset=depths[:]
    del(depthsoffset[0])
    for i in range (len(depthsoffset)):
        differences.append(int(depthsoffset[i])-int(depths[i]))
        #increase+=1
    for i in differences:
        if i >0:
            increase +=1
    return(increase)

def Part_2(depths1):
    groupings1=[]
    differences = []
    increase=0
    depths2=depths1[:]
    del(depths2[0])
    depths3=depths2[:]
    del(depths3[0])
    for i in range (len(depths3)):
        groupings1.append(int(depths1[i])+int(depths2[i])+int(depths3[i]))
        groupings2=groupings1[:]
        del(groupings2[0])
    for i in range (len(groupings2)):
        differences.append(groupings2[i]-groupings1[i])
    for i in differences:
        if i >0:
            increase +=1
    return(increase)


print('The part 1 answer is:', Part_1(puzzle_input))
print('The part 2 answer is:', Part_2(puzzle_input))