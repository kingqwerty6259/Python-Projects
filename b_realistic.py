from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

brick = 'brick'
white = 'white_cube'
wood = 'wood'
block_pick = 1
window.fps_counter.enabled = False
window.exit_button.visible = False
def update():
	global block_pick

	if held_keys['1']: 
		block_pick = 1
	if held_keys['2']: 
		block_pick = 2
	if held_keys['3']: 
		block_pick = 3
	if held_keys['4']: 
		block_pick = 4
	if held_keys['5']: 
		block_pick = 5
	if held_keys['6']: 
		block_pick = 6
	if held_keys['7']: 
		block_pick = 7
	if held_keys['8']: 
		block_pick = 8
	if held_keys['9']: 
		block_pick = 9
	if held_keys['0']: 
		block_pick = 0
	if held_keys == ['scroll wheel up']:
		block_pick = block_pick + 1
class Voxel(Button):
	def __init__(self, position = (0,0,0),texture = white, color = color.white, highlight = color.gray):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			orgin_y = 0.5,
			texture = texture,
			color = color,
			highlight_color = highlight)
	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = white)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = brick)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, color = color.red)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, color = color.blue)
				if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, color = color.yellow)
				if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, color = color.green)
				if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, color = color.brown)
				if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, color = color.black)
				if block_pick == 9: voxel = Voxel(position = self.position + mouse.normal, color = color.orange)
				if block_pick == 0: voxel = Voxel(position = self.position + mouse.normal, color = color.pink)
			if  key == 'right mouse down':
				destroy(self)

			if key == 'f':
				gravity = -50
			
class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = "sphere",
			color = color.black,
			scale = 150,
			double_sided = True)

sky = Sky()

for z in range(30):
	for x in range(30):
		voxel = Voxel(position =(x,0,z))


player = FirstPersonController()
app.run()