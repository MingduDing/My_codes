from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		exit(1)

class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		# be sure to print out the last scene
		current_scene.enter()

class Death(Scene):
	quips = [
		"You died.  You kinda suck at this.",
		"Your mom would be proud... if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scene):
	def enter(self):
		action = raw_input("> ")
		if action == "shoot!":
			return 'death'
		elif action == "dodge!":
			return 'death'
		elif action == "tell a joke":
			return 'laser_weapon_armory'
		else:
			return 'central_corridor'

class LaserWeaponArmory(Scene):
	def enter(self):
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses < 9:
			guesses += 1
			guess = raw_input("[keypad]> ")
		
		if guess == code:
			return 'the_bridge'
		else:
			return 'death'

class TheBridge(Scene):
	def enter(self):
		print "You burst onto the Bridge with the netron destruct bomb"
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			return 'death'
			
		elif action == "slowly place the bomb":
			return 'escape_pod'
		else:
			return "the_bridge"

class EscapePod(Scene):
	def enter(self):
		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			return 'finished'

class Finished(Scene):
	def enter(self):
		return 'finished'

class Map(object):
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()