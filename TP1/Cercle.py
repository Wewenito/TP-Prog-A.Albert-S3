import sys
import math
import Point as P

class Cercle:
    def __init__(self, centre : object = P.Point(0,0), rayon : float = 5):
        self.centre = centre
        self.rayon = rayon

    def calcul_diametre(self) -> float:
        d = self.rayon * 2
        return d
    
    def calcul_perimetre(self) -> float:
        p = 2 * math.pi * self.rayon
        return p
    
    def calcul_surface(self) -> float:
        s = math.pi * (self.rayon**2)
        return s
    
    def check_intersection(self, obj_c : object):
        diff =  obj_c.centre.Distance_1(self.centre.x, self.centre.y)
        if diff < self.calcul_diametre():
            return True
        else:
            return False
    
    def check_point(self):
        dist = self.centre.Distance_1(8,8)#Changer ici la valeur du point que l'on veut tester
        print(f'dist is : {dist}')
        if dist < self.rayon:
            print("point dans le cercle")
            return True
        else:
            print("point pas dans cercle")   
            return False  

def main():
    CERCLE = Cercle(P.Point(3,3), 3)
    CERCLE2 = Cercle(P.Point(4,4), 1)

    print(CERCLE.centre.x)
    print(CERCLE.centre.y)
    print(CERCLE.calcul_diametre())
    print(CERCLE.calcul_perimetre())
    print(CERCLE.calcul_surface())
    print(CERCLE.check_intersection(CERCLE2))
    CERCLE.check_point()



if __name__=="__main__":
    sys.exit(main())
