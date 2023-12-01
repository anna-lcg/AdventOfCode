f = open('2023/2023 D01I.txt', "r")
puzzle_input = f.readlines()

#puzzle_input = ("""1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#treb7uchet""")

#print (puzzle_input)
#puzzle_input =puzzle_input.split("\n")

digitlist=['1','2','3','4','5','6','7','8','9','0','one','two','three','four','five','six','seven','eight','nine','zero']
digitdic={
    '1':1,
    'one':1,
    '2':2,
    'two':2,
    '3':3,
    'three':3,
    '4':4,
    'four':4,
    '5':5,
    'five':5,
    '6':6,
    'six':6,
    '7':7,
    'seven':7,
    '8':8,
    'eight':8,
    '9':9,
    'nine':9,
    '0':0,
    'zero':0,
}

def Part_1(calibration):
  individuals =[] 
  for i in calibration:
      this_line=[]
      for x in i:
          if x.isdigit():
              this_line.append(x)
  
      individuals.append(int(this_line[0])*10 + int(this_line[-1]))
  return (sum(individuals))

def Part_2(calibration):
  individuals=[]
  for i in calibration:
      digits=[]
      places=[]
      thisline2=0
      for x in digitlist:
          if i.find(x) != -1:
              if i.find(x) == i.rfind(x):
                  digits.append((x,(i.find(x))))
                  places.append(i.find(x))
              else:
                  digits.append((x,(i.find(x))))
                  digits.append((x,(i.rfind(x))))
                  places.append(i.find(x))
                  places.append(i.rfind(x))
      one=False
      if len(places)==1:
          one=True
      for x in digits:
          if x[1]== min(places):
              thisline2+=10*digitdic[x[0]]
              if one==True:
                  thisline2+=digitdic[x[0]]
          elif x[1]==max(places):
              thisline2+=digitdic[x[0]]
      
      individuals.append(thisline2)
  return(sum(individuals))

print ('The part 1 answer is', Part_1(puzzle_input))
print ('The part 2 answer is', Part_2(puzzle_input))
