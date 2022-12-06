f = open("anna-lcg/AdventOfCode/2022/Day_06/Day_06_input.txt", "r")
#puzzle_input=()
puzzle_input = f.read()
#print(puzzle_input)


def part_1(puzzle_input):
    moving_sequence=[]
    counter=0
    for i in puzzle_input:
        counter+=1
        if len(moving_sequence)<=2:
            moving_sequence.append(i)

        elif len(moving_sequence)==3:
            moving_sequence.append(i)
            if(len(set(moving_sequence)) == len(moving_sequence)):
                return counter
                break
            else:
                del moving_sequence[0]
   
def part_2(puzzle_input):
    moving_sequence=[]
    counter=0
    for i in puzzle_input:
        counter+=1
        if len(moving_sequence)<=12:
            moving_sequence.append(i)

        elif len(moving_sequence)==13:
            moving_sequence.append(i)
            if(len(set(moving_sequence)) == len(moving_sequence)):
                return counter
                break
            else:
                del moving_sequence[0]
    
part_1_answer=part_1(puzzle_input)
part_2_answer=part_2(puzzle_input)

print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:', part_2_answer)
