class Point:
    def move(self):
        print('move')
    def draw(self):
        print('draw')

point1=Point()
point1.draw()
point1.move()
point1.x=10
point1.y=20
print(f"({point1.x}, {point1.y})")
point2=Point()#Si no tiene instanciado algun atributo no puede accederlo
#Se puede modificar y agregar atributos en tiempo de ejecucion
#point2 no tiene x ni y como atributos por lo tanto intentar accederlos no es posible
#hasta asignar valores
#Constructores
class Point2:
    def __init__(self,x,y):
        self.x=x
        self.y=y

point3 =Point2(11,20)
print(f"({point3.x}, {point3.y})")