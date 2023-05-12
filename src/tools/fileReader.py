"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""

def inputManager(e,expected):
    try:
        if(e in expected):
            return e
    except:
        print("ERROR: The input is different")
        print("File number 7")
    return "7"

def fileReader():

    #print("Enter the file to test:\n1) input1\n2) input2\n3) input3\n4) input4\n5) input5\n6) input6\n7) input7")
    #inputFile = str(inputManager((input()),("1","2","3","4","5","6","7")))

    fileR = open("./data/examen.up","r")
    fileR = fileR.read().split("\n")

    for i in fileR:
        print(i)
        print()
    #     lineCont += 1
    #     i = i.split(" ")
    #     if(lineCont == 1):
    #         maxX = int(i[0])
    #         maxY = int(i[1])
    #     elif(lineCont == 2):
    #         fps = int(i[0])
    #     elif(lineCont >=3):
    #         try:
    #             assert(int(i[0])<= maxX and int(i[1]) <= maxY)
    #             coordinates.append(coordinate(i[0],i[1],(lineCont - 2)))
    #         except AssertionError:
    #             print("ERROR: one of the coordinates is exceeding board Size")
    #             exit()
    #     # print(i + "-a")
    # return maxX, maxY, fps, coordinates
