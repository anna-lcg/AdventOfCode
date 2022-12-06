f = open("Advent of Code Python/2022/Day_03_input.txt", "r")
#puzzle_input=()
puzzle_input = f.read()
#print(puzzle_input)
rucksacks=puzzle_input.split('\n')
rucksack_compartments=[]
part_1_answer=0
values={
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
    'A':27,
    'B':28,
    'C':29,
    'D':30,
    'E':31,
    'F':32,
    'G':33,
    'H':34,
    'I':35,
    'J':36,
    'K':37,
    'L':38,
    'M':39,
    'N':40,
    'O':41,
    'P':42,
    'Q':43,
    'R':44,
    'S':45,
    'T':46,
    'U':47,
    'V':48,
    'W':49,
    'X':50,
    'Y':51,
    'Z':52
}
for i in rucksacks:
    x=len(i)
    compartment1=slice(0,x//2)
    compartment2=slice(x//2,x)
    rucksack_compartments.append([i[compartment1],i[compartment2]])
    
    for x in i[compartment1]:
        if x in i[compartment2]:
            doubleup=x
    part_1_answer+=values[doubleup]

counter=1
badge_check=[]
badge=0
part_2_answer=0
for i in rucksacks:
    if counter%3==0:
        part_2_answer+=values[badge]
        badge_check=[]
    elif counter%3==1:
        for x in i:
            if x in rucksacks[counter]:
                badge_check.append(x)
    elif counter%3==2:
        for x in badge_check:
            if x in rucksacks[counter]:
                badge=x
                # print(badge)
    counter+=1

        

# print(rucksack_compartments)


print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:', part_2_answer)
