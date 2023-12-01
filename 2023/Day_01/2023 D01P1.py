
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
for i in calibration:
    this_line=[]
    for x in i:
        #if x in digitlist:
        if x.isdigit():
            this_line.append(x)

    individuals.append(int(this_line[0])*10 + int(this_line[-1]))
print (sum(individuals))
