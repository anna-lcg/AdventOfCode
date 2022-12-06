f = open("Advent of Code Python/2022/Day_01_input.txt", "r")
#puzzle_input=()
puzzle_input = f.read()
#print(puzzle_input)

def calories_in_bag(bag):
    calories = 0
    for i in bag:
        calories += int(i)
    return calories

separated = puzzle_input.split('\n')

elf=[]
elves=[]
for i in separated:
    if i == '':
        elves.append(elf)
        elf=[]
    else:
        elf.append(i)

calories_per_elf=[]
for i in elves:
    calories_per_elf.append(calories_in_bag(i))


calories_per_elf.sort(reverse=True)

top_three_elves= calories_per_elf[0]+calories_per_elf[1]+calories_per_elf[2]


print('Part 1 Answer:', calories_per_elf[0])
print('Part 2 Answer:', top_three_elves)
