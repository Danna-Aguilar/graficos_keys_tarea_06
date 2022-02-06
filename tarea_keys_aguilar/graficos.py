#Importar librerias                             DANNA AGUILAR

from OpenGL.GL import *
from glew_wish import *
import glfw
import math

color = [1.0, 0.0, 0.0]
posicion = [0.0, 0.0]
velocidad = 0.05
posicioncuad = [0.0, 0.0]
velocidadcuad = 0.05

def key_callback(window, key, scancode, action, mods):
    global color, posicion, velocidad
    global posicioncuad, velocidadcuad

    #Que la tecla escape cierre ventana al ser presionada
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)
    #Cambiar de colores
    if key == glfw.KEY_R and action == glfw.PRESS: 
        color = [1.0, 0.0, 0.0]
    if key == glfw.KEY_G and action == glfw.PRESS: 
        color = [0.0, 1.0, 0.0]
    if key == glfw.KEY_B and action == glfw.PRESS: 
        color = [0.0, 0.0, 1.0]
    #Al presionar arriba se mueve hacia arriba
    if key == glfw.KEY_UP and (action == glfw.PRESS or glfw.REPEAT): 
        posicion[1] = posicion[1] + velocidad
    #Al presionar abajo se mueve hacia abajo
    if key == glfw.KEY_DOWN and (action == glfw.PRESS or glfw.REPEAT): 
        posicion[1] = posicion[1] - velocidad
    #Al presionar izquierda se mueve hacia la izquierda
    if key == glfw.KEY_RIGHT and (action == glfw.PRESS or glfw.REPEAT): 
        posicion[0] = posicion[0] + velocidad
    #Al presionar derecha se mueve hacia la derecha
    if key == glfw.KEY_LEFT and (action == glfw.PRESS or glfw.REPEAT): 
        posicion[0] = posicion[0] - velocidad


    if posicion[0] > 1:
        posicion [0] = -1
    if posicion[0] < -1:
        posicion [0] = 1
    if posicion[1] > 1:
        posicion [1] = -1
    if posicion[1] < -1:
        posicion [1] = 1


    #CUADRADO TAREA
    if key == glfw.KEY_W and (action == glfw.PRESS or glfw.REPEAT): 
        posicioncuad[1] = posicioncuad[1] + velocidadcuad

    if key == glfw.KEY_S and (action == glfw.PRESS or glfw.REPEAT): 
        posicioncuad[1] = posicioncuad[1] - velocidadcuad

    if key == glfw.KEY_D and (action == glfw.PRESS or glfw.REPEAT): 
        posicioncuad[0] = posicioncuad[0] + velocidadcuad

    if key == glfw.KEY_A and (action == glfw.PRESS or glfw.REPEAT): 
        posicioncuad[0] = posicioncuad[0] - velocidadcuad

    if posicioncuad[0] > 0.8:
        posicioncuad[0] = -1.15
    if posicioncuad[0] < -1.15:
        posicioncuad[0] = 0.8
    if posicioncuad[1] > 1.0:
        posicioncuad[1] = -1.0
    if posicioncuad[1] < -1.0:
        posicioncuad[1] = 1.0
 
def draw():
    global color
    global posicion
    global posicion2

    glPushMatrix()
    glTranslatef(posicion[0], posicion[1], 0.0)
    glBegin(GL_TRIANGLES)

    #COLOR
    glColor3f(color[0],color[1],color[2])
    
    #DIBUJAR VERT
    glVertex3f(-0.08,-0.08,0)
    glVertex3f(0,0.08,0)
    glVertex3f(0.08,-0.08,0)

    glEnd()
    glPopMatrix()

    #CUADRADO
    glPushMatrix()
    glTranslatef(posicioncuad[0], posicioncuad[1], 0.0)
    glBegin(GL_QUADS)

    #COLOR
    glColor3f(1,1,0)

    #DIBUJAR VERT
    glVertex3f(-0.2, -0.08, 0.0)
    glVertex3f(-0.4, -0.08, 0.0)
    glVertex3f(-0.4, 0.08, 0.0)
    glVertex3f(-0.2, 0.08, 0.0)


    glEnd()
    glPopMatrix()


def main():
    width = 700
    height = 700
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Establecer el key callback
    glfw.set_key_callback(window, key_callback)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer color de borrado
        glClearColor(0.7,0.7,0.7,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        draw()


        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
