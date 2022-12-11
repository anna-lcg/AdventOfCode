import copy

f = open("Advent of Code Python/2022/Day_09_input.txt", "r")
#puzzle_input=("""""")
# puzzle_input = f.read()
puzzle_input = f.readlines()
for i in range(len(puzzle_input)):
    if puzzle_input[i][-1]=='\n':
        puzzle_input[i]=puzzle_input[i][0:-1]
puzzle_input_list=[]
for i in puzzle_input:
    puzzle_input_list.append(i.split(' '))
# print(puzzle_input_list)

def tail_movements(head,tail,log):

    # print('i')
    while (abs(tail[0]-head[0])>=2) or (abs(tail[1]-head[1])>=2):
        
        if abs(tail[0]-head[0])>=2:
            if head[0]-tail[0]>0:
                tail[0]+=1
                tail[1]=head[1]
            else:
                tail[0]-=1
                tail[1]=head[1]
        elif abs(tail[1]-head[1])>=2:
            if head[1]-tail[1]>0:
                tail[1]+=1
                tail[0]=head[0]
            else:
                tail[1]-=1
                tail[0]=head[0]
        if (tail[0],tail[1]) in log:
            log[(tail[0],tail[1])]+=1
        else:
            log[(tail[0],tail[1])]=1
        # print(head,tail)
    return (tail,log)

def tail_movement(i,head,tail,log,pos):
        # print('i')
    if (abs(tail[0]-head[0])==2) and (abs(tail[1]-head[1])==2):
        if head[0]-tail[0]>0:
            if head[1]-tail[1]>0:
                tail[1]+=1
                tail[0]+=1
            else:
                tail[1]-=1
                tail[0]+=1
        else:
            if head[1]-tail[1]>0:
                tail[1]+=1
                tail[0]-=1
            else:
                tail[1]-=1
                tail[0]-=1      
    elif abs(tail[0]-head[0])==2:
        if head[0]-tail[0]>0:
            tail[0]+=1
            tail[1]=head[1]
        else:
            tail[0]-=1
            tail[1]=head[1]
    elif abs(tail[1]-head[1])==2:
        if head[1]-tail[1]>0:
            tail[1]+=1
            tail[0]=head[0]
        else:
            tail[1]-=1
            tail[0]=head[0]
    elif (abs(tail[0]-head[0])>2) or (abs(tail[1]-head[1])>2):
        print (pos,i,head,tail)
    if (tail[0],tail[1]) in log:
        log[(tail[0],tail[1])]+=1
    else:
        log[(tail[0],tail[1])]=1
    # print(head,tail)
    return (tail,log)

def part_1(puzzle_input_list):
    tail_log={(0,0):1}

    head_position=[0,0]
    tail_position=[0,0]

    
        
    def follow_instructions(i,head,tail,log):
        if i[0]=='U':
            head[1]+= int (i[1])
        elif i[0]=='D':
            head[1]-= int (i[1])
        elif i[0]=='L':
            head[0]-= int (i[1])
        elif i[0]=='R':
            head[0]+= int (i[1])
        # print('    Head', head, 'Tail', tail)
        (tail,log)=tail_movements(head,tail,log)
        
        return (head,tail,log)

    for i in puzzle_input_list:
        (head_position,tail_position,tail_log)=follow_instructions(i,head_position,tail_position,tail_log)
        # print(i,'Head', head_position,'Tail', tail_position)
    return len(tail_log)

def part_2(puzzle_input_list):
    nine_log={(0,0):1}
    else_log={(0,0):1}
    head_position=[0,0]
    one_position=[0,0]
    two_position=[0,0]
    three_position=[0,0]
    four_position=[0,0]
    five_position=[0,0]
    six_position=[0,0]
    seven_position=[0,0]
    eight_position=[0,0]
    nine_position=[0,0]

    for i in puzzle_input_list:
        for x in range(int(i[1])):
            if i[0]=='U':
                head_position[1]+= 1
            elif i[0]=='D':
                head_position[1]-= 1
            elif i[0]=='L':
                head_position[0]-= 1
            elif i[0]=='R':
                head_position[0]+= 1
            (one_position,else_log)=tail_movement(i,head_position,one_position,else_log,'head')
            (two_position,else_log)=tail_movement(i,one_position,two_position,else_log,'one')
            (three_position,else_log)=tail_movement(i,two_position,three_position,else_log,'two')
            (four_position,else_log)=tail_movement(i,three_position,four_position,else_log,'three')
            (five_position,else_log)=tail_movement(i,four_position,five_position,else_log,'four')
            (six_position,else_log)=tail_movement(i,five_position,six_position,else_log,'five')
            (seven_position,else_log)=tail_movement(i,six_position,seven_position,else_log,'six')
            (eight_position,else_log)=tail_movement(i,seven_position,eight_position,else_log,'seven')
            (nine_position,nine_log)=tail_movement(i,eight_position,nine_position,nine_log,'eight')
            # print(head_position,one_position,two_position,three_position,four_position,five_position,six_position,seven_position,eight_position,nine_position)
    return nine_log
 

part_1_answer=part_1(puzzle_input_list)
part_2_answer=len(part_2(puzzle_input_list))

print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:', part_2_answer)
