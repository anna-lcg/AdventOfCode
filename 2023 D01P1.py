
f = open('2023/2023 D01I.txt', "r")
calibration = f.readlines()

#calibration = ("""1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#treb7uchet""")

#print (calibration)
#calibration =calibration.split("\n")
#print ("test")
#for i in calibration:
   # print ("this line is:", i)
individuals =[]
digitlist=[1,2,3,4,5,6,7,8,9,0,'one','two','three','four','five','six','seven','eight','nine','zero']
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
#print(digitdic['zero'])
for i in calibration:
    this_line=[]
    for x in i:
        #if x in digitlist:
        if x.isdigit():
            this_line.append(x)

    individuals.append(int(this_line[0])*10 + int(this_line[-1]))
print (sum(individuals))
