import sys, math

class Point:
    def __init__(self, x : float = 0, y : float = 0):
        self.x = x
        self.y = y
    

    def Distance_1(self, x2 : float, y2 : float) -> float:
        a = self.x - x2
        b = self.y - y2
        r = math.sqrt(a**2 + b**2)**2
        return r
  
    def Distance_2(self, Z):
        a = self.x - Z.x
        b = self.y - Z.y
        r = math.sqrt(a**2 + b**2)**2
        return r

def main():
    OBJ = Point(5.2, 3.7)
    OBJ2 = Point(7, 9)

    print(OBJ.x)
    print(OBJ.y)
    print(OBJ2.x)
    print(OBJ2.y)


    print("calcul dist1")

    z = OBJ.Distance_1(7, 9)
    print(z)

    print("calcul dist2")

    z2 = OBJ.Distance_2(OBJ2)
    print(z2)
  
  
if __name__=="__main__":
    sys.exit(main())




