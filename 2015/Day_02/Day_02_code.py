f = open("anna-lcg/AdventOfCode/2015/Day_02/Day_02_input.txt", "r")
#puzzle_input=()
puzzle_input = f.read()
#print(puzzle_input)
puzzle_list = puzzle_input.split('\n')
# print(puzzle_list)


def paper_needed(dimensions):
    # print(dimensions)
    [length,width,height]= dimensions.split('x')
    length=int(length)
    width=int(width)
    height=int(height)
    surface_areas=[length*width, width*height, height*length]
    surface_area = min(surface_areas)
    for i in surface_areas:
        surface_area+= 2*i
    return(surface_area)

def ribbon_needed(dimensions):
    # print(dimensions)
    [length,width,height]= dimensions.split('x')
    length=int(length)
    width=int(width)
    height=int(height)
    dims=[length, width, height]
    dims.remove(max(dims))

    ribbon_length=2*(dims[0]+dims[1]) +length*width*height
    return(ribbon_length)

wrapping_paper=0
ribbon=0
for i in puzzle_list:
    #print(i)
    wrapping_paper+= paper_needed(i)
    ribbon+= ribbon_needed(i)

print('Part 1 Answer:', wrapping_paper)
print('Part 2 Answer:', ribbon)    
