#ejercicio 4 semana 11 

class Head:
    def __init__(self, eyes=2, nose=True, ears=True, mouth=True):
        self.eyes =eyes
        self.nose =nose
        self.ears = ears
        self.mouth = mouth

class Torso:
    def __init__(self, heart=True, lungs=2):
        self.heart = heart
        self.lungs = lungs

class Arm:
    def __init__(self, side):
        self.side = side 
        self.hand =Hand(side)#definimos izq o derch

class Hand:
    def __init__(self, side, fingers=5):
        self.side = side
        self.fingers = fingers

class Leg:
    def __init__(self, side):
        self.side = side 
        self.feet =Feet(side)#definimos izq o derch

class Feet:
    def __init__(self, side, toes=5):
        self.side = side
        self.toes = toes

class Human:
    def __init__(self, name, ):
        self.name = name
        self.head = Head()
        self.torso = Torso()
        self.left_arm = Arm('left')
        self.right_arm = Arm('right')
        self.left_leg = Leg('left')
        self.right_leg = Leg('right')

    def describe(self):#metodo para describir a la persona en si 
        print(f"Human: {self.name}")
        print(f"Head with {self.head.eyes} eyes and mouth: {self.head.mouth} also nose {self.head.nose} and 2 ears {self.head.ears}")
        print(f"Torso with heart: {self.torso.heart} and lungs {self.torso.lungs}")
        print(f'left hand fingers: {self.left_arm.hand.fingers}')
        print(f'Right hand fingers: {self.right_arm.hand.fingers}')
        print(f'left foot toes: {self.left_leg.feet.toes}')
        print(f'Right foot toes: {self.right_leg.feet.toes}')

Person = Human("Hugo")
Person.describe()