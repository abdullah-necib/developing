import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

class CanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self,parent)
        self.context = glcanvas.GLContext(self)
        self.init = False
    
    
