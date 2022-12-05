f = open("Advent of Code Python/2015/Day_03_input.txt", "r")
#puzzle_input=()
puzzle_input = f.read()
#print(puzzle_input)

def part1(puzzle_input):
    x=0
    y=0
    recipients = {(0,0):1}
    for i in puzzle_input:
        if i == '^':
            y+=1
        elif i =='v':
            y-=1
        elif i =='>':
            x+=1
        elif i =='<':
            x-=1
        else:
            print ('error', i)
        position = (x,y)
        if position in recipients:
            recipients[position]+=1
        else:
            recipients[position]=1
    return recipients


def part2(puzzle_input):
    Robot=True
    xRoboSanta=0
    xSanta=0
    yRoboSanta=0
    ySanta=0
    recipients = {(0,0):1}
    for i in puzzle_input:
        Robot =not Robot
        if i == '^':
            if Robot:
                yRoboSanta+=1
            else:
                ySanta+=1
        elif i =='v':
            if Robot:
                yRoboSanta-=1
            else:
                ySanta-=1
        elif i =='>':
            if Robot:
                xRoboSanta+=1
            else:
                xSanta+=1
        elif i =='<':
            if Robot:
                xRoboSanta-=1
            else:
                xSanta-=1
        else:
            print ('error', i)
        if Robot:
            position = (xRoboSanta,yRoboSanta)
        else:
            position = (xSanta,ySanta)
        if position in recipients:
            recipients[position]+=1
        else:
            recipients[position]=1
    return recipients


print('Part 1 Answer:', len(part1(puzzle_input)))
print('Part 2 Answer:', len(part2(puzzle_input)))
