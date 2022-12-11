import copy
f = open("Advent of Code Python/2022/Day_11_input.txt", "r")
# puzzle_input=("""Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1""")
puzzle_input = f.read()

puzzle_input=puzzle_input.split('\n\n')
for i in range(len(puzzle_input)):
    puzzle_input[i]=puzzle_input[i].split('\n')
# print(puzzle_input)

# puzzle_input = f.readlines()
# for i in range(len(puzzle_input)):
#     if puzzle_input[i][-1]=='\n':
#         puzzle_input[i]=puzzle_input[i][0:-1]
#print(puzzle_input)

def read_input(puzzle_input):
    input_dic={}
    for i in puzzle_input:
        monkey=i[0].split(' ')
        monkey = int(monkey[-1][:-1])
        items = i[1].split(': ')
        items = items[1].split(', ')
        for x in range (len(items)):
            items[x]=int(items[x])
        operation = i[2].split('new = ')
        operation = operation[1].split(' ')
        test=i[3].split('divisible by ')
        test = int(test[1])
        pass_condition=i[4].split('throw to monkey ')
        pass_condition=int(pass_condition[1])
        fail_condition=i[5].split('throw to monkey ')
        fail_condition=int(fail_condition[1])
        process=0
        input_dic[monkey]=[process, items, operation, test, pass_condition, fail_condition]
    return input_dic

input_dic1=read_input(puzzle_input)
input_dic2=copy.deepcopy(input_dic1)

def round_of_functions_part_1(input_dic):
    for i in range(len(input_dic)):
        for x in input_dic[i][1]:
            input_dic[i][0]+=1
            if input_dic[i][2][2]=='old':
                worry_level= x*x
            elif input_dic[i][2][1]=='+':
                worry_level=x+int(input_dic[i][2][2])
            elif input_dic[i][2][1]=='*':
                worry_level=x*int(input_dic[i][2][2])
            if worry_level%3==0:
                worry_level= worry_level//3
            elif worry_level%3==1:
                worry_level = (worry_level-1)//3
            else:
                worry_level = (worry_level-2)//3
            if worry_level%input_dic[i][3]==0:
                input_dic[input_dic[i][4]][1].append(int(worry_level))
                # print(worry_level, input_dic[i][4])
            else:
                input_dic[input_dic[i][5]][1].append(int(worry_level))
                # print(worry_level, input_dic[i][5])
        input_dic[i][1]=[]
        # for x in range(len(input_dic)):
        #     print(i, x, input_dic[x][1])
        
    return input_dic

def round_of_functions_part_2(input_dic):
    worry_mod=input_dic[0][3]*input_dic[1][3]*input_dic[2][3]*input_dic[3][3]*input_dic[4][3]*input_dic[5][3]*input_dic[6][3]*input_dic[7][3]
    for i in range(len(input_dic)):
        for x in input_dic[i][1]:
            input_dic[i][0]+=1
            if input_dic[i][2][2]=='old':
                worry_level= x*x
            elif input_dic[i][2][1]=='+':
                worry_level=x+int(input_dic[i][2][2])
            elif input_dic[i][2][1]=='*':
                worry_level=x*int(input_dic[i][2][2])
            worry_level=worry_level%worry_mod
            if worry_level%input_dic[i][3]==0:
                input_dic[input_dic[i][4]][1].append(int(worry_level))
                # print(worry_level, input_dic[i][4])
            else:
                input_dic[input_dic[i][5]][1].append(int(worry_level))
                
        input_dic[i][1]=[]        
    return input_dic

def part_function(rounds,dictionary, part):
    round=0
    monkey_business_list=[]
    for i in range(rounds):
        round+=1
        if part ==1:
            dictionary=round_of_functions_part_1(dictionary)
        elif part ==2:
            dictionary=round_of_functions_part_2(dictionary)
    for i in dictionary:
        monkey_business_list.append(dictionary[i][0])

    monkey_business=max(monkey_business_list)
    monkey_business_list.remove(monkey_business)
    part_answer=monkey_business*max(monkey_business_list)
    return part_answer

part_1_answer=part_function(20,input_dic1,1)
part_2_answer=part_function(10000,input_dic2,2)

print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:', part_2_answer)
