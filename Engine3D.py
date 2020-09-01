from gr import Render, color
from obj import Obj, Texture
from shaders import *

r = Render(512,384)
print("renderizando fondo")
r.BgImage("./models/room.bmp")

print("renderizando modelo 1/5")
r.active_texture = Texture('./models/tv.bmp')
r.active_shader = gourad
#translate scale rotate
r.loadModel('./models/tv.obj', (250,60,-140), (60,60,60), (0,0,0))

print("renderizando modelo 2/5")
r.active_texture = Texture('./models/woodtex.bmp')
r.active_shader = gourad
#translate scale rotate
r.loadModel('./models/meja.obj', (250,165,20), (25,25,35), (10,90,0))

print("renderizando modelo 3/5")
r.active_texture = Texture('./models/pandas.bmp')
r.active_shader = gourad
#translate scale rotate
r.loadModel('./models/Panda.obj', (200,200,0), (8,8,8), (10,90,0))

print("renderizando modelo 4/5")
r.active_texture = Texture('./models/bearskin.bmp')
r.active_shader = gourad
#translate scale rotate
r.loadModel('./models/bear.obj', (310,170,0), (25,25,25), (10,-90,0))



print("renderizando modelo 5/5")
r.active_texture = Texture('./models/shade.bmp')
r.active_shader = gourad
#translate scale rotate
r.loadModel('./models/trash.obj', (55,90,0), (40,40,40), (10,0,0))

r.glFinish('output.bmp')
print("LISTO!")




