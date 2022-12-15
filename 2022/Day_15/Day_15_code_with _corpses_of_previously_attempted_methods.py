puzzle_input=[]
with open('Advent of Code Python/2022/Day_15_input.txt') as f:
    for line in f:
        puzzle_input.append(line.strip())

# f = open("Advent of Code Python/2022/Day_15_input.txt", "r")
# puzzle_input = f.read()

# puzzle_input="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split('\n')



# print(puzzle_input)

def manhattan_distance(a,b):
    distance = abs(a[0]-b[0])+abs(a[1]-b[1])
    return distance

sensor_dic ={}

for i in puzzle_input:
    [sensor,beacon]=i.split(':')
    [sensor_x,sensor_y]=sensor.split(', y=')
    [beacon_x,beacon_y]=beacon.split(', y=')
    [discard,sensor_x]=sensor_x.split('x=')
    [discard,beacon_x]=beacon_x.split('x=')
    sensor = (int(sensor_x),int(sensor_y))
    beacon = (int(beacon_x),int(beacon_y))
    sensor_dic[sensor]=[manhattan_distance(sensor,beacon),beacon]

# print (sensor_dic)
def no_beacons_in_row (sensor_dic, row):
    no_beacons =[]
    beacons=[]
    for sensor in sensor_dic:
        distance = sensor_dic[sensor][0]
        if sensor_dic[sensor][1][1] == row:
            beacons.append(sensor_dic[sensor][1][0])
        if ((sensor[1]>=row) and ((sensor[1]-distance)<=row)) or ((sensor[1]<=row) and ((sensor[1]+distance)>=row)):
            x_play = abs(abs(sensor[1]-row)-distance)
            left = sensor[0]-x_play
            right = sensor[0]+x_play +1
            for i in range(left,right):
                 no_beacons.append(i)
    beacons=set(beacons)
    no_beacons=set(no_beacons)
    for i in beacons:
        no_beacons.remove(i)
    
    return (no_beacons,beacons,min(no_beacons),max(no_beacons))

def merge_ranges(range_list):
    range_list=set(range_list)
    range_list=list(range_list)
    range_list.sort(key=lambda rng: rng[0])
    # print(range_list[0][1])
    new_list=[[range_list[0][0],range_list[0][1]]]
    for i in range(1,len(range_list)):
        if (range_list[i][0]>=new_list[-1][0]) and (range_list[i][0]<=new_list[-1][1]):
            if range_list[i][1]>new_list[-1][1]:
                new_list[-1][1]=range_list[i][1]
        elif range_list[i][0]>=new_list[-1][1]:
            new_list.append([range_list[i][0],range_list[i][1]])
    newer_list=[]
    for i in new_list:
        newer_list.append((i[0],i[1]))
    return newer_list


def no_beacons_in_row2 (sensor_dic,no_beacon_dic,highest):
    # no_beacons =[]
    # beacons=[]
    counter=0
    for sensor in sensor_dic:
        
        distance = sensor_dic[sensor][0]
        # print(sensor,distance)
        throw_up = sensor[1]-distance
        throw_down=sensor[1]+distance
        if throw_up<=0:
            throw_up=0
        if throw_down>=highest:
            throw_down=highest
        for row in range(throw_up,throw_down):
            # if counter%50000==0:
                # print('Sensor:', sensor,', Row:',row,', Counter:',counter)
            # counter+=1
            x_play = abs(abs(sensor[1]-row)-distance)
            left = sensor[0]-x_play
            if left <=0:
                left =0
            right = sensor[0]+x_play +1
            if right >=highest:
                right=highest+1
            if row not in no_beacon_dic:
                no_beacon_dic[row]=[(left,right)]
            else:
                no_beacon_dic[row].append((left,right))
                no_beacon_dic[row]=merge_ranges(no_beacon_dic[row])

        
    # beacons=set(beacons)
    
    # no_beacons=set(no_beacons)
    # # print(beacons)
    # # print(no_beacons)
    # for i in beacons:
    #     if i in no_beacons:
    #         no_beacons.remove(i)
    # no_beacon_dic[row]=no_beacons.union(beacons)
    # print(no_beacon_dic)
    return (no_beacon_dic)

def part_2(highest):
    possible_beacons=[]
    possible_transmissions =[]
    dic={}
    dic=no_beacons_in_row2(sensor_dic,dic,highest)
    print('part 2.1 done')
    # for i in dic:
    #     print(i)
    # print(min(dic))
    for y in range(min(dic),max(dic)):
        # print(y)
        # print(dic[y])
        if len(dic[y]) !=1:
            z=[0]
            for i in dic[y]:
                for a in range(i[0],i[1]):
                    if a == z[-1]+2:
                        x=z[-1]+1
                        # possible_beacons.append((x,y))
                        transmission = y+ (x*4000000)
                        return(transmission,dic)
                    else:
                        z.append(a)
                        

        # if len(z) != highest+1:
        #     print (y, dic[y])
        #     for x in range(highest+1):
        
        #         if x not in z:
        #             possible_beacons.append((x,y))
        #             transmission = y+ (x*4000000)
        #             return (transmission,dic)
        #             possible_transmissions.append(transmission)

    
    # for y in range(0,(highest+1)):
    #     print(y)
    #     [clear1,clear2,dic]=no_beacons_in_row2(sensor_dic,y,dic,highest)
    #     clear=clear1.union(clear2)
        
    #     print(len(clear))
    #     if len(clear) != highest+1:
    #         for x in range(highest+1):
    #             if x not in clear:
    #                 possible_beacons.append((x,y))
    #                 transmission = y+ (x*4000000)
    #                 return (transmission,dic)
    #                 possible_transmissions.append(transmission)
                    
   
    return ('what',dic)
#

part_1_answer =len(no_beacons_in_row(sensor_dic,2000000)[0])
# part_1_answer =len(no_beacons_in_row(sensor_dic,10)[0]) 
print('Part 1 Answer:', part_1_answer)

# part_2_answer=part_2(20)[0]
part_2_answer=part_2(4000000)[0]
print('Part 2 Answer:', part_2_answer)