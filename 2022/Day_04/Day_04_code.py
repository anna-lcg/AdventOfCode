f = open("Advent of Code Python/2022/Day_04_input.txt", "r")
#puzzle_input=()
puzzle_input = f.read()
#print(puzzle_input)

puzzle_input_list=[]
puzzle_input_lines=puzzle_input.split('\n')
for i in puzzle_input_lines:
    x=i.split(',')
    y=[x[0].split('-'),x[1].split('-')]
    z=[int(y[0][0]),int(y[0][1]),int(y[1][0]),int(y[1][1])]
    puzzle_input_list.append(z)

# print(puzzle_input_list)
def encompase(pair):
    containment=0
    overlap=0
    if pair[0]== pair[2]:
        containment=1
    elif pair[1]==pair[3]:
        containment=1
    elif pair[0]>=pair[2]:
        if pair[1]<=pair[3]:
            containment=1
        elif pair[3]>=pair[0]:
            overlap=1
    elif pair[0]<=pair[2]:
        if pair[1]>=pair[3]:
            containment=1
        elif pair[1]>=pair[2]:
            overlap=1

    
    return (containment,overlap)

part_1_answer=0
part_2_answer=0
counter=0
for i in puzzle_input_list:
    # print(i)
    part_1_answer+=encompase(i)[0]
    part_2_answer+=encompase(i)[1]
    counter+=1
part_2_answer+=part_1_answer        

print(counter)
print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:', part_2_answer)
