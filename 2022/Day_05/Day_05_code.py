f = open("Advent of Code Python/2022/Day_05_input.txt", "r")
#puzzle_input=()
puzzle_input = f.read()
#print(puzzle_input)

stack_1_slice=slice(0,3)
stack_2_slice=slice(4,7)
stack_3_slice=slice(8,11)
stack_4_slice=slice(12,15)
stack_5_slice=slice(16,19)
stack_6_slice=slice(20,23)
stack_7_slice=slice(24,27)
stack_8_slice=slice(28,31)
stack_9_slice=slice(32,35)

puzzle_input_list = puzzle_input.split('\n')

original_stack_slice=slice(0,8)
instructions_slice = slice(10,-1)
original_stack=puzzle_input_list[original_stack_slice]
instructions_draft=puzzle_input_list[instructions_slice]
instructions_draft.append(puzzle_input_list[-1])

part_1_stack=[]
part_2_stack=[]
stack_draft=[[],[],[],[],[],[],[],[],[]]
for line in original_stack:
    stack_draft[0].append(line[stack_1_slice])
    stack_draft[1].append(line[stack_2_slice])
    stack_draft[2].append(line[stack_3_slice])
    stack_draft[3].append(line[stack_4_slice])
    stack_draft[4].append(line[stack_5_slice])
    stack_draft[5].append(line[stack_6_slice])
    stack_draft[6].append(line[stack_7_slice])
    stack_draft[7].append(line[stack_8_slice])
    stack_draft[8].append(line[stack_9_slice])

for line_draft in stack_draft:
    if '   ' in line_draft:
        line=[value for value in line_draft if value != "   "]
        part_1_stack.append(line)
        part_2_stack.append(line)
    else:
        part_1_stack.append(line_draft)
        part_2_stack.append(line_draft)
# print(part_1_stack)

def format_instructions(ins):
    formated_ins=[]
    for i in ins:
        formated= i.split(' ')
        formated_ins.append(formated)
    return formated_ins

instructions = format_instructions(instructions_draft)

def implement_part_1_instructions(ins,s):
    number_of_crates=int(ins[1])
    stack_output=s
    
    move_from=int(ins[3]) -1
    move_to=int(ins[5]) -1
    for i in range(number_of_crates):
        x = stack_output[move_from].pop(0)
        stack_output[move_to].insert(0,x)
        # stack_output[move_from].remove(x)
    return stack_output

def implement_part_2_instructions(ins,s):
    number_of_crates=int(ins[1])
    stack_output=s
    
    crates=slice(0,number_of_crates)
    move_from=int(ins[3]) -1
    move_to=int(ins[5]) -1

    x = stack_output[move_from][crates]
    for i in range(number_of_crates):
        z=x.pop(-1)
        stack_output[move_to].insert(0,z)
        stack_output[move_from].remove(z)
    

    return stack_output    

for i in instructions:
    # part_1_stack=implement_part_1_instructions(i,part_1_stack)
    part_2_stack=implement_part_2_instructions(i,part_2_stack)

part_1_answer= []
part_2_answer= []
# print(instructions[-1])
# print(len(part_1_stack[8]))
for i in part_1_stack:
    print(i)
    if len(i) >=1:
        # print(i[0][1])
        x=i[0][1]
        part_1_answer.append(x)
    else:
        part_1_answer.append('')

part_1_answer=''.join(part_1_answer)

for i in part_2_stack:
    print(i)
    if len(i) >=1:
        # print(i[0][1])
        x=i[0][1]
        part_2_answer.append(x)
    else:
        part_2_answer.append('')

part_2_answer=''.join(part_2_answer)


print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:', part_2_answer)
