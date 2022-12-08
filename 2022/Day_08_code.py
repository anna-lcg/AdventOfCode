f = open("Advent of Code Python/2022/Day_08_input.txt", "r")
# puzzle_input=("""30373
# 25512
# 65332
# 33549
# 35390""")
# puzzle_input=puzzle_input.split('\n')
# puzzle_input = f.read()
puzzle_input = f.readlines()
for i in range(len(puzzle_input)):
    puzzle_input[i]=puzzle_input[i][0:-1]


visible={}
puzzle_input_list=[]
for i in puzzle_input:
    line=[]
    for x in i:
        line.append(int(x))
    puzzle_input_list.append(line)
puzzle_input_list[-1].append(0)

for i in range (len(puzzle_input_list)):
    tallest=puzzle_input_list[i][0]
    for x in range(len(puzzle_input_list[i])):

        position=(x,i)
        visible[position]=(False, puzzle_input_list[i][x])
        #edges
        if x == 0:
            visible[position]=(True, puzzle_input_list[i][x])
        elif x == len(puzzle_input_list[i])-1:
            visible[position]=(True, puzzle_input_list[i][x])
        elif i == 0:
            visible[position]=(True, puzzle_input_list[i][x])
        elif i == len(puzzle_input_list)-1:
            visible[position]=(True, puzzle_input_list[i][x])

        # left to right
        if puzzle_input_list[i][x] > tallest:
            tallest=puzzle_input_list[i][x]
            visible[position]=(True, puzzle_input_list[i][x])
        
    backwards_puzzle_input = puzzle_input_list[i][::-1]

    tallest=backwards_puzzle_input[0]
    for x in range(len(puzzle_input_list[i])):
        x_new= len(puzzle_input_list[i])-1-x
        position=(x_new,i)

        # right to left
        if backwards_puzzle_input[x] > tallest:
            tallest=backwards_puzzle_input[x]
            visible[position]=(True, backwards_puzzle_input[x])

transposed=list(zip(*puzzle_input_list))

for i in range (len(transposed)):
    tallest=transposed[i][0]
    for x in range(len(transposed[i])):

        position=(i,x)

        # top to bottom
        if transposed[i][x] > tallest:
            tallest=transposed[i][x]
            visible[position]=(True, transposed[i][x])
    
    backwards_puzzle_input = transposed[i][::-1]

    tallest=backwards_puzzle_input[0]
    for x in range(len(transposed[i])):
        x_new= len(transposed[i])-1-x
        position=(i,x_new)

        # bottom to top
        if backwards_puzzle_input[x] > tallest:
            tallest=backwards_puzzle_input[x]
            visible[position]=(True, backwards_puzzle_input[x])

part_1_answer=0
visible_trees={}
for i in visible:
    if visible[i][0]==True:
        part_1_answer+=1
        visible_trees[i]=visible[i]

# print(visible_trees)

def sceneic_score(visible,position,grid_dimensions):
    #look up
    up=1
    comparison=position[1]-1
    compared_position=(position[0],comparison)
    while (comparison > 0) and (visible[compared_position][1]<visible[position][1]):
        up+=1
        comparison-=1
        compared_position=(position[0],comparison)
    # print('looked up')

    #look right
    right=1
    comparison=position[0]+1
    compared_position=(comparison,position[1])
    right_limit=grid_dimensions[0]-1
    while (comparison < right_limit) and (visible[compared_position][1]<visible[position][1]):
        right+=1
        comparison+=1
        compared_position=(comparison,position[1])
    # print('looked right')

    #look down
    down=1
    comparison=position[1]+1
    compared_position=(position[0],comparison)
    down_limit=grid_dimensions[0]-1
    while (comparison < down_limit) and (visible[compared_position][1]<visible[position][1]):
        down+=1
        # print(visible[compared_position][1], visible[position][1])
        comparison+=1
        compared_position=(position[0],comparison)
    # print('looked down')

    #look left
    left=1
    comparison=position[0]-1
    compared_position=(comparison,position[1])
    while (comparison > 0) and (visible[compared_position][1]<visible[position][1]):
        left+=1
        comparison-=1
        compared_position=(comparison,position[1])
    # print('looked left')

    score = up*right*down*left
    return score


part_2_answer=0
gd=(len(puzzle_input_list[0]),len(puzzle_input_list))
for i in visible_trees:
    score = sceneic_score(visible,i,gd)
    if score > part_2_answer:
        part_2_answer= score
        print(part_2_answer)


print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:', part_2_answer)