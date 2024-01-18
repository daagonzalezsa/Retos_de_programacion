import sys

def Area_polygon(Figure: str, L1, L2):
    """This function calculate the area of a polygon. For this,
    need three parameters:
    - Figure: This specify the type of the figure. Can be Triangle,
     Square and Rectangle.
    -  L1: Is one of the sides of the figure. In the case of the Triange,
    this can be the high.
    - L2: Is the other side of the figure. In the case of the Triangle,
    could be the base."""

    if(not isinstance(Figure, str)):
        print("Figura debe ser un String")
    elif(not (Figure.lower() in ["square", "triangle", "rectangle"])):
        print("Figura debe ser Square, Triangle o Rectangle")
    elif(Figure.lower() == "square"):
        print(f"El área del cuadrado es {L1**2}")
    elif(Figure.lower() == "rectangle"):
        print(f"El área del rectángulo es {L1*L2}")
    else:
        print(f"El área del triángulo es {L1*L2/2}")
    
if __name__ == '__main__':
    Area_polygon(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))
