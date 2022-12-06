f = open("Advent of Code Python/2022/Day_05_input.txt", "r")
puzzle_input = f.readlines()

break_line=puzzle_input.index('\n')
original_stack=puzzle_input[0:break_line-1]
instructions_draft=puzzle_input[break_line+1:]

part_1_stack=[]
stack_draft=[[],[],[],[],[],[],[],[],[]]
for line in original_stack:
    y=0
    for i in range(1,35,4):
        stack_draft[y].append(line[i])
        y+=1

for line_draft in stack_draft:
    line=line_draft
    while line[0]==' ':
        del line[0]
    part_1_stack.append(line)
# part_2_stack=list(part_1_stack)


def format_instructions(ins):
    formated_ins=[]
    for i in ins:
        formated= i.split(' ')
        formated_ins.append(formated)
    return formated_ins

instructions = format_instructions(instructions_draft)

def implement_part_1_instructions(ins,s):
    number_of_crates=int(ins[1])
    move_from=int(ins[3]) -1
    move_to=int(ins[5]) -1

    stack_output=s

    crate_load=stack_output[move_from][0:number_of_crates]
    # crate_load.reverse()
    for i in crate_load:
        stack_output[move_to].insert(0,i)
    stack_output[move_from]=stack_output[move_from][number_of_crates:]

    return stack_output

def implement_part_2_instructions(ins,s):
    number_of_crates=int(ins[1])
    move_from=int(ins[3]) -1
    move_to=int(ins[5]) -1

    stack_output=s

    crate_load=stack_output[move_from][0:number_of_crates]
    crate_load.reverse()
    for i in crate_load:
        stack_output[move_to].insert(0,i)
    stack_output[move_from]=stack_output[move_from][number_of_crates:]

    return stack_output


for i in instructions:
    part_1_stack=implement_part_1_instructions(i,part_1_stack)


#----------------------------------
f = open("Advent of Code Python/2022/Day_05_input.txt", "r")
puzzle_input = f.readlines()

break_line=puzzle_input.index('\n')
original_stack=puzzle_input[0:break_line-1]
instructions_draft=puzzle_input[break_line+1:]

stack_draft=[[],[],[],[],[],[],[],[],[]]
part_2_stack=[]
for line in original_stack:
    y=0
    for i in range(1,35,4):
        stack_draft[y].append(line[i])
        y+=1

for line_draft in stack_draft:
    line=line_draft
    while line[0]==' ':
        del line[0]
    part_2_stack.append(line)
#--------------------------
for i in instructions:
    part_2_stack=implement_part_2_instructions(i,part_2_stack)



def format_for_answer(stack):
    answer=[]
    count=0
    # print(stack)
    for i in stack:
        # print(count, i)
        if len(i) >=1:
            x=i[0]
            answer.append(x)
        else:
            answer.append('')
        count+=1
    # print('answer:\n', answer)
    answer=''.join(answer)
    return answer

part_1_answer=format_for_answer(part_1_stack)
part_2_answer=format_for_answer(part_2_stack)

print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:', part_2_answer)