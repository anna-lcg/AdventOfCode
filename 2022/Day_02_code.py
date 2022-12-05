f = open("Advent of Code Python/2022/Day_02_input.txt", "r")
#puzzle_input=()
puzzle_input = f.read()
#print(puzzle_input)

part_1_outcomes = {
    'A X':4,
    'A Y':8,
    'A Z':3,
    'B X':1,
    'B Y':5,
    'B Z':9,
    'C X':7,
    'C Y':2,
    'C Z':6
}

part_2_outcomes = {
    'A X':3,
    'A Y':4,
    'A Z':8,
    'B X':1,
    'B Y':5,
    'B Z':9,
    'C X':2,
    'C Y':6,
    'C Z':7
}

puzzle_input_list=puzzle_input.split('\n')

part_1_score=0
part_2_score=0
for i in puzzle_input_list:
    part_1_score+=part_1_outcomes[i]
    part_2_score+=part_2_outcomes[i]

print('Part 1 Answer:', part_1_score)
print('Part 2 Answer:', part_2_score)