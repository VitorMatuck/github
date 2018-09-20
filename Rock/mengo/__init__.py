import math

px1= int(input("Coordenada de px1: "))
px2= int(input("Coordenada de px2: "))
py1= int(input("Coordenada de py1: "))
py2= int(input("Coordenada de py2: "))
d=math.sqrt ((px1-px2)**2+(py1-py2)**2)
print("distancia entre os pontos",d)
