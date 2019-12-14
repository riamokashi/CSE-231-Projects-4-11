###########################################
#
# COMPUTER PROJECT #5

# Files

#   Create a loop for the options  
  
#    make multiple functions

#       check if valid  

#       read face data

#       read vertex data

#       calculate cross product

#       calculate normal 

#       check to see if the shapes are next to each other  

##################################################

#Retain these import statements  
import math

def display_options():
    ''' This function displayes the menu of options'''
    
    menu = '''\nPlease choose an option below:
        1- display the information of the first 5 faces
        2- compute face normal
        3- compute face area
        4- check two faces connectivity
        5- use another file
        6- exit
       '''
       
    print(menu)

        

def open_file():
    '''Insert docstring here.'''
    file_input = input("Please select a file. ")
    try:
        fp = open(file_input, "r")
        return fp
    except ValueError:
        print("Error. please select a valid file.")
        open_file()
        

           
def check_valid(fp,index,shape):
    '''Check if the index is valid'''
    print("Filename: " + fp.name)
    fp.seek(0)
    line = fp.readline() # OFF
    #print("line:",line)
    #print(fp.tell())
    
    line = fp.readline() # Face Vertex Edge
    #print("line:",line)
    #print(fp.tell())
    
    numberOfValues = line.split() # Third line
    #print(numberOfValues)
    #print(fp.tell())
    
    if shape == 'vertex':
        print("##########vertex#########")
        print(" ")
        print("index"+" "+"output")
        numberOfValuesInt = (int(numberOfValues[0]))
        #print(numberOfValuesInt)
        if float(index) >= 0 and float(index) < numberOfValuesInt:
            print(index+"   "+"TRUE")
            return True 
        else:
             print(index+"   "+"FALSE")
             return False
    if shape == 'face':
        print("##########face#########")
        print(" ")
        print("index"+" "+"output")
        numberOfValuesInt = (int(numberOfValues[1]))
        #print(numberOfValuesInt)
        
        if str(index).isdigit():           
            if int(index) >= 0 and int(index) < numberOfValuesInt:
                print(index+"   "+"TRUE")
                return True 
            else:
                print(index+"   "+"FALSE")
                return False
        else:
            return False 
    
    
    
def read_face_data(fp, index):
    '''Returns face data'''
    reader = fp
    for line in fp
#    fp.seek(0)
#    line = fp.readline() # OFF
#    print("line:",line)
#    print(fp.tell())
#    
#    line = fp.readline() # Face Vertex Edge
#    print("line:",line)
#    print(fp.tell())
#
#    print("Filename: " + fp.name)
#    print("This is the line " + str(fp.tell()))
#    line = line.split()
#    i = 0
#    while (line[0] != '3'):
#        line = fp.readline() # skip all vertex lines
#        line = line.split()
#        i = i + 1
#        print(line)
#        print(i)
#    j = i
#    while True:
#        if j == (i + index):  
#            faceLine = fp.readline() # string of face info
#            print(faceLine)
#            faceStr = faceLine.split()
#            faceInfo1 = int(faceStr[1])
#            faceInfo2 = int(faceStr[2])
#            faceInfo3 = int(faceStr[3])     
#            print("face" + str(index) + " info: " + str(faceStr))
#            return faceInfo1, faceInfo2, faceInfo3
#            False
#        else:
#            faceLine = fp.readline()
#            j = j + 1

def read_vertex_data(fp, index):
    '''Insert docstring here.'''
    fp.seek(0) # move to the beginning of the file -- necessary for multiple calls to this function
    line = fp.readline() # OFF
    #print("line:",line)
    #print(fp.tell())
    
    line = fp.readline() # Face Vertex Edge
    #print("line:",line)
    #print(fp.tell())
    
    line = line.split()
    print("Filename: " + fp.name)
    lineSkip = fp.tell()
    vertexLinePos = index + lineSkip
    if line[0] != '3':
        fp.seek(vertexLinePos)
        vertexLine = fp.readline()
        vertexStr = vertexLine.split()
        vertexInfo1 = float(vertexStr[0])
        vertexInfo2 = float(vertexStr[1])
        vertexInfo3 = float(vertexStr[2])
        print("student vertex " + str(vertexLinePos) + " info: " + str(vertexStr))
        return vertexInfo1, vertexInfo2, vertexInfo3
    else:
        fp.seek(lineSkip)

        
def compute_cross(v1,v2,v3,w1,w2,w3):
    '''Find the cross product of 2 vectors'''
    vList = [v1, v2, v3]
    wList = [w1, w2, w3]
    z1 = (v2*w3) - (v3*w2)
    z2 = (v3*w1) - (v1*w3)
    z3 = (v1*w2) - (v2*w1)
    z1Round = round(z1, 5)
    z2Round = round(z2, 5)
    z3Round = round(z3, 5)
    print("v= " + str(vList))
    print("w= " + str(wList))
    print("output: " + str(z1Round) + str(z2Round) + str(z3Round))
    return z1Round, z2Round, z3Round

def compute_distance(x1,y1,z1,x2,y2,z2):
    '''Finding the distance'''
    vList = [x1, y1, z1]
    wList = [x2, y2, z2]
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    print("v= " + str(vList))
    print("w= " + str(wList))
    print("output: " + str(distance))
    return round(distance, 2)
    
    
def compute_face_normal(fp, face_index):
    '''Computing the normal'''
    a, b, c = read_face_data(fp, face_index) 
    # the 3 vertices that make up that face : a, b, c
    a1, a2, a3 = read_vertex_data(fp, a)
    b1, b2, b3 = read_vertex_data(fp, b)
    c1, c2, c3 = read_vertex_data(fp, c)
    # x,y,z the coord of each vertex
  
   #when a is constant  
    side1 = ((b1-a1), (b2-a2), (b3-a3))
    side2= ((c1-a1), (c2-a2), (c3-a3))
    crossA1, crossA2, crossA3 = compute_cross(side1[0], side1[1], side1[2], side2[0], side2[1], side2[2])
    
    # #when b is constant 
    # side1 = ((a1-b1), (a2-b2), (a3-b3))
    # side2= ((c1-b1), (c2-b2), (c3-b3))
    # crossB1, crossB2, crossB3 = compute_cross(side1[0], side1[1], side1[2], side2[0], side2[1], side2[2])
    # # when c is constant 
    #  side1 = ((b1-c1), (b2-c2), (b3-c3))
    # side2= ((a1-c1), (a2-c2), (a3-c3))
    # crossC1, crossC2, crossC3 = compute_cross(side1[0], side1[1], side1[2], side2[0], side2[1], side2[2])
    # print cross at each index 
    print("Filename: " + fp.name)
    print("Index " + str(a) + " : " + str(crossA1) + ", " + str(crossA2) + ", " + str(crossA3))
    # print("Index " + str(b) + " : " + str(crossB1) + ", " + str(crossB2) + ", " + str(crossB3))
    # print("Index " + str(c) + " : " + str(crossC1) + ", " + str(crossC2) + ", " + str(crossC3))
    return round(crossA1,5), round(crossA2,5), round(crossA3,5)
    
    
def compute_face_area(fp, face_index):
    '''Insert docstring here.'''
    a, b, c = read_face_data(fp, face_index) 
    # the 3 vertices that make up that face : a, b, c
    a1, a2, a3 = read_vertex_data(fp, a)
    b1, b2, b3 = read_vertex_data(fp, b)
    c1, c2, c3 = read_vertex_data(fp, c)
    
    # calculate ab 
    abDistance = compute_distance(a1, a2, a3, b1, b2, b3)
    # calculate ac
    acDistance = compute_distance(a1, a2, a3, c1, c2, c3)
    # calculate bc
    bcDistance = compute_distance(b1, b2, b3, c1, c2, c3)
    
    # calculate the area
    p = (abDistance + acDistance + bcDistance)/2
    area = math.sqrt(p*(p-abDistance) * (p-acDistance) * (p-bcDistance))
    
    print("Filename: " + fp.name)
    print("Index " + str(face_index) + " : " + str(area))
    return area
    
def is_connected_faces(fp, f1_ind, f2_ind):
    '''Are the faces connected?'''
    a1, b1, c1 = read_face_data(fp, f1_ind) 
    
    a2, b2, c2 = read_face_data(fp, f2_ind) 
    
    a=[a1,b1,c1]
    b=[a2,b2,c2]
    
    print("Filename:", fp.name)
    print("Index1   Index2  output")
    
    for i in range(3):
        for j in range(3):
            if (a[i] == b[j]):
                print(str(a[i])+"   "+str(b[j])+"   "+"TRUE")
            else:
                print(str(a[i])+"   "+str(b[j])+"   "+"FALSE")
  
    c = set(a) & set(b) # Turn the into sets and look for the similarities
    if(len(c) == 0):
        return False
    else:
        return True
    

        
def main():

    
    print('''\nWelcome to Computer Graphics!
We are creating and handling shapes. Any shape can be represented by polygon meshes, 
which is a collection of vertices, edges and faces.''')
    fp = open_file()   
    display_options()
    user_input = input("Enter your selection: ")
    while user_input != '6':
        if user_input == '1':
            for i in range(5):
                a, b, c = read_face_data(fp, i)
                print("{:^7s}{:^15s}").format('face', 'vertices')
                print(i, a, b, c)
            main()
        elif user_input == '2':
            face_index = input("Please enter an index. ")
            while True:
                if check_valid(fp,face_index,'face'):  
                    compute_face_normal(fp, face_index)
                    False
                else:
                    face_index = input("Please enter an index. ")
                
            main()
        elif user_input == '3':
            face_index = input("Please enter an index. ")
            while True:
                if check_valid(fp,face_index,'face'):  
                    compute_face_area(fp, face_index)
                    False
                else:
                    face_index = input("Please enter an index. ")
            main()
        elif user_input == '4':
            f1_ind = input("Please enter the first index. ")
            f2_ind = input("Please ender a second index.")
            while True:
                if check_valid(fp,f1_ind,'face'):  
                    if check_valid(fp,f1_ind,'face'):
                        compute_face_normal(fp, f1_ind, f2_ind)  
                        False
                else:
                    f1_ind = input("Please enter the first index. ")
                    f2_ind = input("Please ender a second index.")
            main()
        elif user_input == '5':
            fp.close()
            main()
        else:
            display_options()
            user_input = input("Enter your selection: ")


# Do not modify the next two lines.
if __name__ == "__main__":
    main() 