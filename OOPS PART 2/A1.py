# self
#parameters

class Pallu:
    v="swatantra"
    def __init__(self,x,y,z) :
        self.age=x
        self.geneder=y
        self.numbrer=z
    def second(self):
        print(self.age,self.geneder)

poi=Pallu(15,'male',23455)
print(poi.age)
print(poi.numbrer)
print(poi.geneder)