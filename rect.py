import svgwrite
import math

#vertices = 96
#outside_ellipse_height = 120
#outside_ellipse_width = 100
#inside_ellipse_height = 90
#inside_ellipse_width = 75

with open('consts_rects.txt') as f:
    lines = f.readlines()
    # A list containing the values of the constants
    consts = [float(line) for line in lines if not line.startswith('#')]
    x, y, z, o = consts
import svgwrite

def generate_rectangles(x, y, z, o):
    dwg = svgwrite.Drawing('rectangles.svg', profile='tiny')
    for i in range(x):
        for j in range(y):
            dwg.add(dwg.rect((i * z*3.78 + i * o*3.78, j * z*3.78 + j * o*3.78), (z*3.78, z*3.78), fill='none', stroke='black'))
    dwg.save()

# Example usage
generate_rectangles(5, 7, 20, 10)
