import svgwrite
import math

#vertices = 96
#outside_ellipse_height = 120
#outside_ellipse_width = 100
#inside_ellipse_height = 90
#inside_ellipse_width = 75

with open('consts.txt') as f:
    lines = f.readlines()
    # A list containing the values of the constants
    consts = [float(line) for line in lines if not line.startswith('#')]
    vertices, outside_ellipse_height, outside_ellipse_width, inside_ellipse_height, inside_ellipse_width = consts

vertices = int(vertices)
pointes = []
dwg = svgwrite.Drawing('star.svg', profile='tiny', size=(outside_ellipse_width*3.78, outside_ellipse_height*3.78))
for z in range(vertices):
    t = z * 2 * math.pi / vertices
    x1 = outside_ellipse_width * math.cos(t) / 2 + outside_ellipse_width/2
    y1 = outside_ellipse_height * math.sin(t) / 2 + outside_ellipse_height/2
    t += math.pi / vertices
    x2 = inside_ellipse_width * math.cos(t) / 2 + outside_ellipse_width/2
    y2 = inside_ellipse_height * math.sin(t) / 2 + outside_ellipse_height/2
    t -= 2 * math.pi / vertices
    #x3 = inside_ellipse_width * math.cos(t) / 2
    #y3 = inside_ellipse_height * math.sin(t) / 2
    pointes.append((x1*3.78, y1*3.78))
    pointes.append((x2*3.78, y2*3.78))

star = dwg.polygon(points=pointes, fill='none', stroke='black', stroke_width=0.1)
dwg.add(star)
dwg.save()
