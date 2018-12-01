# import numpy as HELLOJOSH
from operator import add
from operator import
import itertools
import numpy as np

vertices = []
faces = []
new_faces = []

def translate(vertex, xt=0, yt=0, zt=0):
    temp = vertex
    Mtranslate = [[1, 0, 0, xt],
                 [0, 1, 0, yt],
                 [0, 0, 1, zt]
                 [0, 0, 0, 1]]
    temp.append(float(1))
    res = [0, 0, 0, 0]
    for i_row, row in enumerate(Mtranslate):
        for i_colomn, v in enumerate(row):
            res[i_row] = temp[i_colomn]*v
    return res[0:2]


def lightItUp(face, lighting_vector):
    face_v1 = list(map(sub, face[1], face[0]))
    face_v2 = list(map(sub, face[2], face[0]))
    cross = np.cross(face_v1, face_v2)
    dotprod = dot(cross, lighting_vector)

def dot(K, L):
   if len(K) != len(L):
      return 0

   return sum(i[0] * i[1] for i in zip(K, L))

def project(vertex, screen_width=200, screen_height=200, screen_depth=5):
    new_x = (((vertex[0]/4)+1)/2)*screen_width
    new_y = (((vertex[1]/4)+1)/2)*screen_height
    new_z = (((vertex[2]/4)+1)/2)*screen_depth
    vertex = [new_x, new_y, new_z]

def plotLineLow(x0,y0, x1,y1):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0

    for x in linrange(x0,x1+1):
    plot(x,y)
    if D > 0:
       y = y + yi
       D = D - 2*dx
    D = D + 2*dy

def plotLineHigh(x0,y0, x1,y1):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0

    for y in linrange(y0,y1+1):
        plot(x,y)
        if D > 0:
           x = x + xi
           D = D - 2*dy
        D = D + 2*dx

def plotLine(x0,y0, x1,y1):
    """Plot line"""
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
          plotLineLow(x1, y1, x0, y0)
        else:
          plotLineLow(x0, y0, x1, y1)
    else:
        if y0 > y1
          plotLineHigh(x1, y1, x0, y0)
        else
          plotLineHigh(x0, y0, x1, y1)

def raster():
    """Raster"""
    z_buffer =
    color_buffer =



if __name__ == "__main__":
    # np.do_shit(shit)
    objFile = open('triangles.obj', 'r')

    for line in objFile:
        split = line.split()
        # print(split)
        if split[0] == 'v':
            vertices.append([float(split[1]), float(split[2]), float(split[3])])
        elif split[0] == 'f':
            faces.append([vertices[int(split[1])-1], vertices[int(split[2])-1], vertices[int(split[3])-1]])

    for i, face in enumerate(faces):
        face_a = []
        for vertex in face:
            face_a.append(translate(vertex, 100, 100))
        new_faces.append(face_a)
    print(new_faces) """Debug if neeeded"""


    print(vertices)
    print(faces)
    objFile.close()
# finalTexture = open('finalTexture.txt', 'w')
# finalVertex = open('finalVertex.txt', 'w')
#
#
# vertexList = []
# textureList = []
#
# finalVertexList = []
# finalTextureList = []
#
# for line in objFile:
# 	split = line.split()
	#if blank line, skip
	# if not len(split):
	# 	continue
	# if split[0] == "v":
	# 	vertexList.append(split[1:])
	# elif split[0] == "vt":
	# 	textureList.append(split[1:])
	# elif split[0] == "f":
	# 	count=1
	# 	firstSet=[]
	# 	secondSet=[]
	# 	firstTextureSet=[]
	# 	secondTextureSet = []
	# 	while count<5:
	# 		removeSlash = split[count].split('/')
	# 		if count == 1:
	# 			firstSet.append(vertexList[int(removeSlash[0])-1])
	# 			secondSet.append(vertexList[int(removeSlash[0])-1])
	# 			firstTextureSet.append(textureList[int(removeSlash[1])-1])
	# 			secondTextureSet.append(textureList[int(removeSlash[1])-1])
	# 		elif count == 2:
	# 			firstSet.append(vertexList[int(removeSlash[0])-1])
	# 			firstTextureSet.append(textureList[int(removeSlash[1])-1])
	# 		elif count == 3:
	# 			firstSet.append(vertexList[int(removeSlash[0])-1])
	# 			secondSet.append(vertexList[int(removeSlash[0])-1])
	# 			firstTextureSet.append(textureList[int(removeSlash[1])-1])
	# 			secondTextureSet.append(textureList[int(removeSlash[1])-1])
	# 		elif count == 4:
	# 			secondSet.append(vertexList[int(removeSlash[0])-1])
	# 			secondTextureSet.append(textureList[int(removeSlash[1])-1])
    #
	# 		count+=1
	# 	finalVertexList.append(firstSet)
	# 	finalVertexList.append(secondSet)
	# 	finalTextureList.append(firstTextureSet)
	# 	finalTextureList.append(secondTextureSet)
#
#
# vertexCount = 0
# for item in finalVertexList:
# 	for cordinateTrio in item:
# 		for cordinate in cordinateTrio:
# 			finalVertex.write(str(cordinate)+'f*x, ')
# 	vertexCount += 1
#
# textureCount = 0
# for item in finalTextureList:
# 	for cordinateTrio in item:
# 		for cordinate in cordinateTrio:
# 			finalTexture.write(str(cordinate)+'f, ')
# 	textureCount += 1
#
# print ("Total vertices: " + str(vertexCount*3))
# print ("Total texture cordinates: " + str(vertexCount*2))
#
# objFile.close()
# finalTexture.close()
# finalVertex.close()
