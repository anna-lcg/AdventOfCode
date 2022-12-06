# f = open("Advent of Code Python/2015/Day_04_input.txt", "r")
puzzle_input=("iwrupvqb")
# puzzle_input = f.read()
#print(puzzle_input)

# print('Part 1 Answer:', len(part1(puzzle_input)))
# print('Part 2 Answer:', len(part2(puzzle_input)))

# Python 3 code to demonstrate the 
# working of MD5 (byte - byte)
import hashlib
# encoding GeeksforGeeks using md5 hash
# function 
# result = hashlib.md5(b'abcdef609043')

def first_5_digits(str2hash):
    # str2hash= "abcdef609043"
    result = hashlib.md5(str2hash.encode())
    # printing the equivalent byte value.
    # print("The byte equivalent of hash is : ", end ="")
    # print(result.digest())
    print (result)
    result = str(result)
    (a,hashresult) = result.split('@ 0x')
    print(hashresult)
    hashresult= hashresult.strip('>')
    return hashresult[0:5]

not_found= True
answer='0'
while not_found:
    pieces = (puzzle_input,answer)
    testcase = ''.join(pieces)
    print(testcase)
    if first_5_digits(testcase)== '00000':
        print(answer)
        not_found=False
    else:
        answer+=1
