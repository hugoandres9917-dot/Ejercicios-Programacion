#Cree las siguientes clases:
#Head
#Torso
#Arm
#Hand
#Leg
#Feet
#Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.

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
        print(f"Persona: {self.name}")
        print(f"Cabeza con {self.head.eyes} ojos y boca: {self.head.mouth} tambien nariz {self.head.nose} y 2 orejas {self.head.ears}")
        print(f"Torso con corazon: {self.torso.heart} y pulmones {self.torso.lungs}")
        print(f'Mano izquierda dedos: {self.left_arm.hand.fingers}')
        print(f'Mano derecha dedos: {self.right_arm.hand.fingers}')
        print(f'Pie izquierdo dedos: {self.left_leg.feet.toes}')
        print(f'Pie derecho dedos: {self.right_leg.feet.toes}')

Person = Human("Hugo")
Person.describe()