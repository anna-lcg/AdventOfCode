
f = open('2023/2023 D01I.txt', "r")
calibration = f.readlines()

#calibration = ("""two1nine
#eightwothree
#abcone2threexyz
#xtwone3four
#4nineeightseven2
#zoneight234
#7pqrstsixteen""")

#print (calibration)
#calibration =calibration.split("\n")
#print ("test")
#for i in calibration:
   # print ("this line is:", i)
individuals =[]
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
    '0':0
}

for i in calibration:
    this_line=[]
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
    

    #for x in i:
        #if x in digitlist:
     #   if x.isdigit():
      #      this_line.append(x)
    #print (i)
    #print (digits)
    #print(thisline2)
    #print (this_line)
    individuals.append(thisline2)
    #individuals.append(int(this_line[0])*10 + int(this_line[-1]))
print (sum(individuals))
print(len(individuals))