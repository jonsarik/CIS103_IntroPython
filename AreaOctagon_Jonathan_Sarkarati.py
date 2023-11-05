# Created by Jonathan Sarkarati
# 11/2/23
# Derived from Chapter 5, Exercise 5.3.4 in
# The Practice of Computing Using Python, 3rd Ed
# Area of an Octagon
import math

def main():
    print_intro()   # Program description

    # Priming the loop
    more_octagons = 'y'
    while more_octagons.lower() == 'y':
        x1, y1, x2, y2 = get_octagon()      # Get coordinates
        area = calculate_area(x1,y1,x2,y2)  # Calculate area
        print(f'Area is {area:,.2f}')
        print('---------------------')
        print()
        
        # Any more octagons?
        more_octagons = input('Find the area for another octagon? (y = yes): ')
    exit_program()
        
# Explain purpose of program
def print_intro():
    print("""
+===============================================+
| This program calculates the area of a regular |
| octagon with triangles if the radius          | 
| is known using Euclidean coordinates (x,y)!   |
+===============================================+
    """)

#   Get all coordinates for center and radius
def get_octagon():
    print()
    print('Octagon Center')
    x1,y1 = get_coord()
    print('Vertex')
    x2,y2 = get_coord()
    return x1, y1, x2, y2

# Get coordinates of a vertex
def get_coord():
    x = float(input('   Please enter x: '))
    y = float(input('   Please enter y: '))
    return x,y

# Calculate leg, and areas for triangle and octagon
def calculate_area(x1,y1,x2,y2):
    """return triangle area times eight"""
    leg_a = leg_b = leg_length(x1,y1,x2,y2)
    triangle_area = get_triangle_area(leg_a, leg_b)
    return 8 * triangle_area

# Calculate area of isosceles triangle
def get_triangle_area(leg_a, leg_b):
    """Vertex angle = 45 degrees. sin(45) = (sqrt 2)/2"""
    return (1/2) * leg_a * leg_b * math.sqrt(2)/2

# Calculate the Euclidean length of one leg
def leg_length(x1,y1,x2,y2):
    """return length of leg (Euclidean distance)"""
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# End program
def exit_program():
    print()
    print('Exiting program...')
    print('Goodbye!')

if __name__ == '__main__':
    main()
