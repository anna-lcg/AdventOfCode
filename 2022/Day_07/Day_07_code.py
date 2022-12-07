import copy

f = open("Advent of Code Python/2022/Day_07_input.txt", "r")
# puzzle_input = f.read()
puzzle_input = f.readlines()

# $ - command
# dir - directory
# number - file

def process_data(data):
    by_line = []
    command_line=[]
    # directory_list=[]
    inside=[]
    directories=[]
    gaaaaah=[]
    directory_dic={}
    list_status='not'
    for i in data:
        x=i[:-1]
        by_line.append(x.split(' '))
    for i in by_line:
        if i[0]=='$':
            if list_status=='start':
                direct_size=0
                internal_directories=copy.deepcopy(inside)
                for x in inside:
                    if isinstance(x,int):
                        direct_size+=x
                        internal_directories.remove(x)
                directory_dic['/'.join(gaaaaah)]=['/'.join(gaaaaah[:-1]),internal_directories,direct_size]
                inside=[]
                list_status='end'
            # print(i)
            if i[1] == 'cd':
                command_line.append(i[2])
                if i[2] == '/':
                    gaaaaah=['/']
                elif i[2]== '..':
                    del gaaaaah[-1]
                else:
                    gaaaaah.append(i[2])

            elif i[1]=='ls':
                list_status='start'
                directories.append('/'.join(gaaaaah))
                # directory_list.append(['/'.join(gaaaaah),inside])
                
        else:
            if i[0]=='dir':
                boop=copy.deepcopy(gaaaaah)
                boop.append(i[1])
                inside.append('/'.join(boop))
            else:
                inside.append(int(i[0]))

    if list_status=='start':
        direct_size=0
        internal_directories=copy.deepcopy(inside)
        for x in inside:
            if isinstance(x,int):
                direct_size+=x
                internal_directories.remove(x)
        directory_dic['/'.join(gaaaaah)]=['/'.join(gaaaaah[:-1]),internal_directories,direct_size]
        inside=[]
        list_status='end'
    return (command_line,directory_dic,directories)

(command_line,directory_dic,directories) = process_data(puzzle_input)



# for i in directory_dic
size_dic={}
reveresed_dictionary =dict(reversed(list(directory_dic.items())))

for i in reveresed_dictionary:
    # print(i,':',directory_dic[i])
    if directory_dic[i][1]==[]:
        size_dic[i]=directory_dic[i][2]
    else:
        size=directory_dic[i][2]
        for x in directory_dic[i][1]:
            size+=size_dic[x]
        size_dic[i]=size

part_1_answer=0
for i in size_dic:
    if size_dic[i]<=100000:
        part_1_answer+=size_dic[i]

def part_2_answer_function(size_of_computer, space_needed,size_dictionary):
    deletion_needed= space_needed+size_dictionary['/']-size_of_computer
    capable='/'
    for i in size_dictionary:
        if size_dictionary[i]>=deletion_needed:
            if size_dictionary[i]<=size_dictionary[capable]:
                capable=i

    return (capable)


part_2_answer=size_dic[part_2_answer_function(70000000,30000000,size_dic)]

print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:', part_2_answer)
