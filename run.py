import ctypes
import sys

sys.path.append('..')

import pyglet
from pyglet.gl import *

from pywavefront import visualization
import pywavefront

rotation = 0
meshes = pywavefront.Wavefront('ex.obj')
window = pyglet.window.Window()
lightfv = ctypes.c_float * 4


@window.event
def on_resize(width, height):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60., float(width)/height, 0.01, 100.)
    glMatrixMode(GL_MODELVIEW)
    return True

global rotatex, rotatey, zoom, frameNumber
rotatex = 0
rotatey = 0
zoom=0
frameNumber = 0

@window.event
def on_draw():
    global rotatex, rotatey, frameNumber
    frameNumber += 1
    glClearColor(210, 210, 210, 255)
    window.clear()
    glLoadIdentity()

    glLightfv(GL_LIGHT0, GL_POSITION, lightfv(-1.0, 1.0, 1.0, 0.0))
    glEnable(GL_LIGHT0)

    glTranslated(0.0, 0.0, -3.0+zoom)
    glRotatef(90.0+rotatex, 0.0, 1.0, 0.0)
    #glRotatef(rotatey, 1.0, 0.0, 0.0)
    glRotatef(90.0+rotatey, 0.0, 0.0, 1.0)

    glEnable(GL_LIGHTING)

    visualization.draw(meshes)
    file_num=str(frameNumber).zfill(5)
    filename="out/frame-"+file_num+'.png'
    pyglet.image.get_buffer_manager().get_color_buffer().save(filename)
global mousedownx, mousedowny
@window.event
def on_mouse_press(x, y, button, modifiers):
    global mousedownx, mousedowny
    mousedownx = x
    mousedowny = y
@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    global rotatex, rotatey, mousedownx, mousedowny
    rotatex += (x-mousedownx)/3
    if rotatex > 90.0:
        rotatex = 90.0
    elif rotatex < -270.0:
        rotatex = -270.0
    mousedownx = x
    rotatey += (y-mousedowny)/3
    if rotatey > 90.0:
        rotatey = 90.0
    elif rotatey < -90.0:
        rotatey = -90.0
    mousedowny = y
@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    global zoom
    zoom += scroll_y/4

def update(dt):
    global rotation
    rotation += 90.0 * dt

    if rotation > 720.0:
        rotation = 0.0


pyglet.clock.schedule(update)
pyglet.app.run()