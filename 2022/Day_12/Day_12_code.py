import copy

f = open("Advent of Code Python/2022/Day_12_input.txt", "r")
puzzle_input = f.readlines()

# puzzle_input=("""Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi""")
# puzzle_input=puzzle_input.split('\n')

# puzzle_input = f.read()

for i in range(len(puzzle_input)):
    if puzzle_input[i][-1]=='\n':
        puzzle_input[i]=puzzle_input[i][0:-1]

potential_starts=[]
geo_map={}
x_limit=len(puzzle_input[0])
y_limit=len(puzzle_input)
for i in range (y_limit):
    for x in range (x_limit):
        if puzzle_input[i][x] == 'S':
            geo_map[(x,i)]= 1
            original_start = (x,i)
            potential_starts.append((x,i))
        elif puzzle_input[i][x] == 'E':
            geo_map[(x,i)]= puzzle_input[i][x]
            end = (x,i)
        elif puzzle_input[i][x] == 'a':
            potential_starts.append((x,i))
            geo_map[(x,i)]=ord(puzzle_input[i][x])-96
        else:
            geo_map[(x,i)]=ord(puzzle_input[i][x])-96


x_limit-=1
y_limit-=1

def add_to_path (old,new,pathways):
    for i in range(len(pathways)):
        if pathways[i][-1]==old:
            path=copy.deepcopy(pathways[i])
            path.append(new)
            pathways.append(path)
            return pathways
    return pathways

def process(a,elevation_map,coordinates,options):
    if (a==end) and (elevation_map[coordinates]>=25):
        options[0].append(a)
        options[1].append(coordinates)
    elif a==end:
        nearby = True
    elif elevation_map[a]<= elevation_map[coordinates]+1:
        options[0].append(a)
        options[1].append(coordinates)
    return options

def part_1(start,bad_routes):
    routes=[[start]]
    
    def progressive_movement(elevation_map, positions, movement_options, paths):
        options = [[],[]]
        next_options ={}

        for coordinates in positions:
            if coordinates[0]!=0:
                a = (coordinates[0]-1,coordinates[1])
                options=process(a,elevation_map,coordinates,options)
            if coordinates[1]!=0:
                a = (coordinates[0],coordinates[1]-1)
                options=process(a,elevation_map,coordinates,options)
            if coordinates[0]!=x_limit:
                a = (coordinates[0]+1,coordinates[1])
                options=process(a,elevation_map,coordinates,options)
            if coordinates[1]!=y_limit:
                a = (coordinates[0],coordinates[1]+1)
                options=process(a,elevation_map,coordinates,options)
        for x in range(len(options[0])):
            i = options[0][x]
            y = options[1][x]
            if i not in movement_options:
                movement_options[i]=elevation_map[i]
                next_options[i]=elevation_map[i]
                paths=add_to_path(y,i,paths)
        return (movement_options, next_options, paths)

    mov_options={}
    start_list=[start]
    (mov_options,next_positions,routes)=progressive_movement(geo_map,start_list, mov_options,routes)
    found=True
    while end not in next_positions:
        (mov_options,next_positions, routes)=progressive_movement(geo_map,next_positions, mov_options, routes)
        if (next_positions=={}) and (end not in mov_options):
            found=False
            for x in routes[-1]:
                if x not in bad_routes:
                    bad_routes.append(x)
            part_1_answer=700
            return (part_1_answer,bad_routes)
    for i in routes:
        if i[-1]==end:
            part_1_answer=len(i)-1
    return (part_1_answer,bad_routes)

def part_2():
    steps=[]
    bad_routes=[]
    print(len(potential_starts))
    for i in potential_starts:
        # print(bad_routes)
        if i in bad_routes:
            print(i, 'Skipped')
        else:
            # print(i)
            (x,bad_routes)=part_1(i,bad_routes)
            steps.append(x)
    part_2_answer=min(steps)
    return part_2_answer

bad_routes=[]

part_1_answer=part_1(original_start,bad_routes)[0]
print('Part 1 Answer:', part_1_answer)

part_2_answer=part_2()
print('Part 2 Answer:', part_2_answer)
