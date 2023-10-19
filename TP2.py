class Weapon:
    def __init__(self, Ammunations : int , Range : int) -> None:
        ammunations = self.Ammunations
        range = self.Range

class LanceMissilesAntisurface :
    def __init__(self) -> None:
        ammunations = 50
        range = 100
    
    def fire_at(self, x : int, y : int, z : int) -> None:
        if z != 0 :
            self.ammunation -= 1
            raise TypeError("OutOfRangeError")
        
        elif self.ammunation == 0 :
            raise TypeError("NoAmmunitionError")
        
        else :
            self.ammunation -= 1
        
class LanceMissilesAntiair :
    def __init__(self) -> None:
        ammunations = 40
        range = 20
    
    def fire_at(self, x : int, y : int, z : int) -> None:
        if z <= 0 :
            self.ammunation -= 1
            raise TypeError("OutOfRangeError")
        
        elif self.ammunation == 0 :
            raise TypeError("NoAmmunitionError")
        
        else :
            self.ammunation -= 1       

class LanceTorpilles :
    def __init__(self) -> None:
        ammunations = 24
        range =  40
    
    def fire_at(self, x : int, y : int, z : int) -> None:
        if z < 0 :
            self.ammunation -= 1
            raise TypeError("OutOfRangeError")
        
        elif self.ammunation == 0 :
            raise TypeError("NoAmmunitionError")
        
        else :
            self.ammunation -= 1 


class Vessel:
    def __init__(self, Coordinates : tuple, Max_hits : int, Weapon : Weapon) -> None:
        self.coordinates = Coordinates
        self.max_hits = Max_hits #nombre d ehit pour mourir
        self.weapon = Weapon
    
    def go_to(self, x : int, y : int, z : int) -> None :
        self.coordinates = (x, y, z) 
    
    def get_coordinates(self) -> tuple:
        return self.coordinates
    
    def fire_at(self, x : int, y : int, z : int) -> None:
        self.weapon.fire_at(x, y, z)
        
class ChampdeBataille :
    def __init__(self, lenght, width, height ) -> None:
        lenght = self.lenght
        width = self.width
        height = self.height
        
        
    
    