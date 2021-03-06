import pyglet
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet import image

def RenderMode3D(window):
	width, height = window.get_size()
	glEnable(GL_DEPTH_TEST)
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(65.0, width / float(height), 0.1, 60.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def Generate3DRender(blocklist, c):
	r=pyglet.graphics.Batch()
	for pos in blocklist:
		x,y,z=pos
		#north
		if (x,y,z-1) not in blocklist:
			r.add(4, GL_QUADS, c.blocks[blocklist[pos].mod][blocklist[pos].id].north,('v3f/static', (x+0.5,y-0.5,z-0.5, x-0.5,y-0.5,z-0.5, x-0.5,y+0.5,z-0.5, x+0.5,y+0.5,z-0.5)), ('t2f/static', (0,0,1,0,1,1,0,1)))
		#south
		if (x,y,z+1) not in blocklist:
			r.add(4, GL_QUADS, c.blocks[blocklist[pos].mod][blocklist[pos].id].south,('v3f/static', (x-0.5,y-0.5,z+0.5, x+0.5,y-0.5,z+0.5, x+0.5,y+0.5,z+0.5, x-0.5,y+0.5,z+0.5)), ('t2f/static', (0,0,1,0,1,1,0,1)))
		#top
		if (x,y+1,z) not in blocklist:
			r.add(4, GL_QUADS, c.blocks[blocklist[pos].mod][blocklist[pos].id].top,('v3f/static', (x-0.5,y+0.5,z-0.5, x-0.5,y+0.5,z+0.5, x+0.5,y+0.5,z+0.5, x+0.5,y+0.5,z-0.5)), ('t2f/static', [0,0,1,0,1,1,0,1]))
		#bottom
		if (x,y-1,z) not in blocklist:
			r.add(4, GL_QUADS, c.blocks[blocklist[pos].mod][blocklist[pos].id].bottom,('v3f/static', (x-0.5,y-0.5,z-0.5, x+0.5,y-0.5,z-0.5, x+0.5,y-0.5,z+0.5, x-0.5,y-0.5,z+0.5)), ('t2f/static', (0,0,1,0,1,1,0,1)))
		#west
		if (x-1,y,z) not in blocklist:
			r.add(4, GL_QUADS, c.blocks[blocklist[pos].mod][blocklist[pos].id].west,('v3f/static', (x-0.5,y-0.5,z-0.5, x-0.5,y-0.5,z+0.5, x-0.5,y+0.5,z+0.5, x-0.5,y+0.5,z-0.5)), ('t2f/static', (0,0,1,0,1,1,0,1)))
		#east
		if (x+1,y,z) not in blocklist:
			r.add(4, GL_QUADS, c.blocks[blocklist[pos].mod][blocklist[pos].id].east,('v3f/static', (x+0.5,y-0.5,z+0.5, x+0.5,y-0.5,z-0.5, x+0.5,y+0.5,z-0.5, x+0.5,y+0.5,z+0.5)), ('t2f/static', (0,0,1,0,1,1,0,1)))
	return r

def RenderSelectBlock(pos):
	x,y,z=pos
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
	glColor3d(0, 0, 0)
	#north
	pyglet.graphics.draw(4, GL_QUADS, ('v3f/static', (x+0.5,y-0.5,z-0.5, x-0.5,y-0.5,z-0.5, x-0.5,y+0.5,z-0.5, x+0.5,y+0.5,z-0.5)))
	#south
	pyglet.graphics.draw(4, GL_QUADS,('v3f/static', (x-0.5,y-0.5,z+0.5, x+0.5,y-0.5,z+0.5, x+0.5,y+0.5,z+0.5, x-0.5,y+0.5,z+0.5)))
	#top
	pyglet.graphics.draw(4, GL_QUADS,('v3f/static', (x-0.5,y+0.5,z-0.5, x-0.5,y+0.5,z+0.5, x+0.5,y+0.5,z+0.5, x+0.5,y+0.5,z-0.5)))
	#bottom
	pyglet.graphics.draw(4, GL_QUADS,('v3f/static', (x-0.5,y-0.5,z-0.5, x+0.5,y-0.5,z-0.5, x+0.5,y-0.5,z+0.5, x-0.5,y-0.5,z+0.5)))
	#west
	pyglet.graphics.draw(4, GL_QUADS,('v3f/static', (x-0.5,y-0.5,z-0.5, x-0.5,y-0.5,z+0.5, x-0.5,y+0.5,z+0.5, x-0.5,y+0.5,z-0.5)))
	#east
	pyglet.graphics.draw(4, GL_QUADS,('v3f/static', (x+0.5,y-0.5,z+0.5, x+0.5,y-0.5,z-0.5, x+0.5,y+0.5,z-0.5, x+0.5,y+0.5,z+0.5)))
	glColor3d(1, 1, 1)
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)