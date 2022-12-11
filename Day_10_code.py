f = open("Advent of Code Python/2022/Day_10_input.txt", "r")
# puzzle_input=("""addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\noop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop""")

puzzle_input = f.read()

puzzle_input=puzzle_input.split('\n')
# puzzle_input = f.readlines()
for i in range(len(puzzle_input)):
    puzzle_input[i]=(puzzle_input[i]).split(' ')
    if puzzle_input[i][-1]=='\n':
        puzzle_input[i][-1]=' '
        
# print(puzzle_input)

cycle_number=1
register=1
signal_dic={}
for i in puzzle_input:
    if i[0]=='noop':
        signal_dic[cycle_number]=register
        cycle_number+=1
    elif i[0]=='addx':
        signal_dic[cycle_number]=register
        cycle_number+=1
        signal_dic[cycle_number]=register
        register+=int(i[1])
        cycle_number+=1

wanted = [20,60,100,140,180,220]
part_1_answer=0
for i in wanted:
    part_1_answer+= i*signal_dic[i]


part_2_answer=''
for i in signal_dic:
    if (i%40 == signal_dic[i]) or (i%40==signal_dic[i]+1) or (i%40==signal_dic[i]+2):
        part_2_answer+='#'
    else:
        part_2_answer+='.'
    if i%40==0:
        part_2_answer+='\n '

print('Part 1 Answer:', part_1_answer)
print('Part 2 Answer:\n',part_2_answer)
