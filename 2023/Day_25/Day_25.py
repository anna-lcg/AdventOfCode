#f = open('2023/2023 D25I.txt', "r")
#puzzle_input = f.readlines()

puzzle_input = ("""jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr""")
puzzle_input =puzzle_input.split("\n")
#print (puzzle_input)

def createdictionary(components):
    compdict={}
    for component in components:
        words=component.split(': ')
        values = set(words[1].split(' '))
        compdict[words[0]]= values
    print(compdict)
    compdict2={}
    for component in compdict:
        for i in compdict[component]:
            #print(component, i, compdict[component])
            if i in compdict:
                holding = compdict[i]
                holding.add(component)
                compdict[i]=holding
                #print('ammended',i, compdict[i])
            elif i in compdict2:
                holding = compdict2[i]
                holding.add(component)
                compdict2[i]=holding 
                #print('ammended',i, compdict2[i])
            else:
                compdict2[i]={component}
                #print('ammended',i, compdict2[i])



    compdicts = {**compdict, **compdict2}
    print(compdicts.keys())
    for i in compdicts:
        print(i,compdicts[i])
    return(compdicts)
        
print(createdictionary(puzzle_input))

#def Part_1(components):

#def Part_2(calibration):

#print ('The part 1 answer is', Part_1(puzzle_input))
#print ('The part 2 answer is', Part_2(puzzle_input))
