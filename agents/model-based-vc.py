# model-based reflex agent

import random

class Agent:

	def __init__(self, world):
		self.state = world
		# rules mapping states to actions
		self.rules = {
			'A': {
				'clean': 'right',
				'dirty': 'suck'
			},
			'B': {
				'clean': 'left',
				'dirty': 'suck'
			}
		}
		self.action = None

	def __str__(self):
		return 'Action: {}\nWorld: {}\n'.format(self.action, self.state)

	# in principle, we take both room and floor as inputs, so that we don't
	# only rely on our internal model of the world since last perception
	def agent_function(self, percept):
		"""Takes percept with properties room and floor and returns action"""
		room = percept['room']
		floor = percept['floor']
		self.action = self.rules[room][floor]

	def act(self):
		"""Update state based on model of the world"""
		if self.action:
			if self.action == 'suck':
				pos = self.state['position']
				self.state[pos] = 'clean'
			elif self.action == 'left':
				self.state['position'] = 'A'
			else:
				self.state['position'] = 'B'

	# this is not really sensing, just relying on internal model
	# and previous actions
	def sense(self):
		"""Returns percept, i.e. room and floor"""
		room = self.state['position']
		floor = self.state[room]
		return { 'room': room, 'floor': floor }

# iterate for predefined number of steps
# TODO: iterate until world is clean, then stop
def clean(vc, initial_percept, iterations):
	def step(vc, percept, count):
		vc.agent_function(percept)
		vc.act()
		print(vc)
		percept = vc.sense()
		count -= 1
		if count > 0:
			step(vc, percept, count)

	step(vc, initial_percept, iterations)


if __name__ == '__main__':
	states = ['clean', 'dirty']
	locations = ['A', 'B']

	# initial state of the world
	world = {
		'A': random.choice(states),
		'B': random.choice(states),
		'position': random.choice(locations)
	}

	vacuum_cleaner = Agent(world)

	initial_percept = {
		'room': world['position'],
		'floor': world[world['position']]
	}

	print('# Initial state')
	print(world)
	print ('# And clean...')
	clean(vacuum_cleaner, initial_percept, 4)
