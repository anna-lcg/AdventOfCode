textinputstr = """3   4
4   3
2   5
1   3
3   9
3   3"""
textinputstr=textinputstr.split("\n")

f = open('Day01I.txt', "r")
puzzle_input = f.readlines()

textinput=[]
for pair in textinputstr:
    textinput.append(pair.split("   "))

def Process1(source):
    #print(source)
    HisLocA=[]
    HisLocB=[]
    for pair in source:
        HisLocA.append(int(pair[0]))
        HisLocB.append(int(pair[1]))
    
    #print(HisLocA)
    HisLocA.sort()
    HisLocB.sort()
    #print(HisLocA)
    return((HisLocA,HisLocB))



def Part1(SourceA,SourceB):
    differencelist=[]
    for itemindex in range(len(SourceA)):
        #print(itemindex)
        differencelist.append(abs(SourceA[itemindex]-SourceB[itemindex]))

    #print (differencelist)
    return (sum(differencelist))


def Part2(SourceA,SourceB):
    multlist=[]
    for itemA in SourceA:
        quant=0
        if itemA in SourceB:
            for itemB in SourceB:
                if itemB==itemA:
                    quant+=1
        multlist.append(itemA*quant)
    return(sum(multlist))
                


processedinput=Process1(textinput)
#print(processedinput)
print(Part1(processedinput[0],processedinput[1]))
print(Part2(processedinput[0],processedinput[1]))
