from cmu_graphics import *

def onMouseMove(x, y):
    

    app.fondo = 'negro'

Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))

tierra = Grupo(
    Círculo(200, 200, 150, relleno=None, borde='grisOscuro'),
    Círculo(200, 50, 10, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))

    )
marte=Group(
    Círculo(200, 200, 120, relleno=None, borde='grisOscuro'),
    Circulo(200,320,8,relleno=gradiente('ladrillo','naranja', inicio='izquierda-superior'))
)
c1=Circulo(100,200,6,relleno=gradiente('negro','naranja',inicio='derecha'))
c1.dx=5
c1.dy=3
c2=Circulo(100,100,5,relleno=gradiente('negro','naranja',inicio='derecha'))
c2.dx=5
c2.dy=3
    
#JOSE RODALLEGA

tierra.dirección = 'sentido-horario'
marte.dirección = 'sentido-horario'
def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
        marte.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'
        marte.dirección = 'sentido-antihorario'
def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    c1.centroX +=c1.dx
    c2.centroX -=c2.dx
    c1.centroY +c1.dy
    c2.centroY -=c2.dy
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 3
        marte.rotarÁngulo += 6
    
    else:
        tierra.rotarÁngulo -= 3
        marte.rotarÁngulo -= 6
 
    if c1.superior<0 or c2.inferior>400 :
       c1.centroX -=c1.dx
       c2.centroX +=c2.dx
       c1.centroY -c1.dy
       c2.centroY +=c2.dy
    
    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1
    
       
cmu_graphics.run()