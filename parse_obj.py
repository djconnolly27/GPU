# import numpy as HELLOJOSH
# from operator import add
# from operator import subtract
# import itertools
# import numpy as np
import time, math

width = 300
height = 300
depth = 255
# Initiaize Z buffer with max depth and color buffer to be a white canvas to start
z_buffer = [[depth for j in range(width)] for i in range(300)]
color_buffer = [[255 for j in range(width)] for i in range(300)]


def translate(vertex, xt=0, yt=0, zt=0):
    """Translate the object"""
    temp = vertex
    Mtranslate = [[1, 0, 0, xt],
                  [0, 1, 0, yt],
                  [0, 0, 1, zt],
                  [0, 0, 0, 1]]
    temp.append(float(1))
    res = [0, 0, 0, 0]
    for i_row, row in enumerate(Mtranslate):
        for i_colomn, v in enumerate(row):
            res[i_row] += temp[i_colomn]*v
    return res[0:3]


# def lightItUp(face, lighting_vector=[1.3,2.1,1.2]):
#     """Lighting"""
#     face_v1 = list(map(sub, face[1], face[0]))
#     face_v2 = list(map(sub, face[2], face[0]))
#     cross = np.cross(face_v1, face_v2)
#     dotprod = dot(cross, lighting_vector)


def dot(K, L):
    """Dot product"""
    if len(K) != len(L):
        return 0

    return sum(i[0] * i[1] for i in zip(K, L))


def project(vertex, screen_width=width, screen_height=height, screen_depth=depth):
    """Project onto the screen space"""
    new_x = int((((vertex[0]/4)+1)/2)*screen_width)
    new_y = int((((vertex[1]/4)+1)/2)*screen_height)
    new_z = int((((vertex[2]/4)+1)/2)*screen_depth)
    return [new_x, new_y, new_z]


def Bresenham3D(x1, y1, z1, x2, y2, z2):
    """Compute the edges of each face"""
    ListOfPoints = []
    ListOfPoints.append([x1, y1, z1])
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    dz = abs(z2 - z1)
    if (x2 > x1):
        xs = 1
    else:
        xs = -1
    if (y2 > y1):
        ys = 1
    else:
        ys = -1
    if (z2 > z1):
        zs = 1
    else:
        zs = -1

    # Driving axis is X-axis"
    if (dx >= dy and dx >= dz):
        p1 = 2 * dy - dx
        p2 = 2 * dz - dx
        while (x1 != x2):
            x1 += xs
            if (p1 >= 0):
                y1 += ys
                p1 -= 2 * dx
            if (p2 >= 0):
                z1 += zs
                p2 -= 2 * dx
            p1 += 2 * dy
            p2 += 2 * dz
            ListOfPoints.append([x1, y1, z1])

    # Driving axis is Y-axis"
    elif (dy >= dx and dy >= dz):
        p1 = 2 * dx - dy
        p2 = 2 * dz - dy
        while (y1 != y2):
            y1 += ys
            if (p1 >= 0):
                x1 += xs
                p1 -= 2 * dy
            if (p2 >= 0):
                z1 += zs
                p2 -= 2 * dy
            p1 += 2 * dx
            p2 += 2 * dz
            ListOfPoints.append([x1, y1, z1])

    # Driving axis is Z-axis"
    else:
        p1 = 2 * dy - dz
        p2 = 2 * dx - dz
        while (z1 != z2):
            z1 += zs
            if (p1 >= 0):
                y1 += ys
                p1 -= 2 * dz
            if (p2 >= 0):
                x1 += xs
                p2 -= 2 * dz
            p1 += 2 * dy
            p2 += 2 * dx
            ListOfPoints.append([x1, y1, z1])
    return ListOfPoints


def raster(edges):
    """Raster"""
    for edge in edges:
        for each in edge:
            if each[2] < z_buffer[each[0]][each[1]]:
                z_buffer[each[0]][each[1]] = each[2]
                color_buffer[each[0]][each[1]] = 0


def create_pgm(pixel_map):
    ''' Takes in list and creates a pgm file. '''
    filename = time.strftime("%Y%m%d-%H%M%S")
    fout = open(filename+".pgm", 'w')
    pgm_str = "P2\n#optional comment line\n"+str(width)+" "+str(height)+"\n"+str(depth)+"\n"
    for row in pixel_map:
        for pixel in row:
            pgm_str += str(pixel) + " "
        pgm_str += ("\n")
    fout.write(pgm_str)
    fout.close()


if __name__ == "__main__":

    objFile = open('triangle.obj', 'r')

    vertices = []
    faces = []
    new_faces = []
    plottable_edges = []
    D = 0

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
            face_a.append(translate(vertex, xt=0, yt=1))
        new_faces.append(face_a)
    # print("translated faces\n",new_faces, "\n") #"""Debug if neeeded"""

    # print(vertices)
    edges = []
    projection = []
    """Projection"""
    for i, face in enumerate(new_faces):
        face_pr = []
        for vertex in face:
            # print(vertex)
            face_pr.append(project(vertex))
        projection.append(face_pr)
    # print("projected faces\n", projection, "\n") #debug if needed

    # Make edges
    for i, face in enumerate(projection):
        edge1_temp = Bresenham3D(face[0][0], face[0][1], face[0][2], face[1][0], face[1][1], face[1][2])
        edge2_temp = Bresenham3D(face[2][0], face[2][1], face[0][2], face[1][0], face[1][1], face[1][2])
        edge3_temp = Bresenham3D(face[2][0], face[2][1], face[0][2], face[0][0], face[0][1], face[0][2])
        edges.append([edge1_temp, edge2_temp, edge3_temp])

    # Plot it onto the screen
    for face in edges:
        # print(edges[0][0])
        raster(face)

    create_pgm(color_buffer)
    objFile.close()
