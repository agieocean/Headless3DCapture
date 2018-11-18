import ctypes
import sys

sys.path.append('..')

# NOTE: Reference for running headless from processing docs
# https://github.com/processing/processing/wiki/Running-without-a-Display

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

global rotatex, rotatey, zoom, outName
rotatex = 0
rotatey = 0
zoom=0
outName = "test.png"

@window.event
def on_draw():
    global rotatex, rotatey, outName
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

    pyglet.image.get_buffer_manager().get_color_buffer().save(outName)

    exit()

pyglet.app.run()