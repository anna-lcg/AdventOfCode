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

print('The part 1 answer is:', Part_1(puzzle_input))
